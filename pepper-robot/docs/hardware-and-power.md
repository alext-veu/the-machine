# Pepper hardware, power and procurement

Research snapshot: 11 November 2026. **Revision-specific values must be confirmed from labels and running system.**

## Robot concept and hardware

Pepper was introduced in 2014 as a social/human-interaction robot for customer service, education, hospitality, research and demonstration. Around 1.2 m high, it uses a wheeled base, a chest tablet, cameras/depth sensing, microphones, speakers and articulated upper body. It was not designed as an industrial lifting robot.

Common later Pepper 1.8-series documentation describes an **Intel Atom E3845 (quad-core, 1.91 GHz), 4 GB RAM and 32 GB eMMC**, but this is **not universal**. Pepper 1.6 documentation describes differing internal storage (including eMMC and microSD arrangements) and RAM accessible to the operating system. Identify the revision before ordering parts.

## Charger: required compatibility checks

Reported original charger class: **Delta ADP-235CR-A / ADP-235AR-A**; **AC 100–240 V, 50/60 Hz**, DC approximately **28.6 V at 8 A** (~229 W), with **Pepper-specific twist-lock charging connector**. Do **not** purchase by voltage alone. Ask the seller for photographs of the actual barrel/locking plug, output label, polarity/pinout confirmation, serial/model identifiers, mains cable and proof of testing on Pepper.

### Two current online purchasing leads

| Option | Advertised price | Shipping advertised | Approx. before tax/import | Status |
|---|---:|---:|---:|---|
| Delta ADP-235CR-A, used, eBay marketplace | **US $129.68** | **US $25.00** | **US $154.68** | Marketplace search result on 11 Nov 2026; confirm listing and UK checkout |
| Delta ADP-235AR-A, used, eBay marketplace | **US $128.00** | **Free delivery advertised** | **US $128.00** | Marketplace search result on 11 Nov 2026; confirm UK checkout and connector |

Current marketplace search: https://www.ebay.com/sch/i.html?_nkw=softbank+charger&_sop=12

Earlier ADP-235CR-A listing: https://www.ebay.com/itm/267446715716 (US $134.99 + US $26 advertised at prior check; availability may change).

**Excluded alternative:** a UK listing around **£202.08** was advertised for **NAO**, a different robot. It is **not a confirmed Pepper-compatible charger**, and must not be treated as an interchangeable purchasing option.

No purchase placed; no UK VAT, import duty, UK checkout shipping or current stock guaranteed. Seller should confirm correct variant and connector before payment.

## Battery

Original Pepper battery reported as **lithium-ion, ~26.46 V nominal, 30 Ah, ~795 Wh**. Two years unused means deep discharge, battery-management protection or failure are material possibilities, but condition is unknown until tested. Use the compatible charger and documented startup procedure only. Never directly inject DC into the pack, force-charge, bypass BMS or open cells. Stop if swelling, unusual heat, leakage or smell is present. A failed battery may require specialist replacement and hazardous-goods transport.

### Replacement/service lead

[IRIS Robotics Pepper service (Europe)](https://irisrobotics.eu/en/service-pepper-europe): advertised Pepper diagnostics/service; a previously observed diagnostic figure was **€250 plus VAT** (reconfirm current quote). Ask for OEM/compatible complete battery availability, price, lead time, import/shipping terms, and whether the robot can boot on adapter with failed battery. Complete UK replacement pack and price remain **unverified**.

## Connections and modification opportunities

Some Pepper hardware service documentation refers to internal or under-cover **Ethernet, USB, serial and storage interfaces**. These are **not necessarily customer-accessible expansion ports**. Manufacturer cautions apply to head-cover access and unapproved USB peripherals. Do not promise USB power delivery or a drop-in SSD/RAM upgrade; no supported RAM-slot replacement path is confirmed.

**Preferred performance upgrade:** connect a separate mini PC (e.g., Raspberry Pi 5 or x86 mini PC) over Pepper's LAN and keep original motor/safety control on Pepper. Use independently engineered power, isolation and cooling. Prove the system externally before considering an internal installation.

Sources: [Pepper user guide (2019)](https://www.aldebaran.com/sites/default/files/node/support/download/PEPPER_UserGuide_EN_2019%2007%2005_1.pdf); [hardware parameter sheet](https://www.softbankrobotics.com.cn/index_files/pdf/Hardware_Parameters_en.pdf); [Maxtronics Pepper support](https://maxtronics.com/fr/support/kb/category/pepper/).
