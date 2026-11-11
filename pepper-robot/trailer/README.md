# Pepper Revival trailer

Cinematic teasers for the Pepper Revival project, kept beside the [research](../research/) folder.

## The Awakening (2026)

**File:** [the-awakening/pepper-revival-the-awakening.mp4](the-awakening/pepper-revival-the-awakening.mp4)

A 29-second 16:9 teaser: forgotten Pepper in a dark cupboard, a boy’s first touch, a stuttering AI spark, then Pepper awake in a modern lab saying “Hello, Boris. I've been waiting for you.”

| | |
| --- | --- |
| Title | Pepper Revival: The Awakening |
| Runtime | 29 s (delivered file; 29.000 s) |
| Picture | 1920×1080, 24 fps, H.264 (yuv420p), ~10.1 Mbps |
| Sound | AAC 192 kb/s, 48 kHz, stereo; original score plus a synthesised British voice line |
| Version | Final cut, version 3 (11 November 2026, Europe/London) |
| Contact sheet | [the-awakening/contact-sheet.png](the-awakening/contact-sheet.png) |

### Shot list

Times are from the v3 assembly timeline. The muxed file is 29.000 s.

| Time | Shot |
| --- | --- |
| 0.000–3.750 | **Forgotten.** Slow push in to dusty, powered-off Pepper in a dark store-room / cupboard, cold moonlight, head lowered, tablet black. |
| 3.750–7.583 | **The human touch.** Warm door light; a young boy places his hand on Pepper’s shoulder. |
| 7.583–13.645 | **The spark.** Pause, faint seam pulse, stuttering eye flicker, black gaps, tablet glitching awake. Heartbeat and crackles on the soundtrack. |
| 13.645–17.145 | **Surge.** Impact flash, eyes and seams come on, cyan light from the chest, startup chime. |
| 17.108–19.408 | **Head lift.** Pepper raises his head and looks toward the boy. |
| 19.408–21.258 | **Rebirth, Pepper MCU.** Pepper greets the boy. Voice (and subtitle): “Hello, Boris. I've been waiting for you.” (voice from 19.958 s). |
| 21.258–22.191 | **Boy close-up.** The boy smiles. |
| 22.191–25.208 | **Wide pull-back.** The two together in a warm modern lab; fade to black from 24.608 s. |
| 25.208–29.000 | **Title card.** PEPPER REVIVAL — Forgotten technology. Reborn intelligence. — THE AWAKENING — 2026. |

### Original brief (summary)

AT’s full prompt is in [the-awakening/prompts/original-brief.md](the-awakening/prompts/original-brief.md). In short: a photorealistic 16:9 science-fiction teaser of the original SoftBank Pepper, moving from abandonment to a boy’s discovery, the first spark of modern AI, and Pepper’s rebirth. Colour should travel from cold desaturated moonlight to electric cyan and warm amber. Mechanics should stay believable — no morphing into a different robot, no cartoon rendering. The film should make Boris want to bring Pepper back to life. A later film, **The Evolution**, is planned to show what they could build together (hotel AI concierge). During production AT also asked for an original soundtrack and a more dramatic spark: flicker, then awakening.

### How it was made

- **Picture.** AI-generated video from keyframes. Stills (1280×720) were generated with `GenerateImage` using Wikimedia Commons photographs of SoftBank Pepper as likeness references, then animated with `GenerateVideo` (image-to-video). Shots were graded, trimmed and cut together in ffmpeg. The spark is a montage of close-ups with inserted flashes, not one continuous take. The title card is typography, not generated text. Confirmed parameters, source stills and trim points are in [the-awakening/prompts/generation-prompts.md](the-awakening/prompts/generation-prompts.md). The exact generator prompt strings were not saved with the assets.
- **Score.** An original synthesised soundtrack (piano, orchestral strings, restrained electronics), mixed for the v3 cut: [the-awakening/audio/mix-v3.flac](the-awakening/audio/mix-v3.flac).
- **Voice.** Microsoft `edge-tts` voice **en-GB-RyanNeural**, lightly processed (no ring modulation; short chorus and reverb): [the-awakening/audio/pepper_line_v3_ryan_light.flac](the-awakening/audio/pepper_line_v3_ryan_light.flac).

The keyframes actually used in v3 are in [the-awakening/keyframes/](the-awakening/keyframes/). Rejected candidates and v1/v2 cuts are not in this folder.

### Known remaining flaws

Version 3 is the agreed final cut, with these issues left in:

- The boy’s hand blends into Pepper’s shoulder around 14–17 s (during the surge / late spark).
- The surge lighting on Pepper’s seams and the starburst on the tablet can look flat, as if laid on top of the footage rather than emitted from inside the robot.
- The boy’s face drifts a little across the last three shots.
- The opening reads more like a store-room than a tight cupboard, and the boy is about the same height as Pepper rather than a little taller.

### Advertising disclosure

The boy is a **fictional AI-generated character**, not a real child and not a likeness of Boris. If this film is used in advertising, UK ASA/CAP rules require a clear disclosure that people in the ad were AI-generated.

Pepper’s appearance is an artistic depiction of the SoftBank / Aldebaran Pepper robot, guided by the credited reference photographs. SoftBank, Aldebaran and Pepper are trademarks of their respective owners. This teaser is a project film, not an official SoftBank production.

### Reference attributions

Eight photographs from Wikimedia Commons were used only as likeness references when generating keyframes. Several are **CC BY-SA** and require attribution; keep [the-awakening/references/sources.txt](the-awakening/references/sources.txt) with the files.

| File | Author | Licence |
| --- | --- | --- |
| `01-front-studio-pepper-the-robot.jpg` | Softbank Robotics Europe (photograph: Philippe Dureuil / TOMA, 15 February 2016) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `02-face-closeup-innorobo-2015.JPG` | Xavier Caré / Wikimedia Commons, Innorobo Lyon, 2 July 2015 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `03-fullbody-innorobo-2015.JPG` | Xavier Caré / Wikimedia Commons, Innorobo Lyon, 2 July 2015 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `04-threequarter-softbank-pepper.JPG` | Tokumeigakarinoaoshima, 18 July 2014 | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |
| `05-off-screen-pepper-robot-off.jpg` | Hanonimas, Futako-Tamagawa Rise showroom, 7 November 2015 | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
| `06-threequarter-alex-knight-unsplash.jpg` | Alex Knight (agkdesign), Unsplash photo 2EJCSULRwC8 (published before 5 June 2017) | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |
| `07-chest-tablet-pepper-a-humanoid-robot.jpg` | Kukarobot, 9 September 2019 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| `08-fullbody-peper-school.jpg` | Nebojsa.pavic, 16 January 2023 | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |

The eye rings in photograph 07 are purple in the source; that colour was not copied into the film.

### Follow-up film — The Evolution

Placeholder. A second film, **The Evolution**, is planned: Pepper receives modern computing, vision and new personalities, and becomes the hotel AI concierge imagined in the family roadmap. It should reuse this Pepper, this boy and this look so the two films match. Brief and media will go here (or in a sibling `the-evolution/` folder) when work starts.

See also the [family R&D roadmap](../planning/family-rd-roadmap.md) and [AI retrofit research](../research/README.md).
