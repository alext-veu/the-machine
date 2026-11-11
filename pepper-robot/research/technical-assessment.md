# Technical assessment — reuse before reinvention
Research snapshot: 11 November 2026.

## Firmware versus applications
**Firmware** in this context covers Pepper's OS, controller firmware and safety-critical motor/power functions. **Applications** sit above those layers using NAOqi, QiSDK or ROS adapters. A Kotlin Android APK on NAOqi 2.9 is **not** a replacement for controller firmware. An external ROS computer likewise does not replace NAOqi.

| Route | Compatible target | What we can reuse | Principal blocker |
| --- | --- | --- | --- |
| Studerus realtime Android | Pepper 1.8 / NAOqi 2.9.5 | Kotlin app, provider adapters, QiSDK actions, tablet UI, tested patterns | Requires correct Android/QiSDK generation; firmware upgrade must not be presumed |
| PepperChat / direct NAOqi | likely NAOqi 2.5 legacy pathway (version check) | Dialogue sequencing, Pepper TTS and sensor API | Python 2-era runtime and audio latency |
| ROS 1 / naoqi_driver | legacy NAOqi installations with working bridge | topics, motion interface, external perception, local LLM | legacy ROS maintenance and network-security exposure |
| Jetson + RealSense | physical R&D retrofit | external compute, depth camera, perception methods | mounting, power, thermal and mobility safety |
| Pepper+ vendor | eligible devices **only after vendor confirmation** | potential supported hardware/software upgrades | parts, licences, access, geography, support and cost |
| Complete custom firmware | none verified | no safe reusable end-to-end replacement identified | proprietary control system, BMS, motion safety and product liability |

## Studerus specifics worth examining
- Android Studio project with **Pepper** and **standalone Android** flavours.
- Native streaming voice against OpenAI Realtime, Gemini Live and other providers.
- QiSDK movement/gestures, vision, local people tracking, navigation and tablet applications.
- Android 6/API 23 on its target Pepper; current Android libraries need compatibility checks.
- README warns development builds may embed API keys in the APK: **never do that commercially**. Proxy model access through a secure per-tenant backend and rotate credentials.
- On-device face recognition is technologically interesting but creates biometric processing obligations. **Exclude recognition of named individuals from MVP**.

## Security/product considerations
1. Legacy robotics services should live on isolated LAN/VLAN; no inbound port forwarding.
2. A secure outbound device tunnel, device identity, central credential rotation and signed config updates are better SaaS foundations than direct vendor SDK exposure.
3. Implement an allowlisted capability interface (speak, gesture, gaze; later mobility), with action budgets, local watchdog, physical emergency stop, audit and human override.
4. Measure audio response latency, transcription failure, disconnections, heat, battery runtime and lost-network behaviour on the real robot.
5. Use consent-based camera/microphone activation and avoid biometric identification by default.
6. No claims about uptime, autonomy, security certification or battery lifetime before testing.

## Build versus buy matrix
| Component | Prefer reuse | Build ourselves only where it differentiates |
| --- | --- | --- |
| Robot motion | NAOqi/QiSDK + ROS bridge | Safety action gateway and monitoring |
| Speech pipeline | Existing realtime SDK / provider | Tenant policy, latency budgets, fallback |
| Vision | Open-source libraries and model APIs | Privacy filtering, domain-specific workflow |
| Robot personality | Prompt/voice settings | Versioned persona packs and testing |
| Retail/visitor answers | Retrieval + product catalogue APIs | Business connectors, measurable outcomes |
| Fleet management | General SaaS/observability primitives | Device provisioning, permissions, OTA application delivery |
| Firmware | Supported vendor paths | Only after legal review and substantial engineering justification |

## Commercial differentiation hypothesis
Our prospective advantage would be *supported legacy Pepper retrofit + enterprise knowledge integrations + privacy controls + model choice + fleet management*, not simply another ChatGPT demo. SoftBank Pepper+ means differentiation needs interviews and feature-level benchmarking.

## Reference links
- [Studerus code & setup](https://github.com/studerus/pepper-android-realtime-chat)
- [HRI 2026 paper](https://doi.org/10.1145/3757279.3788808)
- [PepperChat](https://github.com/ilabsweden/pepperchat)
- [ROS driver](https://github.com/ros-naoqi/naoqi_driver)
- [Jetson/RealSense paper](https://arxiv.org/abs/2409.01036)
- [SoftBank Pepper+](https://www.softbankrobotics.com/jp/news/press/20260202a/)
