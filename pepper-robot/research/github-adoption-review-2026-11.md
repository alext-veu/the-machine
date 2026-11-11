# GitHub adoption review — Pepper AI retrofit
**Reviewed:** 11 November 2026. Public repository metadata/README inspections; **no code executed or security audit performed**.

## Evidence-based selection

| Repository | Observed state | Licence reported by GitHub | Adopt / learn | Risk / validation |
|---|---|---|---|---|
| [studerus/pepper-android-realtime-chat](https://github.com/studerus/pepper-android-realtime-chat) | Active (last push 2026-11-04); 21 stars at review; targets NAOqi 2.9.5 / QiSDK | NOASSERTION (read actual licence file) | **Study first for 2.9**: streaming voice, provider adapters, tablet, gestures, agent tool-calling | Determine licence rights and Android/API compatibility; ensure model keys aren't embedded in shipped APK |
| [ilabsweden/pepperchat](https://github.com/ilabsweden/pepperchat) | Last push 2026-04-29; 47 stars; 8 reported open issues | MIT | **Prototype on NAOqi 2.5** for speech and GPT bridge | Legacy runtime, dependency pinning, latency measurements; review open issues |
| [rosielab/Pepper-GPT](https://github.com/rosielab/Pepper-GPT) | Last push 2024-02-08; 0 stars | Not established in metadata | **Reference only** for ROS + Ollama / self-hosted LLM | Licence and maintenance unclear; not proof of production speech |
| [Crostino14/Cognitive-Robotics-Project](https://github.com/Crostino14/Cognitive-Robotics-Project) | Last push 2026-05-21; 0 stars | GPL-3.0 | **Study** hotel/retail-style skills, Whisper, GPT-4o, ROS perception | GPL obligations; service reliability and sensor behaviour unverified |
| [VediYD/pepper-bot](https://github.com/VediYD/pepper-bot) | Last push 2024-07-01; 0 stars | MIT | **Study** university FAQ/knowledge approach | Legacy Python stack; limited maintenance evidence |
| [ros-naoqi/naoqi_driver](https://github.com/ros-naoqi/naoqi_driver) | Last push 2024-09-17; 63 stars; 41 reported open issues | Apache-2.0 | **Potential infrastructure** for older ROS workflows | ROS 1 dependency and open issues; consider ROS 2 successor |
| [RGU-Computing/pepper](https://github.com/RGU-Computing/pepper) | Last push 2025-03-21; 4 stars | Not established | **Reference** for setup lessons | Check licence and reproducibility |
| [LAIRLabUnivpm/LAIR-GPT](https://github.com/LAIRLabUnivpm/LAIR-GPT) | Last push 2024-07-29; 2 stars | Not established | **Study** MQTT bridge: Python audio/transcript/GPT, Choregraphe receiver | Interesting separation of processes; avoid copying code until licence clarified |
| [L-Hadil/PepperRobot_AI_assistant](https://github.com/L-Hadil/PepperRobot_AI_assistant) | Last push 2025-05-25; 1 star | MIT | **Study** Kotlin/NAOqi 2.9 child-friendly interactions and tablet flows | Preschool use case differs from hotel; inspect API/privacy handling |
| [z5210274/COMP3431_Pepper_Visual-SLAM_ROS2](https://github.com/z5210274/COMP3431_Pepper_Visual-SLAM_ROS2) | Last push 2025-11-28; 1 star | Not established | **Research path** for ROS 2 Humble + RTAB-MAP with NAOqi 2.5 | Student project; version/camera support and real-world navigation must be independently tested |

**Stars, activity and issue counts are indicators, not evidence of working or secure code.** Dates reflect GitHub's pushed_at metadata, not verified release dates. Licence metadata does not replace checking repository LICENCE files, bundled dependencies and SDK redistribution conditions.

## Specific adoption decisions

### Reuse or adapt once robot version known
- **If 2.9.5:** reproduce Studerus standalone Android configuration, then test on Pepper; study Kotlin/QiSDK application architecture, tool calling and low-latency voice. Do not include live model credentials in the app.
- **If 2.5:** reproduce PepperChat speech baseline; evaluate ROS bridge only when necessary for sensing/action interfaces; use an isolated subnet and sandboxed legacy Python.
- **For navigation:** investigate ROS 2 / RTAB-MAP research only after original obstacle detection, brakes, localisation and supervised motion have passed testing.
- **For multi-persona:** use configuration/prompt/voice packs and deterministic action templates rather than forking critical firmware.
- **For cloud:** build tenant identity, secure outbound edge tunnel, knowledge retrieval and policy enforcement ourselves; reusable AI SDK components can sit behind adapters.

### Not adopting in first prototype
- Whole-board firmware replacement or custom BMS controls.
- Unsupervised autonomous navigation.
- Face identification or emotion inference as a customer feature.
- A subscription billing system before a hotel concierge demonstration works.

## Immediate technical due diligence
1. Confirm actual NAOqi revision and backup access.
2. Inspect licences in candidate repositories and dependencies.
3. Pin exact commit hashes and build environments; record reproducible install scripts.
4. Verify realtime voice with interruptions in a realistic noisy setting.
5. Test strict tool-call allowlisting, network isolation and failure handling.
6. Confirm use of Pepper microphones and cameras doesn't require undisclosed vendor cloud services.
7. Compare original SDK capability with external sensors; avoid hardware surgery unless benchmarks justify it.

Related catalogue: [evidence-catalogue.md](evidence-catalogue.md). Validation tests: [validation-backlog.md](validation-backlog.md).
