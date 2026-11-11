# Pepper Reborn — potential commercialisation (hypotheses, not a product claim)
**Initial family mission:** hotel AI concierge, followed by college reception. **Commercial concept:** legacy Pepper retrofit with secure gateway and configurable AI skills. Preserve ability to support other robots through adapters.

## Target customer jobs
1. **Hotel reception:** answer common questions reliably, display visual directions and hand off to staff. Avoid integrating real booking or identity data until access/privacy controls are reviewed.
2. **College reception:** site/department information, event and visitor enquiries; safeguarding/privacy requirements are stricter.
3. **Retail:** product knowledge and availability linked to approved catalogue APIs; needs measurable enquiry resolution and staff handoff.
4. **Museums/events:** interactive education, multilingual explanations, predictable scripted motion.

## Reuse-versus-build principle
Use existing NAOqi/QiSDK code paths, ROS bridges and demonstrated streaming AI. Build our differentiated components: cross-firmware connector abstraction, local safety-policy gateway, secure tenancy, business-system connectors, knowledge grounding, fleet diagnostics and usage metering.

## Candidate MVP features
- Approved knowledge only, source trace and refusal/escalation on unknown answers.
- Conversation interruptibility and predictable speaker/listener transitions.
- Tablet information panel and human-call action.
- Basic opt-in perception; no facial identity recognition.
- Remote health checks and secure configuration.
- Switchable personas independent of hardware drivers.

## Commercial hypotheses to validate
- A legacy Pepper owner will pay for restoration plus AI software rather than procure new hardware.
- A hospitality operator values fewer routine interruptions, better multilingual coverage or guest engagement enough to purchase a paid pilot.
- The platform can operate at sustainable variable model and support costs in noisy, public areas.
- A viable installed fleet remains accessible with documented hardware/OS versions.
- SoftBank Pepper+ and integrators leave a meaningful niche for vendor-independent legacy deployments.

## Discovery interviews: ask before pricing
How many robots are deployed? Which firmware version? What happens when something fails? What is the single repetitive task worth automating? How is ROI measured? Who approves security/privacy? What support is expected? Would they fund a 6-week paid pilot? What price and risk ceiling is acceptable?

## Stage gates
- **R&D:** 30 fictional hotel questions with >=90% grounded success, zero invented hotel policies in controlled tests.
- **Pilot:** measurable production-like demand, consent and data-handling plan, safety review, incident escalation and audited costs.
- **Commercial:** supported update/recovery path, licensing audit, contractual support process, maintenance strategy, telemetry and device security.
 
## Risks
Unknown condition/firmware of our robot, proprietary SDK rights, unsupported legacy systems, unknown battery health, network security, privacy/biometric law, customer support load, prospective Pepper+ competition and limited reachable installed base.

## What is NOT decided
Pricing tiers, churn, installed-base size, firmware replacement, capital needs, supported robot models beyond Pepper, or final cloud vendor.
