# Verification backlog and decision gates
Research snapshot: 11 November 2026. **No experiment below has yet been run.** Recording measured evidence is more valuable than guessing.

| Priority | Test | Acceptance evidence | Decision informed |
| --- | --- | --- | --- |
| P0 | Charger, battery and safe boot | photo of charger label/connector; charge LEDs; boot log | Is robot serviceable? |
| P0 | Hardware + software inventory | precise hardware revision, NAOqi, tablet/Android version, device status | Which SDK and retrofit route? |
| P0 | Authorised access + backup | IP, successful authorised SDK/API operation, exported config/app list | Can we preserve before reset? |
| P1 | Speech 'I'm back' | recorded audio output and API log | Baseline control |
| P1 | Read-only camera/sensors | frame resolution, FPS, latency, permissions | Existing vision sufficient? |
| P1 | Studerus standalone Android build | reproducible signed APK, no secrets in binary | Android code maturity without Pepper |
| P1 | PepperChat or ROS bridge on external PC | reproducible container environment and robot action | 2.5 path feasible? |
| P1 | Conversational AI benchmark | median/p95 speech-end to response onset, interruptions, WER, cost/10 minutes | Provider & UX decision |
| P1 | Safety fault injection | network loss, stopped client, emergency stop, unknown tool request | Is action gateway safe? |
| P2 | Knowledge-based retail/reception demo | 30 representative Q&A prompts, factual accuracy, handoff and citations | Real customer utility |
| P2 | Vision + conversation | consented object test, false recognitions and response latency | Multimodal reliability |
| P2 | Navigation (supervised only) | map, obstacle encounter logs, emergency stop response | Whether mobility belongs in v1 |
| P2 | Vendor compatibility enquiry | written SoftBank/IRIS eligibility, licence and costs | Supported firmware option |
| P2 | Commercial licensing review | third-party SPDX inventory, distribution and data-processing obligations | Can we productise? |
| P3 | 5-10 operator/customer interviews | documented pains, budget, procurement, willingness to pilot | Demand |
| P3 | Paid pilot (if safe) | SLA targets, uptime, revenue/cost data and incident record | Go/no-go SaaS |

## Initial experiment order
1. Power on, inventory and back up — no firmware flash.
2. Choose **NAOqi 2.5** vs **2.9.5** branch based on actual version.
3. Reproduce a published baseline (PepperChat or Studerus) without new architecture.
4. Compare against our own small model gateway, measure cost and latency.
5. Build one high-value scenario: e.g. reception Q&A with document retrieval.
6. Only then prototype modular upgrades, fleet management or cloud subscriptions.

## Evidence template
- Date and test operator:
- Robot revision/serial (private; do not publish serial):
- NAOqi release and tablet OS:
- Source commit/tag and licence:
- Test setup, versions and network:
- Input dataset / sample size:
- Observed outcome and raw logs:
- Latency (median, p95), reliability and cost:
- Safety and privacy observation:
- Reproducibility / blockers:
- Go/no-go and next test:

## Open questions for next brainstorming
- Is our robot v1.6 or v1.8, running NAOqi 2.5 or 2.9?
- Does the battery permit a safe startup, and are original cameras/mics acceptable?
- Is the current 2026 Android reference implementation maintainable across customer devices?
- What exact Pepper+ upgrade costs and licences apply to legacy units?
- Can we achieve natural full-duplex conversation with stable interruptions on a noisy shop floor?
- What high-value task can be completed reliably, not merely demonstrated?
- How do we serve legacy versions without distributing proprietary OS/controller images?
- Do we want a retrofittable edge kit or an externally connected gateway first?
