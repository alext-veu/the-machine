# Evidence catalogue — actual Pepper AI and hardware upgrades
Research snapshot: **11 November 2026**. Publisher claims are distinguished from our untested assumptions.

| ID | Project / evidence | What it implements or reports | Platform and prerequisites | Evidence | Current assessment |
| --- | --- | --- | --- | --- | --- |
| P01 | [Studerus Pepper Realtime AI Assistant](https://github.com/studerus/pepper-android-realtime-chat) · [HRI 2026 DOI](https://doi.org/10.1145/3757279.3788808) | End-to-end realtime speech, multiple providers, vision, gestures, navigation/mapping, tablet games, perception and tool calls | Pepper 1.8, **NAOqi 2.9.5**, Android 6/API 23, QiSDK, Kotlin; standalone Android testing flavour | **A** — extensive code and instructions; conference paper and demo linked | Top reference for Android-based Pepper; **not a plug-in for 2.5**. Audit security and test each claimed feature |
| P02 | [ilabsweden/pepperchat](https://github.com/ilabsweden/pepperchat) · [HRI 2023 DOI](https://doi.org/10.1145/3568294.3580040) | Robot speech/dialogue linked to GPT, for Pepper and NAO | Older NAOqi/Python development; verify precise versions | **A** — repository, MIT licence and publication | Good 2.5 dialogue baseline; verify latency, audio chain and current API compatibility |
| P03 | [rosielab/Pepper-GPT](https://github.com/rosielab/Pepper-GPT) | Text-client conversation via ROS naoqi_driver and local Mistral/Ollama | Docker Compose, ROS, naoqi_driver, external host | **A** — instructions and source | Best local-model architecture reference; **text client is not proof of native full-duplex voice** |
| P04 | [Crostino14/Cognitive-Robotics-Project](https://github.com/Crostino14/Cognitive-Robotics-Project) | Shopping-mall assistant, Pepper video/face detection, Azure Whisper, GPT-4o, animated speech | ROS 1/Noetic, NAOqi and Azure/OpenAI integrations | **A** — modular source/report/demo references; GPL-3.0 | Useful retail pipeline and integration reference; licence review mandatory |
| P05 | [VediYD/pepper-bot](https://github.com/VediYD/pepper-bot) | University information assistant, local GPT service, Python 2.7/Jupyter control and robot telemetry | Legacy Python/NAOqi, external host | **A/C** — code and setup notes, no independent test | Educational/campus use-case reference; inspect maintenance and redistribution terms |
| P06 | [Magri et al. 2024 hardware enhancement](https://arxiv.org/abs/2409.01036) | Jetson GPU and RealSense D435i for human detection, localisation, pose/gaze; ROS integration | Extra compute/camera/mounts, ROS NAOqi driver | **B** — research paper describes actual prototype | Hardware proof of concept, not general purpose drop-in kit |
| P07 | [Published public-event ChatGPT Pepper study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137922/) | Choregraphe + external back end + ChatGPT dialogue at a public event, 4–5 s average response under study conditions | Older NAOqi/Choregraphe | **B** — peer-reviewed field study | Gives real latency benchmark; modern streaming approaches should be benchmarked rather than assumed faster |
| P08 | [SoftBank Pepper+ announcement, 2 February 2026](https://www.softbankrobotics.com/jp/news/press/20260202a/) | Commercial Pepper+ offer with latest AI and video analytics | Manufacturer-controlled product; migration eligibility unknown | **B** — primary manufacturer announcement | Real competitor. **Not proof our unit supports a user-installed upgrade** |
| P09 | [IRIS Robotics Pepper service/upgrade](https://irisrobotics.eu/en/pepper-plus) | Commercial Pepper+ upgrade/service offering, including replacement tablet and AI functions as advertised | Service-dependent, kit and pricing to confirm | **C** — vendor marketing | Contact vendor for written compatibility, costs and firmware rights |
| P10 | [ros-naoqi/naoqi_driver](https://github.com/ros-naoqi/naoqi_driver) | ROS bridge to NAOqi | ROS 1 legacy ecosystem, exact supported distro/build check | **A** — source | Interface building block, **not** a replacement OS |
 
## What is genuinely demonstrated versus still unproven
**Demonstrated in published examples:** cloud GPT/LLM conversations; streamed realtime AI on supported Android Pepper; command/action integration; tablet UI; camera-assisted people detection; ROS/NAOqi control; external GPU and depth camera augmentation.

**Not yet verified for our hardware:** our Pepper's boot status, NAOqi release, admin recovery path, camera stream quality, native navigation robustness, any specific USB/service-port pinout, reliable unattended deployment, commercial fleet management, subscription retention, and a safe independent firmware image.

## Source and licence cautions
Do not infer commercial reuse rights from a public GitHub page. P01 and P02 explicitly describe **MIT** licences; P04 is **GPL-3.0**, with source-distribution implications for derivative software. Check the licence of *every component*, including third-party AI SDKs, robot SDKs, Choregraphe assets and datasets. For P03, P05, P06 and P10, perform a repository-file licence audit before incorporating code.

## Supplementary video links
- [Pepper World 2016](https://www.youtube.com/watch?v=eJkfZR8mhBA) — historic business demonstration.
- [Pepper at trade show](https://www.youtube.com/watch?v=6qbULogPdnI) — speech and gestures.
- Studerus README contains its own contemporary AI demo link; verify direct video URL and availability.
- [Japan Times retail experiment](https://www.japantimes.co.jp/multimedia/2016/03/26/news/video-pepper-packed-mobile-shop-the-cellphone-store-ran-by-only-robots/).
