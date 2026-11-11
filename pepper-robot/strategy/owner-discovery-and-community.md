# Pepper Revival Network — Owner Discovery & Community Strategy

**Status:** Proposed strategy; not yet launched or market-validated.
**Date:** 11 November 2026  
**Parent project:** [Pepper Robot Revival](../README.md)  
**Related:** [Family R&D roadmap](../planning/family-rd-roadmap.md) · [Commercial discovery](../planning/product-discovery.md) · [GitHub adoption review](../research/github-adoption-review-2026-11.md)

## Executive decision

Build a **Pepper Revival Network** to find and help owners of legacy SoftBank/Aldebaran Pepper robots. Lead with useful technical assistance and openly documented restoration/AI demonstrations; invite owners to register voluntarily; learn which robots remain operational and which business problems owners want solved. Only then offer early-access pilots and potential paid AI upgrades.

**First technical proof of concept:** Hotel AI Concierge, with college reception as backup. **First owner outreach geography:** UK and European contacts for accessible interviews, while developing a Japanese-language experience because Japan historically had the largest Pepper market. The order and commercial priorities remain hypotheses until tested.

**Positioning concept:** “Give your Pepper a second life.” Not affiliated with or endorsed by SoftBank Robotics. Avoid confusing the community with official firmware support.

## Why this could work

Pepper owners face practical issues: missing chargers, aged batteries, discontinued or changing vendor/cloud services, legacy NAOqi versions, application compatibility and limited modern AI capabilities. Useful public guidance creates a reason to discover and trust the project **before** we ask owners to buy anything.

The old global sales/manufacturing figures do not prove an active addressable market. UK installed-base estimates and remaining operational fleet are unverified. We will measure opt-in verified ownership and upgrade readiness rather than claim a known TAM.

## Proposed web platform

| Module | Free utility / proposed scope | Later commercial path | Data considerations |
| --- | --- | --- | --- |
| **Pepper Doctor** | Model/firmware compatibility wizard; charger, battery and safe boot guide; symptom-based checklist | Optional paid service referral / remote diagnostic agent with explicit permission | Do not collect passwords or upload serials by default |
| **Owner Registry** | Opt-in country, approximate region, hardware/NAOqi release, operating status, preferred contact | Invite qualified pilots; track reachable compatible devices | Consent, deletion/export, no exact public location |
| **Pepper World Map** | Aggregate **consented** country-level or coarse regional counts and optional robot stories | Community discovery and partnerships | Never publish street address, serial, identifiable photos without separate consent |
| **Developer Hub** | GitHub catalogue, SDK compatibility matrix, technical articles, vetted videos, repair links | Developer ecosystem, connector SDK, support | Cite authors, respect third-party licences and branding |
| **Skills Gallery** | Honest demonstration pages: hotel, retail, education, museum, hospitality | Managed industry skills and subscriptions after validation | Label planned vs working vs independently tested |
| **Early Access** | A waitlist for authorised Pepper owners willing to pilot AI upgrades | Paid trials and upgrade kits | Minimal contact fields; transparent purpose and contact cadence |

The existing [Pepper research site](https://alext-veu.github.io/the-machine/research/) can seed the Developer Hub. It should link to source documents without exposing the private repository, and public publishing must be verified before promotion.

## Initial release — 4–6 week planning hypothesis

**MVP (no hardware connection or payments):**
1. Bilingual English/Japanese landing pages with clear provenance and disclosure.
2. Public Pepper research catalogue and restoration guide with source dates.
3. Compatibility checker: revision, NAOqi family, battery state, known blockers; output a *provisional* readiness report, not a diagnosis.
4. Voluntary owner registration and explicit communication opt-in.
5. Early-access application for owners with recoverable robots.
6. Restricted admin view with basic analytics and deletion/export process.

**Suggested implementation:** Next.js frontend; Supabase Postgres/Auth with row-level security; server-side validation/rate limits; email through a transactional provider. Keep analytics privacy-conscious. Separate visitor content from private registry records. Avoid publishing API keys in static GitHub Pages. Public GitHub Pages remains an educational front door; any registration forms should use a securely hosted backend with suitable privacy notices.

**Not in MVP:** robot remote access, autonomous firmware installs, payment processing, public owner email lists, precise map pins, facial identification, or unverified AI upgrade claims.

## Owner acquisition channels

### Japan
- Japanese-language technical SEO pages for Pepper charger, NAOqi version, battery, SDK and AI upgrade questions.
- Partner outreach to universities, research groups, former service partners and organisations with *publicly documented* Pepper deployments.
- Relevant Japanese robotics communities, X and video channels with genuine technical contributions.
- Find Japanese-speaking advisors/reviewers before publishing support guidance; translation-only localisation is insufficient.

### UK and Europe
- University robotics labs and public deployment case studies.
- Robotics integrators/refurbishers and training providers.
- Technical GitHub community contributions and restoration walkthrough videos.
- Respectful one-to-one outreach, not bulk unsolicited scraping.

### Content flywheel
- Public recovery journal with real results, clear dates and failures.
- “Can my Pepper run modern AI?” compatibility guide.
- Reproducible SDK comparisons across NAOqi 2.5 and 2.9.
- Before/after hotel concierge demo with measurable response latency and correct answers.
- Lessons on obsolete battery charging and safe repair referral, not DIY bypass instructions.

## Funnel and measurement

Visitor discovers help → completes optional checker → receives useful result without registering → optionally joins registry → selects consented early-access contact → technical suitability interview → pilot → subscription *if proven*.

### First 90 days: experimental targets, not forecasts

| Metric | Initial target | Caveat |
| --- | ---: | --- |
| Site visitors | 2,000 | Requires real distribution; not an organic forecast |
| Completed compatibility checks | 200 | No email gate |
| Voluntary owner registrations | 50 | Confirm duplicate/self-reported units |
| Reported functioning robots | 20 | Self-reported until verified |
| Owner pilot conversations | 10 | Outreach only where consented / appropriate |
| Candidate pilot organisations | 3–5 | Demand not established |

Track source channel, landing-page language, checker completion, voluntary sign-up rate, confirmed hardware revisions and *qualitative reasons* for upgrading or not upgrading. Do not extrapolate global market size from convenience samples.

## Customer and partner research

First interviews:
- Which country and organisation owns the robot? Is ownership/authority clear?
- Hardware revision, NAOqi version, charging/battery state, number of devices?
- What is the robot currently used for? What breaks or prevents use?
- Which single task would make it worthwhile to restore?
- Is there a funded pilot budget? Who approves security, privacy and procurement?
- Does it need voice, tablet, vision, navigation, CRM/POS connection, languages or handoff?
- What uptime, support, data residency and upgrade risks are acceptable?
- Would an external edge module be allowed, or is a supported official software-only approach required?

Potential partners: Pepper technicians, battery refurbishment specialists, SDK developers, Japanese robotics researchers, hospitality technology integrators. Record verified interest rather than treating public case studies as customers.

## Competitive and technical reality

Official Pepper+ modernisation exists; do not assume we have an exclusive AI retrofit opportunity. The [open-source adoption review](../research/github-adoption-review-2026-11.md) identifies reusable examples including Studerus realtime Android/NAOqi 2.9, PepperChat/NAOqi 2.5, ROS bridges, and Jetson + depth-camera research.

Differentiate via legacy compatibility, configurable verified skills, privacy-by-design, secure fleet operations and enterprise knowledge integrations. The strongest subscription proposition must solve a measurable customer-service problem. Do not market a completely independent firmware replacement without real evidence, licence clearance and a safety case.

## Legal, privacy, safety and security gates
- Clear unofficial branding; acknowledge Pepper/NAOqi/SoftBank trademarks.
- UK GDPR / applicable Japanese and other data-protection requirements: purpose, consent where needed, data minimisation, retention and deletion; publish privacy notice before registry goes live.
- No public serial numbers, passwords, precise owner locations or unsecured remote robot interfaces.
- No scraping of personal data or unsolicited bulk outreach.
- Confirm project source and SDK licences before distributing any binaries or proprietary firmware.
- Retain NAOqi safety controllers and physical emergency stop. Do not use LLM output directly as unrestricted motor commands.
- No biometric recognition by default. For public deployments, perform appropriate safety/privacy assessments.
- Clarify which third-party components and integrations will still be maintainable in a commercial service.

## Decision gates

**Gate 0 — Public usefulness:** readable English/Japanese articles, correct source links and no inaccurate compatibility guarantees.

**Gate 1 — Reachable owners:** ≥10 real owner conversations; ≥3 owners willing to share hardware compatibility information and discuss pilot scope.

**Gate 2 — Working robot:** our Pepper powered, version confirmed, SDK bridge reproducible; hotel concierge end-to-end demonstration measured.

**Gate 3 — Paid demand:** at least one paid or formally budget-approved pilot, clear task-level value and support expectations.

**Gate 4 — Commercial expansion:** evidence of repeatability, privacy/security controls, software redistribution rights, workable service margins and maintenance arrangements.

## Team / learning roles
- **Boris:** shape owner-friendly questions, compatibility quiz wording, community storytelling and first hotel persona.
- **Victor:** usability and accessibility tests, documentation demos, interview note templates and technical testing.
- **Alexander:** architecture, privacy/security, supply/repair partners, operational viability and customer validation.

## Next concrete deliverables
1. Define owner-registry data schema and consent text.
2. Design compatibility decision tree for NAOqi 2.5 / 2.9 and battery states, with safe unknown outcome.
3. Prepare English/Japanese content outline; validate Japanese technical terminology.
4. Prepare 10-owner interview guide and outreach tracker.
5. Restore our Pepper and publish a verified video of the first successful SDK command.
6. Review pricing only after genuine customer interviews and measured AI inference cost.

**Proposed brand is a working title**, not a trademark clearance or domain availability claim.
