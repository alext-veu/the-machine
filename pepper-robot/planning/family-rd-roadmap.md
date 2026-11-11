# Pepper Reborn — family R&D proof of concept
**Direction agreed:** Hotel-reception demonstration first; college-reception backup. Boris designs experiences and test questions; Victor helps engineering tests and demonstrations; Alexander owns hardware/networking/cloud architecture. **No operating Pepper yet**; timings are contingent on recovery.

## Outcome
A visitor approaches Pepper. Pepper notices someone (without identifying their face), welcomes them, answers a factual question from a fictional hotel's approved knowledge base, displays useful information and offers staff escalation when uncertain. No real guest or booking system access in the first demo.

## Architecture (first iteration)
Pepper sensors, speaker, tablet and motion controllers <-> NAOqi 2.5 SDK bridge **or** NAOqi 2.9 QiSDK agent <-> secure local gateway <-> configurable cloud AI, speech, knowledge retrieval, operator dashboard.

First use a laptop on an isolated LAN. Later trial a low-power edge mini PC and onboard mounting. Native motion, emergency-stop and collision safeguards remain authoritative. The LLM requests **allowlisted skills**; it never sends unfiltered motor commands.

## Milestones and gates
| Phase | Indicative timeframe | Deliverable | Evidence to pass |
|---|---|---|---|
| M0: Restore | Weeks 1–2 | Charger, battery assessment, boot, NAOqi version, authorised access | Photos of connection, diagnostics, SDK compatibility, backup where possible |
| M1: Control | Weeks 2–3 | TTS, head and safe gesture, tablet status | Repeat 5 supervised actions reliably |
| M2: Voice | Weeks 3–5 | Realtime AI chat, interruption support | 5-minute demo; logged median/p95 latency and failure cases |
| M3: Senses/personas | Weeks 5–7 | Object descriptions, visitor detection, persona switching | 10 controlled objects, false-positive tracking and three persona tests |
| M4: Hotel | Weeks 7–9 | Fictional hotel FAQ, opening hours, directions, staff handoff | At least 27/30 scripted questions accurate with zero fabricated hotel facts |
| M5: Platform foundation | Weeks 9–12 | Provisioning, read-only telemetry, signed configuration, offline behaviour; college FAQ profile | Repeat after reboot and network outage; preserve safety |

These are **targets**, not guarantees. Battery, firmware lockout or incomplete project dependencies may change schedule.

## Roles
- **Boris — experience lead:** 30 visitor questions, storyboards, greeting scripts, persona design, test scorecards and discovery journal.
- **Victor — test lead:** hardware photographs, recording demos (with consent), latency tests, navigation observation and reliability reports.
- **Alexander — technical lead:** power safety, networking, OS/SDK discovery, cloud architecture, service controls and procurement.
- **AI tools:** coding assistance and documentation; review generated code and its safety before connecting motors.

## Demonstration scenarios
- Welcome and hotel FAQ: breakfast finish time, pool availability, directions and local amenities; all from synthetic knowledge.
- Multilingual mode: greeting in two selected languages and correct fallback for unsupported requests.
- Tablet: show answers, map and a 'contact reception' option.
- Vision: identify a selected object or detect presence without storing named faces.
- Personality modes: Friendly Concierge, Curious Explorer and sci-fi-inspired Collective; each changes voice/wording/tablet appearance, **not** safety constraints.
- College-reception backup: campus FAQ from a separate fictional dataset, demonstrating reusable skills.

## Minimum documentation for commercial reuse
Versioned edge/robot connector; licence inventory; deployment instructions; anonymised test results; device registration and revocation; telemetry with privacy controls; operating cost per conversation; fault recovery; evidence that the demo genuinely works without hidden manual intervention.

## Budget — indicative only
Charger £120–£200; battery repair reserve £300–£1,000; reuse developer PC £0; optional edge compute/storage £150–£400; optional sensors £100–£300; three months cloud/test services £50–£250. **Potential total £720–£2,150**, excludes engineering labour, specialist repair and unforeseen shipping/parts. Verify prices before purchase.

## Go/no-go
**Do not commercialise on demonstration appeal alone.** Required first: repeatable hotel task success, safe failure handling, acceptable latency/uptime in realistic acoustics, IP rights cleared and a paid-pilot interview pipeline.
