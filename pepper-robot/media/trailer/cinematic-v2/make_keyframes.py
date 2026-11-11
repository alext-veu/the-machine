#!/usr/bin/env python3
"""Derive 1920x1080 start / end keyframes for AI video generators from the four concept stills.

    python3 make_keyframes.py     # writes frames/*.jpg

Each shot in README.md names the frames it uses. Requires numpy + Pillow.
"""
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build_trailer as bt  # noqa: E402  (reuses the camera / grade / glow helpers)

OUT = HERE / "frames"
W, H = bt.W, bt.H
rng = np.random.default_rng(7)


def still(name):
    return bt.camera(bt.load_still(name), 640, 360, 1.0)


def save(frame, name):
    frame = np.where(frame > 0.8, 0.8 + (1 - np.exp(-(frame - 0.8) / 0.2)) * 0.2, frame)
    Image.fromarray((np.clip(frame, 0, 1) * 255 + 0.5).astype(np.uint8)).save(OUT / name, quality=94)
    print(name)


def burst(frame, cam, centre):
    """Energy burst from the chest screen: core, radial rays and flying sparks."""
    x0, y0, a = cam
    cx, cy = (centre[0] - x0) / a, (centre[1] - y0) / a
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.hypot(xx - cx, yy - cy)
    ang = np.arctan2(yy - cy, xx - cx)
    spokes = rng.random(720) ** 5
    spokes = np.convolve(np.tile(spokes, 3), np.hanning(7) / np.hanning(7).sum(), "same")[720:1440]
    idx = ((ang + math.pi) / (2 * math.pi) * 719).astype(np.int32)
    rays = spokes[idx] * np.exp(-r / 520) * np.clip(r / 90, 0, 1)
    ring = np.exp(-((r - 430) ** 2) / (2 * 26 ** 2)) * 0.35
    core = np.exp(-(r ** 2) / (2 * 95 ** 2)) * 1.5 + np.exp(-(r ** 2) / (2 * 330 ** 2)) * 0.5
    cyan = np.asarray((0.35, 0.80, 1.0), np.float32)
    out = frame * 0.82 + (rays * 1.6 + ring)[..., None] * cyan + core[..., None] * np.asarray((0.75, 0.93, 1.0), np.float32)
    layer = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(layer)
    for _ in range(420):
        t, rad = rng.uniform(0, 2 * math.pi), 80 + 900 * rng.random() ** 1.6
        ln = rng.uniform(6, 46) * (0.4 + rad / 900)
        col = (255, 190, 110) if rng.random() < 0.22 else (150, 225, 255)
        p0 = (cx + math.cos(t) * rad, cy + math.sin(t) * rad)
        p1 = (cx + math.cos(t) * (rad + ln), cy + math.sin(t) * (rad + ln))
        d.line([p0, p1], fill=col, width=int(rng.integers(1, 4)))
    sparks = np.asarray(layer, np.float32) / 255
    halo = np.asarray(layer.filter(ImageFilter.GaussianBlur(7)), np.float32) / 255
    return out + sparks * 0.9 + halo * 1.4


def main():
    OUT.mkdir(exist_ok=True)
    f, cam = still("01-forgotten.jpg")
    cold = bt.grade(f, sat=0.35, gain=(0.86, 0.95, 1.12), exposure=0.95)
    save(cold, "s1-forgotten-start.jpg")
    door = np.clip((np.mgrid[0:H, 0:W][1] / W - 0.25) / 0.75, 0, 1)[..., None] ** 1.5
    save(cold + door * np.asarray((1.0, 0.66, 0.30), np.float32) * 0.6, "s2-door-light-end.jpg")

    f, cam = still("02-human-touch.jpg")
    save(bt.grade(f, sat=0.8, exposure=0.85), "s3-touch-start.jpg")
    eyes = [(815, 222), (1035, 275)]
    lit = bt.glow(bt.glow(f, cam, eyes, 9, (0.45, 0.85, 1.0), 1.0), cam, eyes, 46, (0.10, 0.45, 1.0), 0.45)
    save(lit, "s3-touch-end-eyes-lit.jpg")

    f, cam = still("03-ai-spark.jpg")
    save(bt.grade(f, sat=0.45, gain=(0.95, 0.98, 1.05), exposure=0.5), "s4-spark-start.jpg")
    save(burst(f, cam, (750, 462)), "s4-spark-peak.jpg")
    save(bt.grade(f, sat=1.12, exposure=1.03), "s5-awake-start.jpg")

    f, cam = still("04-rebirth.jpg")
    save(bt.grade(f, sat=1.06), "s6-rebirth-start.jpg")

    sheet = Image.new("RGB", (W, H), (8, 10, 14))
    for i, n in enumerate(("04-rebirth.jpg", "03-ai-spark.jpg", "02-human-touch.jpg", "01-forgotten.jpg")):
        im = Image.open(HERE.parent / "stills" / n).convert("RGB").resize((950, 534), Image.LANCZOS)
        sheet.paste(im, (5 + (i % 2) * 960, 3 + (i // 2) * 540))
    sheet.save(OUT / "pepper-reference-sheet.jpg", quality=93)
    print("pepper-reference-sheet.jpg")


if __name__ == "__main__":
    main()
