# Parts unit economics: first-pass operating framework

18 October 2026. No forecast or workbook changed. Research question: which purchased-component savings are economically feasible for an existing Ram pickup, and which require changes in product performance, architecture, contracts or investment?

## Scope and classification

Illustrative vehicle: Ram 1500 gasoline, Hurricane engine, 4WD. This is a system-level map, not a VIN-specific BOM or supplier quote. Trim, model year and optional content must be fixed before costing. Public product specifications do not disclose factory procurement prices. Retail service-part prices are not valid substitutes.

Purchased parts are predominantly variable per vehicle from the OEM perspective, while their prices recover supplier variable inputs, fixed tooling/engineering/capacity and margin. Fixed/variable describes volume behavior; reducibility is a separate dimension. OEM-owned tooling, minimum-volume commitments and in-house engine/transmission production complicate classification. Never count supplier transformation embedded in purchased parts again as Stellantis manufacturing savings.

## System map and engineering hypotheses (not observed Ram savings)

| System | Items | Potential lever | Constraint |
|---|---|---|---|
| Structure/body | frame, crossmembers, panels, doors, bed, hood, brackets | material yield, common stampings, fewer joining operations | crash, fatigue, corrosion, tooling |
| Engine | block, head, crankshaft, pistons, bearings, cams, valves, oil system | shared castings, machining yield, sourcing | durability, thermal/load capability; make/buy boundary |
| Air/fuel/turbo | turbochargers, charge coolers, injectors, pumps, filters, sensors | supplier competition, integration | power, emissions, heat, calibration |
| Transmission/4WD | gears, clutches, torque converter, transfer case, differentials, shafts | common components, specifications, sourcing | torque, towing, validation, switching cost |
| Thermal/exhaust | radiator, fans, pumps, hoses, catalyst, muffler, sensors | routing, integration, material yield | cooling duty, emissions performance, commodity content |
| Suspension/steering/brakes | arms, knuckles, springs, dampers, rack, rotors, calipers, ABS | common modules, manufacturing yield | load rating, ride, stopping performance; option deletion changes product |
| Wheels/tires | rims, tires, TPMS, spare | fewer variants, competing qualified bids | load, grip, noise, buyer preference |
| Electrical/electronics | harness, connectors, modules, chips, alternator/battery as equipped | variant reduction, shorter wiring, integration | software, thermal, qualification; architecture changes slow |
| Cabin | seats, foam, frames, upholstery, dash, console, trim | common hidden components, tooling, assembly simplification | comfort, perceived quality, crash integration |
| HVAC/glass/closures | compressor, heat exchangers, ducts, glass, seals, latches | common components, supplier process | defogging, leakage, noise, reliability |
| Lighting/ADAS/restraints | lamps, cameras/radar as equipped, airbags, belts | module reuse, sourcing, packaging | performance and validation; do not equate required function with immutable part price |
| Miscellaneous | fasteners, adhesives, paint, fluids, insulation | standardization, process waste | corrosion, NVH, durability |

No percentage saving assigned by system without spend and engineering evidence. Large supplier price cuts do not guarantee equally large whole-pool savings. Safety-critical does not mean unsaveable; commodity-heavy does not mean fixed-price. Product deletion is a mix/value proposition decision, not automatically comparable-content productivity.

## Mechanics and model implications

Same-content purchasing saving = old invoice less new invoice on eligible units. Redesign requires validation, tooling and timing. Commodity deflation is separate from controllable productivity. Lower trim mix reduces revenue as well as cost. Supplier fixed-cost absorption benefits Stellantis only if pricing changes; it is not automatically OEM cash savings.

Our estimated EUR35bn pool ×9% gives EUR3.15bn terminal annual gross savings arithmetically, not independent validation. Existing VCP notes qualify 9% as ambitious. Preserve commodity, timing, ordinary productivity, internal manufacture and warranty boundaries. A reduction in procurement cost initially enters inventory; AOI generally follows cost of vehicles sold, subject to accounting treatment. Capex and warranty/provision effects are separate from the recurring purchase-price delta.

## Evidence retrieved / limitations

- Stellantis supplier workshops target cost, waste and quality: https://www.stellantis.com/en/sustainability/engaging-our-stakeholders/suppliers-and-partners/driving-supplier-excellence (opened).
- Aptiv SEC correspondence, 13 May 2024, annual per-part reductions, negotiability and volume/cost dependencies: https://www.sec.gov/Archives/edgar/data/1521332/000152133224000043/filename1.htm (opened; lines101–114).
- Magna annual report explains embedded engineering/tooling recovery, price concessions and commodity risks: https://www.sec.gov/Archives/edgar/data/749098/000110465924040524/tm241263d3_ex99-1.pdf (indexed excerpt, not full PDF reviewed).
- Official 2025 Ram product launch: https://blog.stellantisnorthamerica.com/2023/12/02/new-2025-ram-1500-with-more-powerful-more-fuel-efficient-hurricane-engine-family-unveiled/ (search result).
- Official fleet guide indexed but direct retrieval returned404: https://www.stellantisfleet.com/content/dam/fca-fleet/na/fleet/en_us/shopping-tools/brochures-literature/docs/buyers-guide/2025/25DOMFLT_FBG_Ram1500.pdf . Do not claim complete BOM review.
- Existing historical outcome evidence: ../vcp-schedule-2026-10-14/component-nine-percent-plausibility.md and nissan-analogue.md.

Next productive depth: select exact configuration, map engine/driveline make-vs-buy and source comparable engineering changes. Detailed component dollars remain unknown; no bulk teardown acquisition performed.
