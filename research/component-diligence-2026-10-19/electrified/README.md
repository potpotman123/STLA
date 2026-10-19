# Electrified propulsion and battery diligence — 19 October 2026

**Decision:** batteries offer real engineering opportunities, but the public evidence does not establish a new, fleet-wide North American VCP saving by 2028. The strongest transparent cost evidence is an architecture-specific laboratory model; the strongest Stellantis integration evidence either already exists or lacks a named North American production date. No workbook or forecast assumption changed.

## Findings that change the interpretation

1. **A hybrid battery is not a miniature BEV battery at the same $/kWh.** A full hybrid needs frequent high-power pulses from relatively little stored energy. A BEV needs sustained energy storage. Control hardware and packaging also do not shrink proportionately. Applying a headline BEV $/kWh price to Cherokee's 1.08 kWh pack understates cost.
2. **Existing integration must not be credited again.** The Grand Cherokee 4xe already combined charger and DC/DC functions. STLA Large already specifies three-in-one motor/inverter/reduction units. A future shared component can still improve, but its baseline must be the integrated existing product, not an obsolete collection of separate boxes. [Grand Cherokee architecture](https://www.media.stellantis.com/uk-en/jeep/press/uk-orders-open-for-the-all-new-jeep-grand-cherokee-4xe-plug-in-hybrid), [STLA Large](https://www.stellantis.com/en/news/press-releases/2024/january/stellantis-unveils-bev-native-stla-large-platform-with-800-km-500-mile-range-and-the-ultimate-flexibility-to-cover-a-wide-spectrum-of-vehicles).
3. **Ram nomenclature changed.** The old pure-electric Ram 1500 program was cancelled; the current 2027 REV marketing page describes the 92 kWh range-extender truck. A pure-BEV battery-cost improvement cannot be allocated to every Ram 1500. [FY2025 report, pp15 and52](https://www.stellantis.com/content/dam/stellantis-corporate/investors/financial-reports/Stellantis-NV-20251231-Annual-Report.pdf), [current Ram](https://www.ramtruck.ca/en/1500rev).
4. **The Stellantis IBIS demonstration is interesting, but not a quantified 2028 saving.** A Peugeot E-3008 demonstrator integrates charger/inverter functions into the battery. The September2025 release reports up to10% energy-efficiency improvement, approximately40kg vehicle-level weight reduction, and end-decade production ambition. Ten-percent efficiency does not mean ten-percent component cost. Replacement electronics, validation and eligible models are unpriced. [OEM demonstration](https://www.media.stellantis.com/at-de/corporate/press/weltpremiere-erstes-prototypenfahrzeug-mit-bahnbrechendem-intelligent-battery-integrated-system-ibis-startet-praxistests-19092025).

## Representative configurations

| Architecture | Explicit example | Boundary and constraint |
|---|---|---|
| Full hybrid | 2026 Jeep Cherokee Limited4x4, Mexico specification:1.6L turbo, two electric motors,1.08kWh pack,210hp,5 seats,1,587kg tow/385kg payload | A named North American-market trim; do not apply Mexico equipment or ratings indiscriminately to US trims. No plug-in charger. [Technical sheet p2](https://www.jeep.com.mx/content/dam/cross-regional/nafta/jeep/es_mx/paginas-genericas/archivos-descargables/cherokee/FT_JEEP_CHEROKEE_2026_03FEB2026_V2.pdf) |
| PHEV | 2022 Grand Cherokee Limited4xe architecture:2.0L turbo, two motors,8-speed transmission, two-speed4x4,17kWh rounded pack,375hp, maximum6,000lb tow | Historical architecture comparator, not confirmed2028 production eligibility; pack capacity is not identified as usable energy. [OEM launch](https://www.media.stellantis.com/em-en/jeep/press/all-new-2022-jeep-grand-cherokee-the-most-technologically-advanced-4x4-capable-and-luxurious-grand-cherokee-yet) |
| BEV | 2025 Wagoneer S Limited, US:400V/100kWh rounded pack, dual electric drive,20in wheels, heated power seats, optional600hp boost | Two-row SUV, not the full-size Wagoneer or Ram. Tow/payload not established in selected primary source. [OEM launch](https://blog.stellantisnorthamerica.com/2025/02/06/all-new-all-electric-2025-jeep-wagoneer-s-limited-well-equipped-competitively-priced-and-now-open-for-orders/) |
| REEV | 2027 Ram1500 REV preproduction:92kWh battery/130kW generator, dual400V drives; targets663hp,14,000lb tow,2,600lb payload | Still carries generator-engine/fuel/exhaust/cooling hardware. These maximum ratings are not proof one VIN simultaneously achieves all maxima. [OEM targets](https://www.ramtruck.ca/en/1500rev), [generator](https://www.ramtrucks.com/electric/range-and-batteries.html) |

ICE and48V mild-hybrid configurations are covered by the main dossier. No claim that all six powertrains exist on one model.

## What the assemblies do, and what constrains cost

| Assembly | Physical parts and function | Economic opportunity and hard constraints |
|---|---|---|
| Traction motor | Rotor, stator laminations/windings, bearings, housing, position sensing; converts electricity to torque | Magnet-material alternatives, winding yield, shared designs. Motor type cannot be changed without reassessing efficiency, cooling, size and inverter controls. No verified Stellantis dollar saving found. |
| Inverter | Power semiconductors, gate drivers, capacitors, control board, cooling, enclosure; converts battery DC to controlled motor AC | Fewer duplicated housings and shorter interconnects. Higher power/voltage and heat removal still require qualified devices. Silicon-carbide efficiency is not equal to a cheaper inverter. |
| Drive unit | Motor, inverter, reduction gears, differential, lubrication/cooling in an assembly | Shared enclosure and interfaces can save material and assembly; much integration already exists. Internal manufacturing labor is not purchased-component cost. |
| Onboard charger and DC/DC | Charging electronics plus conversion for low-voltage loads | Packaging/thermal/control sharing possible. HEV lacks plug-in hardware; cannot award it charger-deletion savings. Battery still requires low-voltage support. |
| High-voltage distribution | Busbars, cables, connectors, contactors, fuses, isolation monitoring and charge port | Routing and connectors can simplify. Current, fault interruption, insulation and collision protection remain required. Higher voltage changes the entire system design. |
| Battery cells | Cathode/anode active material, current-collector foil, separator, electrolyte, casing | Chemistry, yield and electrode design matter. Power, lifetime, fast charging, temperature and energy density constrain substitution. Cheaper chemistry may require a larger/heavier pack. |
| Pack | Modules if used, enclosure, structure, cooling plates, sensors, BMS, connectors, protection | Fewer modules can reduce inactive hardware. Structural integration affects repairability, crash behavior, body tooling and service method; not a free refresh change. |
| Thermal system | Pumps, valves, heat exchangers, pipes, refrigerant interfaces, heaters/chillers | Shared circuits and fewer joints; battery, cabin and propulsion may need different simultaneous temperatures. Trailer towing and cold weather are design constraints. |
| REEV generator system | Engine, generator, controls, fuel/exhaust and cooling | Can operate engine differently from a mechanically driven truck, but it remains additional hardware. Smaller battery versus BEV changes electric range and operating proposition; not a like-for-like savings proof. |

These rows are engineering reasoning, not disclosed Stellantis projects. For an outsourced assembly, the invoice is variable per vehicle but recovers supplier fixed tooling/engineering. For an in-house motor or battery operation, classify the actual material and plant expenses separately. No contract evidence shows that supplier efficiency automatically passes through to Stellantis.

## Transparent battery cost anchors

All figures below are **modeled US production, constant2023USD per pack**, excluding45X. They are not current Stellantis quotes. Costs include supplier capital recovery, overhead, R&D, profit and warranty; motors/chargers and OEM integration are outside this battery boundary. Freight/tariff treatment is not established. MY2026 pack volumes are200k HEV/60k PHEV/140k BEV;2030 uses200k/100k/250k, with cell plants growing50→70GWh. [Argonne, Tables1,8–12,18–19](https://publications.anl.gov/anlpubs/2024/01/187177.pdf).

| Fixed rated-energy/power comparator |2026 pack cost|2030 pack cost|Full modeled reduction|Illustrative2028 midpoint reduction*|
|---|---:|---:|---:|---:|
|1.2kWh/48kW HEV|$664|$644|$20|$10|
|1.8kWh/70kW HEV|$752|$725|$27|$14|
|18kWh/150kW PHEV, Ni/Mn|$2,829|$2,664|$166|$83|
|24kWh/200kW PHEV, Ni/Mn|$3,453|$3,193|$260|$130|
|90kWh/200kW BEV SUV, Ni/Mn|$10,465|$9,004|$1,462|$731|
|105kWh/260kW BEV pickup, Ni/Mn|$12,024|$10,409|$1,615|$807|

*The2028 midpoint is our timing sensitivity, not an Argonne or Stellantis forecast. The path combines chemistry, design, scale, yield and assumed material-price changes; it cannot be called pure VCP execution. None is an exact Ram/Jeep pack match. Rated-energy versus usable-energy denominators must remain separate.

The same2026 model shows Ni/Mn→LFP differences of$246 for24kWh PHEV,$1,367 for90kWh BEV and$1,334 for105kWh BEV. These are **alternative**, not additional savings. Equal rated energy/power does not establish equal vehicle mass, range, towing or packaging.

## Three concrete mechanism tests

**Scale/shared cells:** Argonne's separate sensitivity study models a10GWh pack operation at$138/kWh if cell production is also10GWh, versus$134 if cells come from a50GWh operation. The$4/kWh difference is about2.9%, not a proportional fivefold saving. This is supplier economics, not an observed OEM invoice concession.

**Chemistry tradeoff:** The same study's PHEV example substitutes LFP for NMC622: pack cost changes$143→$142/kWh, while mass rises186→237kg. Lower cathode cost alone does not make a complete pack dramatically cheaper. Its BEV chemistry examples have different outcomes and remove a fast-charge constraint; do not transplant them into this PHEV.

**Yield and demand:** Scrap consumes materials and processing without producing a saleable cell; avoiding it can genuinely reduce resource use. But factory capacity is not utilization. The FY2025 filing reports EV-capacity rationalization and NextStar exit obligations—disconfirming evidence for a frictionless scale story. [Argonne sensitivity, pp9–13 and37](https://publications.anl.gov/anlpubs/2023/08/183571.pdf), [Stellantis FY2025, pp52–53](https://www.stellantis.com/content/dam/stellantis-corporate/investors/financial-reports/Stellantis-NV-20251231-Annual-Report.pdf).

## A/B/C/D model treatment and adoption

- **A — technical partial frontier:** retain each Argonne pack's rated energy/power and use its2030 endpoint. Never combine NMC and LFP endpoints, IBIS, and independent component savings into one fictional battery.
- **B — economically attractive:** calculate a break-even implementation budget = per-pack saving × remaining eligible lifetime packs. The script uses200,000 lifetime packs solely as a scale illustration; actual OEM investment is unknown. Discounting, warranty offsets and supplier sharing would reduce that ceiling. This is a hurdle, not proof of payback.
- **C —2028:** midpoint cost path is an explicit sensitivity, with annual benefits shown per10,000 eligible vehicles. Actual Stellantis coverage, supplier capture and integration cost remain null. No North American annual total is admitted from this work.
- **D — delay:**2026 modeled pack costs persist through2028. Incremental savings for this particular step are zero; that does not mean total battery opportunity is zero.

STLA One targets2027 launch with more LFP and cell-to-body integration, but its20% platform target cannot be added atop the pack projects. Specific Ram/Jeep2028 adoption and volumes are not established here. The announced CATL Spain factory targets European B/C applications; it does not prove North American sourcing. [STLA One](https://www.stellantis.com/en/news/press-releases/2026/may/stellantis-unveils-stla-one-global-modular-vehicle-architecture), [Spain JV](https://www.stellantis.com/en/news/press-releases/2024/december/stellantis-and-calt-to-invest-up-to-4-1-billion-in-joint-venture-for-large-scale-lfp-battery-plant-in-spain).

## Interview takeaway and missing evidence

“Electrification has substantial design-to-cost potential, but the saving depends on what vehicle we actually sell. A small hybrid battery, a performance-SUV battery and a towing-truck battery solve different problems. We cannot apply a BEV cost decline to the whole component bill, or count integration that Stellantis already uses. I need the current supplier price, replacement specification, approved production date and eligible sold volume before assigning2028 AOI.”

This sub-workstream neither validates nor disproves the€35bn×9%=€3.15bn component scenario. Full-vehicle component denominators, propulsion-specific volumes, existing contract trajectories, implementation spending and purchase-price capture are missing. The quantified battery comparisons are partial evidence, not the unexplained remainder of a complete vehicle BOM.

Files: `architectures.json`, `sources.json`, `battery-benchmarks.json`, `projects.json`, `calculate.py`, `calculated.json`. Run `python3 calculate.py` to reproduce arithmetic; no workbook access. No EUR conversion is imposed on constant2023USD benchmarks.
