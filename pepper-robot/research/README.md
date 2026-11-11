# Pepper AI retrofit — research index
**Research date:** 11 November 2026. **Status:** Desk research, not yet tested on our Pepper.

## Executive conclusion
Multiple independent teams have demonstrated modern conversational AI on Pepper. The most substantial public reference is [Studerus Realtime AI Assistant](https://github.com/studerus/pepper-android-realtime-chat), targeting Pepper v1.8 / NAOqi 2.9.5. For NAOqi 2.5, [PepperChat](https://github.com/ilabsweden/pepperchat) and ROS-based approaches are more relevant. A [2024 hardware research paper](https://arxiv.org/abs/2409.01036) integrated external Jetson GPU and RealSense depth sensing through the NAOqi ROS driver. None of these establishes a publicly reproducible clean-room replacement for Pepper's full safety/motor firmware.

**Decision:** restore power and identify our firmware before choosing a software branch. Preserve NAOqi and build an external AI bridge first. Commercialise a cloud service only after reliability, licensing and customer-demand tests.

## Documents
- [Evidence catalogue](evidence-catalogue.md): projects, demonstrated functionality, compatibility and source/claimed evidence.
- [Compatibility, licences and architecture](technical-assessment.md): reuse approach, licensing cautions, firmware reality and security.
- [Verification backlog](validation-backlog.md): experiments, acceptance measures and decision gates.
- [Existing Pepper restoration notes](../README.md).
- [Public-friendly research webpage](https://alext-veu.github.io/the-machine/research/) (deployment must be confirmed independently).

## Evidence labels
- **A — documented implementation:** public code plus explicit setup/architecture, or peer-reviewed experimental methods. Not independently reproduced here.
- **B — research/commercial claim:** credible paper or manufacturer/supplier announcement, but source/replication may be restricted.
- **C — research lead:** linked project or claim with incomplete verification.

These confidence labels describe **the published evidence**, not successful execution on our robot.

## Important limitations
- Exact Pepper model, battery, operating system and passwords still unknown.
- Provider model names, project dependencies and download links change; pin versions when testing.
- Do not copy third-party firmware, media or source into this repo without a licence review.
- Biometric identification, autonomous motion and customer-facing claims require dedicated privacy and safety assessment.
