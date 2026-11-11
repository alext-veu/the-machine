# Field restoration runbook

**Known:** Pepper unused approximately two years, charger lost, password/account unknown, hardware and OS revisions not yet identified.

## P0: document
Photograph complete robot, identification plate, charging flap and connector, rear of head and tablet. Keep full serial identifiers and credentials private. Inspect for damage, battery swelling, odour or excess heat. If present, stop and consult a specialist.

## P1: power
Select original-compatible 28.6 V 8 A Pepper charger with verified connector and polarity; see [hardware and power](hardware-and-power.md). Verify UK mains suitability. Charge only according to manufacturer's guide. Record LEDs, sounds, charging behaviour and time. Do not force-charge or bypass the lithium pack's protection circuitry.

## P2: boot and inventory
In a clear, level area, follow documented emergency stop release and normal chest-button startup. Record tablet state, LEDs, voice, motion, NAOqi release and hardware revision. Do not attempt blind firmware reset.

## P3: network
Connect to an isolated wired/Wi-Fi LAN; identify IP from spoken announcement (where supported), tablet or DHCP. Test browser management UI, SSH or robot API using authorised credentials. Try documented defaults only where applicable. Avoid exposure of legacy NAOqi services to the internet or production network.

## P4: preserve or recover
If authorised access works, export application/config inventory and backup before factory reset. Otherwise, investigate vendor-supported recovery or qualified repair. Local firmware file alone does not fix an unknown SSH password.

## P5: first control
On an external PC, test read-only API discovery, then text-to-speech, then a small supervised gesture with clear surroundings and emergency stop accessible. Keep cloud AI out of motion control until allowlists and safety limits are in place.

## Inspection record
| Field | Value |
|---|---|
| Hardware revision | TBD |
| Firmware release | TBD |
| Charging adapter and connector | TBD |
| Charging result | TBD |
| Boot / tablet status | TBD |
| IP / SDK access | TBD |
| Backup | TBD |
| Next decision | TBD |
