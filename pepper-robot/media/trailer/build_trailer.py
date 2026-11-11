#!/usr/bin/env python3
"""Build the "PEPPER REVIVAL — THE AWAKENING" teaser trailer.

Renders the four concept stills into a 1080p / 24 fps film with camera moves,
colour grading, light effects, particles, grain and title cards, and scores it
with an original synthesized soundtrack (piano, strings, electronics) plus
Pepper's voice line.

Requirements: python3 with numpy + Pillow, ffmpeg on PATH, Inter fonts.

    python3 build_trailer.py            # full render -> pepper-revival-the-awakening.mp4
    python3 build_trailer.py --preview  # contact sheet of key frames only
"""
import argparse
import math
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "pepper-revival-the-awakening.mp4"
W, H, FPS = 1920, 1080, 24
SW, SH = 1280, 720          # coordinate space of the stills
UP = 2                      # stills are pre-upscaled by this factor
DURATION = 25.5
SR = 48000
FONT_DIR = Path("/usr/share/fonts/opentype/inter")
rng = np.random.default_rng(2026)


# ----------------------------------------------------------------- helpers
def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def ramp(t, a, b):
    """0 -> 1 smoothly as t goes a -> b."""
    return smooth((t - a) / (b - a)) if b != a else float(t >= b)


def lerp(a, b, k):
    return a + (b - a) * k


def load_still(name):
    im = Image.open(HERE / "stills" / name).convert("RGB")
    im = im.resize((SW * UP, SH * UP), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=45, threshold=2))


def camera(still, cx, cy, z):
    """Sample the still with a virtual camera centred on (cx, cy) at zoom z."""
    vw, vh = SW / z, SH / z
    cx = min(max(cx, vw / 2), SW - vw / 2)
    cy = min(max(cy, vh / 2), SH - vh / 2)
    x0, y0 = cx - vw / 2, cy - vh / 2
    a = vw / W
    im = still.transform((W, H), Image.AFFINE,
                         (a * UP, 0, x0 * UP, 0, a * UP, y0 * UP), Image.BICUBIC)
    return np.asarray(im, np.float32) / 255.0, (x0, y0, a)


# low-res grid used to evaluate light effects in still coordinates
GW, GH = W // 4, H // 4
_gx, _gy = np.meshgrid(np.arange(GW, dtype=np.float32) * 4 + 2,
                       np.arange(GH, dtype=np.float32) * 4 + 2)


def upsample(field):
    im = Image.fromarray(np.clip(field * 255, 0, 255).astype(np.uint8))
    return np.asarray(im.resize((W, H), Image.BILINEAR), np.float32) / 255.0


def glow(frame, cam, points, sigma, colour, amp):
    """Additive soft light at still-space points."""
    if amp <= 0.002:
        return frame
    x0, y0, a = cam
    sx, sy = x0 + _gx * a, y0 + _gy * a
    f = np.zeros((GH, GW), np.float32)
    for px, py in points:
        f += np.exp(-((sx - px) ** 2 + (sy - py) ** 2) / (2 * sigma * sigma))
    f = upsample(np.clip(f, 0, 1)) * amp
    return frame + f[..., None] * np.asarray(colour, np.float32)


def ripple(frame, cam, origin, radius, width, colour, amp):
    """A ring of light travelling across lit surfaces (the 'electrical pulse')."""
    if amp <= 0.002:
        return frame
    x0, y0, a = cam
    sx, sy = x0 + _gx * a, y0 + _gy * a
    d = np.sqrt((sx - origin[0]) ** 2 + (sy - origin[1]) ** 2)
    f = upsample(np.exp(-((d - radius) ** 2) / (2 * width * width))) * amp
    luma = frame @ np.asarray([0.3, 0.59, 0.11], np.float32)
    return frame + (f * np.clip(luma * 1.6, 0, 1))[..., None] * np.asarray(colour, np.float32)


def grade(frame, sat=1.0, gain=(1, 1, 1), exposure=1.0, gamma=1.0):
    luma = (frame @ np.asarray([0.3, 0.59, 0.11], np.float32))[..., None]
    out = luma + (frame - luma) * sat
    out = out * (np.asarray(gain, np.float32) * exposure)
    if gamma != 1.0:
        out = np.clip(out, 0, None) ** gamma
    return out


class Particles:
    """Soft drifting motes rendered additively in output space."""

    def __init__(self, n, colour, vel, size=(1.2, 3.0), region=(0, 0, W, H), seed=1):
        r = np.random.default_rng(seed)
        self.n, self.colour, self.region = n, np.asarray(colour, np.float32), region
        self.p0 = r.random((n, 2))
        self.v = (np.asarray(vel) + r.normal(0, 1, (n, 2)) * np.abs(np.asarray(vel)).max() * 0.6)
        self.size = r.uniform(size[0], size[1], n)
        self.phase = r.random(n) * 6.283
        self.bright = r.uniform(0.25, 1.0, n)

    def draw(self, frame, t, amp):
        if amp <= 0.002:
            return frame
        x0, y0, x1, y1 = self.region
        rw, rh = x1 - x0, y1 - y0
        for i in range(self.n):
            x = x0 + (self.p0[i, 0] * rw + self.v[i, 0] * t + 14 * math.sin(t * 0.7 + self.phase[i])) % rw
            y = y0 + (self.p0[i, 1] * rh + self.v[i, 1] * t + 9 * math.cos(t * 0.5 + self.phase[i])) % rh
            s = self.size[i]
            r = int(s * 3) + 1
            xi, yi = int(x), int(y)
            if xi - r < 0 or yi - r < 0 or xi + r >= W or yi + r >= H:
                continue
            yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
            k = np.exp(-((xx - (x - xi)) ** 2 + (yy - (y - yi)) ** 2) / (2 * s * s)).astype(np.float32)
            tw = 0.6 + 0.4 * math.sin(t * 2.1 + self.phase[i] * 3)
            frame[yi - r:yi + r + 1, xi - r:xi + r + 1] += k[..., None] * self.colour * (amp * self.bright[i] * tw)
        return frame


def tracked_text(draw, centre_x, y, text, font, tracking, fill):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = centre_x - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking


def title_layers():
    def layer():
        return Image.new("L", (W, H), 0)

    f_title = ImageFont.truetype(str(FONT_DIR / "InterDisplay-ExtraLight.otf"), 118)
    f_tag = ImageFont.truetype(str(FONT_DIR / "Inter-Light.otf"), 38)
    f_sub = ImageFont.truetype(str(FONT_DIR / "Inter-Regular.otf"), 25)
    a, b, c, rule = layer(), layer(), layer(), layer()
    tracked_text(ImageDraw.Draw(a), W / 2, 395, "PEPPER REVIVAL", f_title, 30, 255)
    tracked_text(ImageDraw.Draw(b), W / 2, 590, "Forgotten technology. Reborn intelligence.", f_tag, 5, 255)
    tracked_text(ImageDraw.Draw(c), W / 2, 700, "THE AWAKENING — 2026", f_sub, 11, 255)
    ImageDraw.Draw(rule).rectangle((W / 2 - 150, 556, W / 2 + 150, 557), fill=255)
    bloom = a.filter(ImageFilter.GaussianBlur(22))
    return [np.asarray(x, np.float32) / 255.0 for x in (a, b, c, rule, bloom)]


# ------------------------------------------------------------------ picture
class Film:
    def __init__(self):
        self.s1 = load_still("01-forgotten.jpg")
        self.s2 = load_still("02-human-touch.jpg")
        self.s3 = load_still("03-ai-spark.jpg")
        self.s4 = load_still("04-rebirth.jpg")
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        self.vignette = (1 - 0.42 * np.clip(d - 0.35, 0, None) ** 1.6)[..., None].astype(np.float32)
        self.door = np.clip((xx / W - 0.25) / 0.75, 0, 1)[..., None] ** 1.5   # light entering from the right
        self.grain = [rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32) for _ in range(12)]
        self.dust = Particles(70, (0.75, 0.82, 1.0), (6, -3), (1.0, 2.6), (560, 0, 1500, 900), seed=3)
        self.sparks = Particles(110, (0.25, 0.75, 1.0), (4, -26), (1.0, 2.8), seed=5)
        self.embers = Particles(45, (1.0, 0.72, 0.38), (5, -8), (1.0, 2.4), seed=7)
        self.titles = title_layers()

    # each scene returns a linear-ish float frame
    def scene1(self, t):
        k = ramp(t, 0.0, 4.8)
        f, cam = camera(self.s1, lerp(640, 664, k), lerp(360, 236, k), lerp(1.0, 1.52, k))
        f = grade(f, sat=0.35, gain=(0.86, 0.95, 1.12), exposure=0.92)
        f = self.dust.draw(f, t, 0.30)
        warm = ramp(t, 3.7, 4.8)                       # the cupboard door opens
        return f + self.door * np.asarray((1.0, 0.66, 0.30), np.float32) * (0.55 * warm)

    def scene2(self, t):
        k = (t - 4.0) / 4.8
        f, cam = camera(self.s2, lerp(700, 655, k), lerp(352, 378, k), lerp(1.10, 1.27, smooth(k)))
        opened = ramp(t, 4.0, 5.6)
        f = grade(f, sat=lerp(0.55, 1.0, opened), gain=(1.04, 1.0, 0.94), exposure=lerp(0.45, 1.0, opened))
        # faint pulse travelling under the shell from the boy's hand
        p = (t - 6.2) / 1.1
        if 0 < p < 1:
            f = ripple(f, cam, (470, 440), 60 + 760 * p, 34, (0.30, 0.75, 1.0), 0.5 * math.sin(p * math.pi) ** 0.7)
        # ...nothing... then a tiny blue light flickers in the eyes
        e = 0.0
        if 7.45 <= t < 7.55:
            e = 0.55
        elif 7.68 <= t < 7.76:
            e = 0.35
        elif t >= 7.9:
            e = ramp(t, 7.9, 8.5) * (0.9 + 0.1 * math.sin(t * 30))
        eyes = [(815, 222), (1035, 275)]
        f = glow(f, cam, eyes, 9, (0.45, 0.85, 1.0), 1.0 * e)
        return glow(f, cam, eyes, 46, (0.10, 0.45, 1.0), 0.45 * e)

    def scene3(self, t):
        k = ramp(t, 8.4, 14.1)
        f, cam = camera(self.s3, lerp(790, 648, k), lerp(318, 360, k), lerp(1.42, 1.04, k))
        wake = ramp(t, 8.4, 11.5)
        f = grade(f, sat=lerp(0.8, 1.18, wake), exposure=lerp(0.78, 1.04, wake), gain=(0.97, 1.0, 1.05))
        pulse = 0.5 + 0.5 * math.sin((t - 8.4) * 2.2 * math.pi / 1.25)
        f = glow(f, cam, [(750, 462)], 130, (0.20, 0.70, 1.0), wake * (0.16 + 0.14 * pulse))   # touchscreen
        f = glow(f, cam, [(745, 216), (866, 226)], 30, (0.35, 0.80, 1.0), wake * 0.38)          # eyes
        return self.sparks.draw(f, t, 0.55 * wake)

    def scene4(self, t):
        k = ramp(t, 13.9, 19.9)
        f, cam = camera(self.s4, lerp(705, 640, k), lerp(285, 360, k), lerp(1.46, 1.0, k))
        f = grade(f, sat=1.08, gain=(1.03, 1.0, 0.98), exposure=1.03)
        breathe = 0.5 + 0.5 * math.sin((t - 14.0) * 1.6)
        f = glow(f, cam, [(748, 250)], 70, (0.30, 0.75, 1.0), 0.10 + 0.06 * breathe)            # chest screen
        return self.embers.draw(f, t, 0.35)

    def title(self, t):
        a, b, c, rule, bloom = self.titles
        out = np.zeros((H, W, 3), np.float32)
        fade = 1 - ramp(t, 24.3, 25.4)
        ka, kb, kc = ramp(t, 20.4, 21.9) * fade, ramp(t, 21.7, 22.9) * fade, ramp(t, 22.6, 23.7) * fade
        out += bloom[..., None] * np.asarray((0.10, 0.55, 0.95), np.float32) * (0.75 * ka)
        out += a[..., None] * np.asarray((0.96, 0.98, 1.0), np.float32) * ka
        out += rule[..., None] * np.asarray((1.0, 0.72, 0.36), np.float32) * kb
        out += b[..., None] * np.asarray((0.80, 0.86, 0.92), np.float32) * kb
        out += c[..., None] * np.asarray((0.35, 0.78, 1.0), np.float32) * kc
        return out

    def frame(self, n):
        t = n / FPS
        scenes = [  # (render, in start, in end, out start, out end)
            (self.scene1, 0.0, 0.0, 4.0, 4.8),
            (self.scene2, 4.0, 4.8, 8.4, 8.8),
            (self.scene3, 8.4, 8.8, 13.9, 14.1),
            (self.scene4, 13.9, 14.1, 99, 99),
        ]
        out = np.zeros((H, W, 3), np.float32)
        if t < 20.0:
            for fn, a0, a1, b0, b1 in scenes:
                if a0 <= t < b1:
                    w = (ramp(t, a0, a1) if a1 > a0 else 1.0) * (1 - ramp(t, b0, b1))
                    if w > 0.001:
                        out += fn(t) * w
            # light blooms on the two awakenings
            out += np.asarray((0.20, 0.62, 1.0), np.float32) * 0.30 * math.exp(-((t - 8.6) / 0.16) ** 2)
            out += np.asarray((1.0, 0.86, 0.66), np.float32) * 0.42 * math.exp(-((t - 14.0) / 0.13) ** 2)
            out *= self.vignette
            out *= ramp(t, 0.0, 1.3) * (1 - ramp(t, 19.0, 19.9))
        if t > 20.3:
            out += self.title(t)
        # filmic shoulder + grain
        out = np.where(out > 0.8, 0.8 + (1 - np.exp(-(out - 0.8) / 0.2)) * 0.2, out)
        g = self.grain[n % len(self.grain)]
        g = np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None]
        out = out + g * (0.013 if t < 20.0 else 0.005)
        return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)


# -------------------------------------------------------------------- sound
def m2f(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def spectral(x, shape):
    """Filter by multiplying the spectrum with shape(freqs)."""
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(x.shape[0], 1 / SR)
    g = shape(f)
    return np.fft.irfft(X * (g[:, None] if x.ndim == 2 else g), n=x.shape[0], axis=0)


def lowpass(x, fc, order=4):
    return spectral(x, lambda f: 1 / np.sqrt(1 + (f / fc) ** (2 * order)))


def highpass(x, fc, order=2):
    return spectral(x, lambda f: 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order)))


class Mix:
    def __init__(self):
        self.n = int(DURATION * SR)
        self.dry = np.zeros((self.n, 2))
        self.wet = np.zeros((self.n, 2))      # sent to the reverb

    def add(self, sig, start, pan=0.0, send=0.3, level=1.0):
        i = int(start * SR)
        if i >= self.n:
            return
        sig = sig[: self.n - i] * level
        if sig.ndim == 1:
            l, r = math.cos((pan + 1) * math.pi / 4), math.sin((pan + 1) * math.pi / 4)
            sig = np.stack([sig * l, sig * r], 1)
        self.dry[i:i + len(sig)] += sig
        self.wet[i:i + len(sig)] += sig * send


def env(n, attack, release):
    e = np.ones(n)
    a, r = int(attack * SR), int(release * SR)
    a, r = min(a, n), min(r, n)
    e[:a] = np.sin(np.linspace(0, np.pi / 2, a)) ** 2
    e[n - r:] *= np.cos(np.linspace(0, np.pi / 2, r)) ** 2
    return e


def piano(midi, dur=5.0, vel=1.0):
    f0 = m2f(midi)
    t = np.arange(int(dur * SR)) / SR
    out = np.zeros_like(t)
    for h in range(1, 13):
        f = f0 * h * math.sqrt(1 + 0.00035 * h * h)
        if f > 9000:
            break
        amp = (1 / h ** 1.35) * (0.6 + 0.4 * vel if h > 3 else 1.0)
        decay = (0.55 + 0.42 * h) * (f0 / 261.6) ** 0.35
        for det in (-0.35, 0.35):                    # two slightly detuned strings
            out += 0.5 * amp * np.sin(2 * np.pi * (f + det) * t + h) * np.exp(-t * decay)
    hammer = rng.normal(0, 1, len(t)) * np.exp(-t * 90) * 0.12
    out = (out + lowpass(hammer, 2500, 2)) * (1 - np.exp(-t * 600))
    return out * env(len(t), 0.001, 0.6) * vel * 0.33


def strings(midis, dur, attack=1.2, release=1.5, cutoff=2600, swell=None, seed=0):
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    out = np.zeros((n, 2))
    for j, m in enumerate(midis):
        f0 = m2f(m)
        for v in range(6):
            cents = r.uniform(-9, 9)
            vib = 1 + 0.0028 * np.sin(2 * np.pi * r.uniform(4.6, 5.6) * t + r.uniform(0, 6.28)) * np.minimum(t / 1.5, 1)
            ph = np.cumsum(f0 * 2 ** (cents / 1200) * vib) / SR + r.random()
            saw = 2 * (ph % 1) - 1
            pan = r.uniform(-0.8, 0.8)
            out[:, 0] += saw * math.cos((pan + 1) * math.pi / 4)
            out[:, 1] += saw * math.sin((pan + 1) * math.pi / 4)
    out = lowpass(out, cutoff, 2) / (6 * max(len(midis), 1)) ** 0.5
    e = env(n, attack, release)
    if swell is not None:
        e = e * np.interp(t, *swell)
    return out * e[:, None] * 0.5


def thump(f_hi=74, f_lo=38, dur=0.5, sweep=14, decay=9):
    t = np.arange(int(dur * SR)) / SR
    f = f_lo + (f_hi - f_lo) * np.exp(-t * sweep)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * decay) * (1 - np.exp(-t * 900))


def bell(midi, dur=2.2):
    f0 = m2f(midi)
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f0 * t) * np.exp(-t * 3.2) + 0.35 * np.sin(2 * np.pi * f0 * 2.76 * t) * np.exp(-t * 7) \
        + 0.18 * np.sin(2 * np.pi * f0 * 5.4 * t) * np.exp(-t * 12)
    return s * (1 - np.exp(-t * 500)) * 0.25


def pluck(midi, dur=0.7):
    f0 = m2f(midi)
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f0 * t) + 0.3 * np.sin(2 * np.pi * 2 * f0 * t) * np.exp(-t * 10)
    return s * np.exp(-t * 7.5) * (1 - np.exp(-t * 700)) * 0.2


def noise_bed(dur, lo, hi, seed):
    r = np.random.default_rng(seed)
    x = r.normal(0, 1, (int(dur * SR), 2))
    return highpass(lowpass(x, hi, 2), lo, 2)


def reverb(x, rt=2.6):
    n = int(rt * 1.3 * SR)
    t = np.arange(n) / SR
    r = np.random.default_rng(11)
    ir = r.normal(0, 1, (n, 2)) * np.exp(-t * 6.9 / rt)[:, None]
    ir[: int(0.012 * SR)] = 0
    ir = lowpass(ir, 5200, 1)
    ir /= np.sqrt((ir ** 2).sum(0))
    m = x.shape[0] + n
    y = np.fft.irfft(np.fft.rfft(x, m, axis=0) * np.fft.rfft(ir, m, axis=0), m, axis=0)
    return y[: x.shape[0]]


def read_wav(path):
    with wave.open(str(path)) as w:
        assert w.getframerate() == SR and w.getsampwidth() == 2
        d = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64) / 32768
        return d.reshape(-1, w.getnchannels()).mean(1)


def build_audio(path):
    mx = Mix()
    t_all = np.arange(mx.n) / SR

    # --- Scene 1: room tone, faint wind, a lonely piano ------------------
    room = noise_bed(10, 40, 420, 1) * 0.028
    gust = 0.55 + 0.45 * np.sin(2 * np.pi * 0.13 * np.arange(len(room)) / SR + 1.0)
    wind = noise_bed(10, 300, 1400, 2) * 0.022 * gust[:, None]
    mx.add((room + wind) * env(len(room), 1.2, 3.5)[:, None], 0.0, send=0.2)
    mx.add(strings([33, 45], 9.0, attack=3.0, release=2.5, cutoff=420, seed=1), 0.0, level=0.28, send=0.5)
    mx.add(piano(76, 5.5, 0.75), 1.0, pan=-0.15, send=0.75)       # E5
    mx.add(piano(72, 5.0, 0.55), 3.0, pan=0.15, send=0.75)        # C5

    # --- Scene 2: electronic heartbeat, then a rising note ---------------
    for i, bt in enumerate((5.25, 6.2, 7.15)):
        lvl = 0.42 + 0.09 * i
        mx.add(thump(), bt, send=0.25, level=lvl)
        mx.add(thump(66, 36, 0.42), bt + 0.27, send=0.25, level=lvl * 0.7)
    for bt in (7.45, 7.68):                                        # the eye flicker
        mx.add(bell(93, 0.6), bt, pan=0.3, send=0.6, level=0.35)
    n = int(1.9 * SR)
    tt = np.arange(n) / SR
    glide = m2f(57) * 2 ** (np.clip(tt / 1.5, 0, 1) ** 2)          # A3 -> A4
    rise = np.sin(2 * np.pi * np.cumsum(glide) / SR) + 0.4 * np.sin(4 * np.pi * np.cumsum(glide) / SR)
    mx.add(rise * (tt / 1.9) ** 2 * env(n, 0.3, 0.45) * 0.16, 6.9, send=0.7)
    mx.add(strings([57, 64, 69], 2.6, attack=1.9, release=0.7, cutoff=1800, seed=2), 6.4, level=0.5, send=0.5)

    # --- Scene 3: the AI spark — strings + synthesis, Am - F - G ---------
    mx.add(thump(60, 30, 1.4, 6, 3.2), 8.55, send=0.5, level=0.6)
    for i, m in enumerate((81, 84, 88, 93)):                       # system start-up chime
        mx.add(bell(m), 8.85 + i * 0.14, pan=-0.4 + 0.27 * i, send=0.7, level=0.55)
    chords = [
        (8.5, 2.3, [33, 45, 52, 57, 60, 64], [69, 72, 76, 81], 0.62),
        (10.35, 2.3, [29, 41, 48, 53, 57, 60], [69, 72, 77, 81], 0.74),
        (12.2, 2.3, [31, 43, 50, 55, 59, 62], [71, 74, 79, 83], 0.90),
    ]
    for start, dur, notes, arp, lvl in chords:
        mx.add(strings(notes, dur + 0.5, attack=0.7, release=0.9, cutoff=2300 + 900 * lvl, seed=int(start * 10)),
               start, level=lvl, send=0.45)
        mx.add(strings([notes[-1] + 12], dur + 0.5, attack=0.9, release=0.9, cutoff=4200, seed=int(start * 7)),
               start, level=lvl * 0.42, send=0.6)
        steps = int(dur / 0.1875)
        for s in range(steps):
            mx.add(pluck(arp[(s * 3) % len(arp)] + (12 if s % 8 == 7 else 0)), start + s * 0.1875,
                   pan=0.6 * math.sin(s * 1.3), send=0.55, level=0.42 * lvl)
    riser = noise_bed(1.8, 900, 7000, 3) * (np.linspace(0, 1, int(1.8 * SR)) ** 3)[:, None]
    mx.add(riser * 0.10, 12.2, send=0.4)

    # --- Scene 4: rebirth — C major, piano theme, Pepper speaks ----------
    mx.add(thump(70, 32, 2.0, 5, 2.2), 14.0, send=0.5, level=0.85)
    shimmer = noise_bed(2.6, 3500, 11000, 4) * np.exp(-np.arange(int(2.6 * SR)) / SR * 2.4)[:, None]
    mx.add(shimmer * 0.07, 14.0, send=0.6)
    mx.add(strings([36, 43, 48, 55, 60, 64, 67], 4.2, attack=0.25, release=1.2, cutoff=3200, seed=40), 14.0,
           level=0.92, send=0.45)
    mx.add(strings([79], 4.2, attack=0.5, release=1.2, cutoff=4500, seed=41), 14.0, level=0.36, send=0.6)
    mx.add(strings([41, 48, 53, 57, 60, 65], 3.2, attack=0.8, release=1.2, cutoff=2900, seed=42), 17.4,
           level=0.80, send=0.45)
    mx.add(strings([81], 3.2, attack=0.8, release=1.2, cutoff=4500, seed=43), 17.4, level=0.30, send=0.6)
    mx.add(strings([36, 43, 48, 55, 60, 64, 67, 72], 6.0, attack=0.9, release=4.2, cutoff=3000, seed=44), 19.8,
           level=0.80, send=0.5)
    for when, m, v in ((14.0, 79, .8), (14.45, 76, .6), (14.9, 72, .65),            # G E C
                       (18.75, 72, .55), (19.1, 74, .6), (19.45, 76, .65), (19.85, 79, .8),
                       (20.5, 84, .7), (20.5, 48, .7), (22.3, 79, .4), (23.4, 84, .32)):
        mx.add(piano(m, 5.0, v), when, pan=(m - 72) / 40, send=0.7)

    # reverb, master bus, voice
    music = mx.dry + reverb(mx.wet) * 0.9
    voice = read_wav(HERE / "audio" / "pepper_voice.wav")
    v0, v1 = 15.3, 15.3 + len(voice) / SR
    duck = 1 - 0.5 * (np.interp(t_all, [v0 - 0.4, v0, v1 - 0.2, v1 + 0.5], [0, 1, 1, 0]))
    music *= duck[:, None]
    vmix = Mix()
    vmix.add(voice, v0, send=1.0, level=0.9)
    out = music + vmix.dry + reverb(vmix.wet, 1.1) * 0.16
    out = highpass(out, 24, 2)
    out *= np.interp(t_all, [0, 0.4, DURATION - 2.2, DURATION - 0.15], [0, 1, 1, 0])[:, None]
    out = np.tanh(out / np.abs(out).max() * 1.5) / math.tanh(1.5) * 0.89
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((out * 32767).astype(np.int16).tobytes())


# --------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true", help="write a contact sheet instead of the film")
    ap.add_argument("--work", default="/tmp/pepper-trailer", help="scratch directory")
    args = ap.parse_args()
    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)
    film = Film()

    if args.preview:
        times = [0.3, 2.5, 4.4, 5.2, 6.7, 7.5, 8.3, 8.6, 10.0, 12.5, 14.0, 14.6, 17.0, 19.4, 22.0, 23.8]
        sheet = Image.new("RGB", (4 * 640, 4 * 360))
        for i, t in enumerate(times):
            im = Image.fromarray(film.frame(int(t * FPS))).resize((640, 360), Image.LANCZOS)
            sheet.paste(im, ((i % 4) * 640, (i // 4) * 360))
        sheet.save(work / "contact-sheet.jpg", quality=88)
        print(work / "contact-sheet.jpg")
        return

    wav = work / "soundtrack.wav"
    build_audio(wav)
    print("soundtrack written", flush=True)
    total = int(DURATION * FPS)
    ff = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
         "-i", "-", "-i", str(wav), "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "224k", "-movflags", "+faststart", "-shortest",
         "-metadata", "title=Pepper Revival — The Awakening", str(OUT)],
        stdin=subprocess.PIPE)
    for n in range(total):
        ff.stdin.write(film.frame(n).tobytes())
        if n % 48 == 0:
            print(f"frame {n}/{total}", flush=True)
    ff.stdin.close()
    sys.exit(ff.wait())


if __name__ == "__main__":
    main()
