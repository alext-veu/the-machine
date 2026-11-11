# Pepper Robot Revival

Research and engineering workspace for restoring a **SoftBank Robotics / Aldebaran Pepper** after approximately two years without charging, and then connecting it to modern AI. Research snapshot: **11 November 2026**.

**Status:** Robot not yet powered on; hardware revision, battery condition, NAOqi release and administrative credentials unknown. Purchase listings are leads, not verified orders. This folder contains links and original notes, not copies of third-party proprietary firmware or videos.

## Start here

1. [Restoration and recovery runbook](docs/restoration-runbook.md) — purchase charger; safe battery test; boot; identify version; gain access before deciding to reset.
2. [Hardware and power research](docs/hardware-and-power.md) — specifications, revision differences, charger options, battery/repair leads, service interfaces and upgrades.
3. [Software and access recovery](docs/software-and-recovery.md) — NAOqi 2.5 / 2.9, SDKs, password and firmware caveats.
4. [AI architecture and roadmap](docs/ai-integration.md) — external control computer, network boundaries, speech, vision, motion safety and milestones.
5. [Demos and open-source references](references/projects-and-videos.md) — descriptions, working project links, documentation and demonstrations.
6. [Field checklist](checklists/first-power-on.md) — collect evidence during first inspection.

## Current decision

**Do not factory reset or flash firmware before identifying the installed version and preserving working software.** NAOqi 2.5 and 2.9 have incompatible application models. A NAOqi 2.5 factory reset may ask for a previously linked account; having an archived firmware image alone does not bypass a changed password.

**Safety:** Do not open, jump-start, modify or bypass protection on the approximately 795 Wh lithium-ion battery. Use the correct original-compatible power adapter with verified connector/polarity. Service-only interfaces and internal power modifications need qualified inspection.

## Suggested project phases

- P0: photograph identification labels, adapter port, tablet and rear head cover without disassembly.
- P1: purchase correct charger, inspect and power on safely.
- P2: discover IP/network, read NAOqi version and establish authorised access; back up applications/configuration.
- P3: test NAOqi text-to-speech and simple arm/head gesture from external PC.
- P4: prototype AI conversation with push-to-talk, opt-in vision and a whitelisted action bridge.
- P5: assess on-board auxiliary computer only after external proof of concept.

Repository root README describes a separate *Person of Interest*-inspired web experience; this subproject is physical robotics R&D and does not change that application.

## Owner discovery & community strategy

Our proposed next outreach initiative is the [**Pepper Revival Network**](strategy/owner-discovery-and-community.md): a useful public resource and voluntary community for finding legacy Pepper owners, particularly in Japan, with a Pepper compatibility checker, safe restoration guidance, opt-in registry, developer hub and eventual AI pilot applications. This is a **strategy, not a launched service or established customer market**.

## Latest family direction

**Hotel AI Concierge is the primary proof of concept; college reception is the backup.** Boris designs personas, visitor questions and tablet UX; Victor helps test and demonstrate; Alexander leads engineering. See [family R&D roadmap](planning/family-rd-roadmap.md), [commercial discovery hypotheses](planning/product-discovery.md), and [GitHub adoption review](research/github-adoption-review-2026-11.md). The [public upgrade research page](https://alext-veu.github.io/the-machine/research/upgrade-landscape/) makes the findings accessible without access to the private repository (public deployment status must be checked).

## Existing AI upgrade research — start here

Before designing new firmware or a commercial cloud platform, review our [**AI retrofit research catalogue**](research/README.md), containing:

- [Evidence catalogue: real projects, research papers and commercial Pepper+](research/evidence-catalogue.md)
- [Firmware/SDK compatibility, code reuse and licence assessment](research/technical-assessment.md)
- [Validation experiments and go/no-go gates](research/validation-backlog.md)

**Finding:** modern AI has already been connected to Pepper via NAOqi 2.5 / ROS and NAOqi 2.9 / QiSDK. Published Jetson/RealSense hardware upgrades also exist. Full independent replacement of the motion/safety firmware remains unverified. The installed OS on our own Pepper is still unknown.
