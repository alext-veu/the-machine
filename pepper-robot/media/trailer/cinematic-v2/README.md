# Pepper Revival — The Awakening: cinematic v2 shot pack

The first trailer (`../pepper-revival-the-awakening.mp4`) animates still images. This pack is for making a version with real motion — Pepper lifting his head, Boris walking in, an energy burst — using an AI image-to-video generator.

**The key change from the original prompt:** do not ask for one 20-second film. Generators hold a character far better when each shot is a separate 4–8 second generation that starts from one of our own images. Generate the seven shots below, pick the best take of each, then cut them together.

## Which tool

Capabilities below are from vendor and review pages read on 11 November 2026, not from our own tests. Check the current limits before paying.

| Tool | Why use it | Limits to know |
|---|---|---|
| **Kling 3.0** | Start-frame and end-frame control, strong character consistency, native 4K | 3–15 s per clip |
| **Google Veo 3.1** | Most polished lighting; generates dialogue and sound with the picture | 4, 6 or 8 s per clip; 4K is upscaled |
| **Grok Imagine Video 1.5** | Already in use; 1080p image-to-video with spoken dialogue; up to seven reference images | 1–15 s per clip; reference mode is 720p |
| **Seedance 2.0 / 2.5** | Many reference images per shot; longer clips | 2.5 stops at 1080p |
| **Runway Gen-4.5** | Follows camera direction closely | — |

Recommended route: generate the silent shots (1, 2, 3, 4 and 5) in **Kling 3.0** (it accepts our start and end frames) and the two shots with speech (2B and 6) in **Veo 3.1** or **Grok Imagine 1.5**. To stay in one subscription, do all seven in Grok Imagine 1.5 using image-to-video. A multi-model site such as Higgsfield gives access to several of these from one login.

Some generators restrict realistic images of children as input. If a shot with Boris is refused, use the alternative noted on that shot.

## Assets

Run `python3 make_keyframes.py` to regenerate. All frames are 1920×1080.

| File | Use |
|---|---|
| `frames/s1-forgotten-start.jpg` | Start frame, shots 1 and 2 |
| `frames/s2-door-light-end.jpg` | End frame, shot 2, and start frame, shot 2B (warm light from the open door) |
| `frames/s3-touch-start.jpg` | Start frame, shot 3 (eyes dark) |
| `frames/s3-touch-end-eyes-lit.jpg` | End frame, shot 3 (eyes glowing blue) |
| `frames/s4-spark-start.jpg` | Start frame, shot 4 (dim, before the spark) |
| `frames/s4-spark-peak.jpg` | End frame, shot 4 (energy burst at its peak) |
| `frames/s5-awake-start.jpg` | Start frame, shot 5 (fully lit) |
| `frames/s6-rebirth-start.jpg` | Start frame, shot 6 |
| `frames/pepper-reference-sheet.jpg` | Character reference where the tool accepts one |

A real photograph of our own Pepper, added as an extra reference image, will improve accuracy further.

## Style block

Paste this at the end of every shot prompt.

```
Photorealistic live-action science-fiction film, shot on a large-format cinema camera with anamorphic lenses, 24 fps, shallow depth of field, volumetric light, fine film grain. The robot is a SoftBank Pepper: glossy white plastic shell, rounded head with large round black eyes, small smile, tablet touchscreen on the chest, slender jointed arms with five-fingered hands, a single flared base on wheels with no legs. Keep the robot's shape, proportions and colour exactly as in the reference image. Robot movement is smooth, slow and motor-driven. No on-screen text, no subtitles, no logos, no extra fingers, no extra limbs, no legs or feet on the robot, no change of face, no cartoon look.
```

## Shots

### Shot 1 — Forgotten (5 s)

Start frame: `s1-forgotten-start.jpg`

```
A dusty white humanoid robot stands switched off in a dark, abandoned storage cupboard, head bowed, chest screen black. The robot does not move at all. Dust drifts slowly through a narrow shaft of cold moonlight. A cobweb strand sways. Camera: very slow dolly-in towards the robot's lowered face. Mood: lonely, silent. Colour: desaturated cold blue-grey.
Audio: quiet room tone, faint wind through a gap, one soft low piano note. No speech.
```

### Shot 2 — The door opens (5 s)

Start frame: `s1-forgotten-start.jpg` · End frame: `s2-door-light-end.jpg`

```
Same cupboard, same motionless robot. A door off-screen to the right creaks open and a widening blade of warm golden light sweeps across the floor, the boxes and the robot's dusty shell. The long shadow of a small boy falls across the robot and stops. Dust swirls in the new light. The robot stays completely still. Camera: locked off, then a slight push-in.
Audio: door creak, a soft footstep, wind fading, a held string note beginning. No speech.
```

Alternative if the boy's shadow is not wanted: remove the shadow sentence; the light alone tells the story.

### Shot 2B — "Who are you?" (7 s)

Start frame: `s2-door-light-end.jpg` · Reference image for the boy: `pepper-reference-sheet.jpg` (top-left panel)

```
Same cupboard, now lit by warm light from the open door on the right. A boy of about ten with short dark brown hair, wearing a black jumper, dark jeans and dark trainers, walks slowly in from the right, seen from behind and slightly to the side. He steps carefully over the cables on the floor, stops an arm's length from the dusty robot and tilts his head, looking up at its bowed face. He brushes a little dust from the robot's arm with his fingertips, then asks quietly, with curiosity: "Who are you?" The robot does not move or answer. Dust hangs in the light between them. Camera: handheld, following just behind the boy's shoulder at his eye level, settling into a two-shot of the boy and the robot.
Audio: soft footsteps on a dusty floor, the boy's quiet voice saying "Who are you?", then silence and faint wind. Only the boy speaks. A single held string note underneath.
```

His question is answered in shot 6, when Pepper says "Hello, Boris. I've been waiting for you."

Alternative if the generator refuses a child on screen: keep the camera on the robot, show only the boy's shadow and his hand reaching into frame, and have the line spoken from off-screen.

### Shot 3 — The human touch (6 s)

Start frame: `s3-touch-start.jpg` · End frame: `s3-touch-end-eyes-lit.jpg`

```
Extreme close-up. A boy's hand rests gently on the robot's white shoulder; his fingers press slightly and his thumb moves. The robot is still and its eyes are dark. For two seconds nothing happens. Then a faint thread of blue light runs under the glossy shell from beneath the hand, up the neck to the head. One eye flickers blue, goes dark, then both eyes come on with a soft steady blue glow. The robot's head tilts up a few degrees. Camera: slow push-in with a slight drift right, focus pulling from the hand to the eyes. Warm amber background light.
Audio: a soft electronic heartbeat, two beats, then a rising tone as the eyes light. No speech.
```

### Shot 4 — The spark (6 s)

Start frame: `s4-spark-start.jpg` · End frame: `s4-spark-peak.jpg`

```
The boy's hand rests on the robot's chest beside its dim touchscreen. The screen flickers once, twice, then ignites: a burst of white-cyan light erupts from the screen, a ring of energy expands outward, and hundreds of bright sparks and thin streams of blue light spiral out and around the robot. The boy's hair and sleeve are blown back by the rush of air and his face is lit bright blue; he leans back slightly but keeps his hand in place. The robot's eyes blaze, its shoulders rise and its fingers spread open. Camera: fast push-in during the flicker, then a quick pull back as the burst expands, with lens flare.
Audio: rising electrical whine, a deep bass impact on the burst, crackling energy, strings surging. No speech.
```

### Shot 5 — Revived (6 s)

Start frame: `s5-awake-start.jpg`

```
The burst has settled into calm streams of cyan light and glowing particles drifting around the robot. The robot slowly lifts its head, blinks its glowing eyes once, flexes the fingers of both hands one after another, then turns its head and looks directly at the boy. The boy slowly lowers his hand and breathes out, amazed. The chest screen pulses gently. Camera: slow arc around the robot from the boy's shoulder towards the robot's front, about 45 degrees.
Audio: warm strings with soft synthesiser, a gentle ascending start-up chime, quiet servo hum as the head moves. No speech.
```

### Shot 6 — Rebirth (8 s)

Start frame: `s6-rebirth-start.jpg`

```
A modern technology laboratory lit in warm amber and cyan. The robot stands beside a boy, facing him, one hand raised. The robot turns its head towards the boy, waves its raised hand gently twice, and says in a warm, friendly, slightly synthetic voice with a British accent: "Hello, Boris. I've been waiting for you." The boy smiles widely and raises his own hand to wave back. The glowing network lights on the wall behind them pulse softly. Camera: slow pull-back and rise to a wide shot of the two together.
Audio: the robot's spoken line, clear and unhurried; warm piano and strings resolving in a major key underneath. Only the robot speaks.
```

Alternative if the generator refuses the frame: crop the start frame so only the boy's shoulder and the back of his head are in view.

### Title card (5 s)

Do not generate this. AI video renders text poorly. Reuse the title card from `../build_trailer.py`: **PEPPER REVIVAL** / *Forgotten technology. Reborn intelligence.* / THE AWAKENING — 2026.

## Getting good takes

- Generate each shot three or four times and keep the best; expect to discard most takes.
- Test at 720p, then re-run the winning prompt at full resolution.
- If the robot's shape drifts, shorten the clip to 4–5 s and remove one action from the prompt.
- Boris must look the same in shots 2B, 5 and 6. Use a tool mode that takes a reference image for 2B, and re-roll until his hair and clothes match the other shots.
- If the generated dialogue voice is wrong, mute it and use `../audio/pepper_voice.wav` instead.
- For a consistent score across all seven clips, mute the generated music and lay the soundtrack from `../build_trailer.py` over the cut.

## Assembly

Order: 1 → 2 → 2B → 3 → 4 → 5 → 6 → title, about 48 seconds. Use hard cuts except a half-second dissolve from 2 to 3 and a white flash from 4 to 5. Fade to black over the last second of shot 6 before the title.
