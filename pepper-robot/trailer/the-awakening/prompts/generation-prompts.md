# Generation prompts and edit record — The Awakening, version 3

This file is meant to hold the exact `GenerateImage` and `GenerateVideo` prompts used for every keyframe and clip in the final v3 cut, with parameters and trim points.

## Provenance

The finished assets, assembly scripts and edit timelines were recovered from the production workspace at `/workspace/pepper-revival/` on 11 November 2026. Trim points, grades, clip-to-keyframe matches, resolutions and durations below are taken from those files and from frame-matching the first frame of each v3 source clip to the still that generated it.

**The literal `GenerateImage` / `GenerateVideo` prompt strings were not persisted** in that workspace (no sidecar, script or log contains them) and were not available from an accessible tool-call transcript at the time this folder was added to the repository. They are therefore **not reconstructed here**. Inventing replacement prompt text would be misleading. Scene intention should be taken from [`original-brief.md`](original-brief.md); confirmed production parameters are below.

What is known about the generators:

- Keyframes were made with `GenerateImage`, then shots were animated with `GenerateVideo` (image-to-video) from those stills, as described during production.
- `GenerateImage` accepted `reference_image_paths`. Wikimedia Commons Pepper photographs in `../references/` were used for likeness; later shots also used earlier chosen stills and boy-lock crops for continuity. A production note in the original keyframe choices list records this.
- All stills in `../keyframes/` are 1280×720, 16:9 JPEG.
- All source clips used in the v3 picture are 1920×1088, 24 fps (then cropped to 1920×1080 with `crop=1920:1080:0:4` during grading). Clip durations fall on whole seconds plus a 1/24 s container remainder (4.042 s, 5.042 s, 6.042 s or 7.042 s), which is consistent with 4–7 second `GenerateVideo` requests.
- The title card was not generated as video text. It was a typographic still, faded and appended in ffmpeg.
- v1 and v2 takes, rejected stills and unused voice/score renders were deliberately omitted from this folder.

## Picture assembly (v3)

The v3 picture keeps the graded v2 cut of Scene 1, Scene 2, the spark montage and the head-lift, then replaces the surge and the whole of Scene 4. Scripts: `edit/assemble_v2.py` and `edit/assemble_v3.py` in the production workspace. Times below are from `edit/v3_timeline.json` unless noted. The delivered file is 29.000 s after mux (the pre-mux timeline total was 29.208 s).

Common grade prefix: `crop=1920:1080:0:4,setsar=1,fps=24,format=yuv420p`.

| Grade | Colour treatment |
| --- | --- |
| GRADE_S1 | `colortemperature=temperature=8200:mix=0.45,eq=saturation=0.80:contrast=1.05:brightness=-0.012,vignette=PI/7` |
| GRADE_S2 | `colortemperature=temperature=5000:mix=0.28,eq=saturation=0.92:contrast=1.03:brightness=-0.005,vignette=PI/7` |
| GRADE_CY | `colortemperature=temperature=6200:mix=0.22,colorbalance=bs=0.06:gs=0.02:rs=-0.02,eq=saturation=0.96:contrast=1.04,vignette=PI/8` |
| GRADE_S4 | `colortemperature=temperature=4600:mix=0.32,colorbalance=rm=-0.10:bm=0.08:rh=-0.08:bh=0.05:bs=0.04,eq=saturation=1.02:contrast=1.03:brightness=0.01,vignette=PI/8` |
| GRADE_BOY | `colortemperature=temperature=4800:mix=0.28,eq=saturation=1.00:contrast=1.03:brightness=0.01,vignette=PI/9` |

### Source clips in the final cut

For each clip: the still actually used (matched by first-frame similarity), the generated clip length, and the in/out trim used in the v3 timeline.

#### Scene 1 — Forgotten

- **Keyframe:** `keyframes/s1-forgotten-chosen.jpg` (identical to the earlier file `s1-forgotten-a.jpg`).
- **Clip:** `s1-forgotten-v1.mp4` — 6.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.00, dur=4.250 s, GRADE_S1.
- **In film:** 0.000–3.750 s (0.50 s crossfade into Scene 2).
- **Notes:** A later still `s1-forgotten-v2.jpg` exists in the workspace but was not the source of this clip. Opening stills also had a rejected tighter candidate (`s1-forgotten-b.jpg`), not included here.

#### Scene 2 — The human touch

- **Keyframe:** `keyframes/s2-v2-a.jpg` (v2 retake of the shoulder touch, used instead of the original `s2-human-touch-chosen.jpg`).
- **Clip:** `s2-human-touch-v2.mp4` — 7.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.04, dur=3.800 s, GRADE_S2 (trimmed before an eye-blaze at about 4.40 s).
- **In film:** 3.750 s until the spark montage at 7.583 s.

#### Scene 3 — Spark montage and awakening

The spark is a rapid cut sequence (not a single generated shot), with short white flashes and black frames inserted in ffmpeg, then a replaced surge and a head-lift.

**Seams pulse**

- **Keyframe:** `keyframes/ecu-seams.jpg`.
- **Clip:** `ecu-seams-pulse.mp4` — 4.042 s, 1920×1088, 24 fps, GRADE_CY.
- **Trims:** ss=0.00, dur=0.62 s (`seams_faint`, from 7.583 s); ss=1.15, dur=0.90 s (`seams_race`, from 12.745 s).

**Eye flicker**

- **Keyframes:** `keyframes/ecu-eye-dark.jpg` (first frame of the clip); `keyframes/ecu-eye-cyan.jpg` (lit-eye state used in the same shot).
- **Clip:** `ecu-eye-flicker.mp4` — 5.042 s, 1920×1088, 24 fps, GRADE_CY.
- **Trims (source-clip time → name):** ss=0.00 / 0.32 s `eye_dark1`; ss=0.55 / 0.36 s `eye_on1`; ss=1.86 / 0.24 s `eye_off`; ss=2.44 / 0.38 s `eye_on2`; ss=3.20 / 0.50 s `eye_on3`.
- **Inserted frames (not generated video):** 2 frames `0xE8FFFF` after `eye_dark1`; 3 frames black after `eye_on1`; 2 frames black after `eye_on2`; 2 frames `0xD8FFFF` after `eye_on3`.

**Tablet startup**

- **Keyframes:** `keyframes/ecu-tablet-dark.jpg` (first frame of the clip); `keyframes/ecu-tablet-glitch.jpg` and `keyframes/ecu-tablet-lit.jpg` (glitch and lit states used for this shot).
- **Clip:** `ecu-tablet-startup.mp4` — 5.042 s, 1920×1088, 24 fps, GRADE_CY. A sister take, `ecu-tablet-boot.mp4`, was not used (footwear visible).
- **Trims:** ss=0.00 / 0.22 s `tab_dark1`; ss=0.50 / 0.92 s `tab_glitch`; ss=3.10 / 0.36 s `tab_dark2`; ss=4.22 / 0.70 s `tab_on`.
- **Inserted frames:** 2 frames black after `tab_glitch`; 2 frames `0xC8FFFF` after `tab_dark2`.

**Surge (v3 replacement)**

- **Keyframe:** `keyframes/s3-surge-integrated-a.jpg`.
- **Clip:** `s3-surge-integrated.mp4` — 6.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.80, dur=3.300 s, GRADE_CY (bloom, avoiding a late hand lift and eye beams). This replaces the v2 surge from `s3-surge.mp4` (ss=0.85, dur=3.30 s).
- **In film:** 3-frame white flash `0xF4FFFF` at 13.645 s (`surge_impact`), then surge 13.770–17.145 s. Startup chime at 13.890 s.

**Head lift**

- **Keyframe:** `keyframes/s3-head-down.jpg`.
- **Clip:** `s3-headlift.mp4` — 5.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=2.50, dur=2.500 s, GRADE_CY (skips a warped head around 1.89 s).
- **In film:** from 17.108 s, joined with a 0.35 s `fadewhite` from the end of the spark block.

#### Scene 4 — Rebirth (v3 three-shot pack)

The v2 Scene 4 clip (`s4-rebirth-v3.mp4`) was discarded because of a ghost head, a tablet on the boy and a melting hand. v3 uses three tighter shots and keeps the two figures apart.

**Pepper MCU**

- **Keyframe:** `keyframes/s4-pepper-mcu-a.jpg`.
- **Clip:** `s4-pepper-mcu.mp4` — 5.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.00, dur=1.85 s, GRADE_S4 (before a fist pose at about 2.52 s).
- **In film:** from 19.408 s (hard cut into the boy CU).

**Boy close-up**

- **Keyframe:** `keyframes/s4-boy-cu-left.jpg`.
- **Clip:** `s4-boy-cu.mp4` — 4.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.12, dur=1.20 s, GRADE_BOY.
- **In film:** from 21.258 s, then a 0.30 s fade into the wide.

**Wide pull-back**

- **Keyframe:** `keyframes/s4-wide-a.jpg`.
- **Clip:** `s4-wide-pullback.mp4` — 6.042 s, 1920×1088, 24 fps.
- **Trim in cut:** ss=0.15, dur=3.00 s, GRADE_S4 (trimmed before late softening).
- **In film:** from 22.191 s. Picture fades to black from 24.608 s over 0.60 s. Picture ends 25.208 s.

#### Title card

- Typographic still (not AI-generated text), 4.0 s, fade in 0.50 s, fade out from 3.20 s over 0.80 s.
- In film: 25.208–29.208 s on the pre-mux timeline; delivered file is 29.000 s.
- On-screen title: **PEPPER REVIVAL** / Forgotten technology. Reborn intelligence. / THE AWAKENING — 2026.
- Spoken line is also burned in as a subtitle during Scene 4: “Hello, Boris. I've been waiting for you.” Voice starts at 19.958 s.

## Soundtrack

- Original score, synthesised in Python (`audio/compose_v3.py` in the production workspace): piano, strings and restrained electronics, with silence, crackles and a speeding heartbeat under the spark, then a startup chime on the surge.
- Mix: `audio/mix-v3.flac` (48 kHz, stereo, 29.21 s). Muxed AAC 192 kb/s, 48 kHz, stereo in the MP4.
- Voice line: Microsoft `edge-tts` voice **en-GB-RyanNeural**, rendered from `tts_ryan_med.mp3`, then light processing (no ring modulation; 6% chorus, 8% short reverb) so the British accent stays clear. Processed stem: `audio/pepper_line_v3_ryan_light.flac` (48 kHz, mono, 3.06 s). Line: “Hello, Boris. I've been waiting for you.”

## Reference images used for likeness

See `../references/sources.txt` for URLs, authors and licences. Eight Wikimedia Commons photographs of the original SoftBank / Aldebaran Pepper were the likeness set. Eye colour in `07-chest-tablet-pepper-a-humanoid-robot.jpg` is purple in the source photograph and was not to be copied.

Boy-lock stills (`boy-lock-profile.jpg`, `boy-lock-threequarter.jpg` and face crops from Scene 2) were used as continuity references when generating later keyframes. They are not start-frames of clips in the v3 cut, so they are not in `../keyframes/`.
