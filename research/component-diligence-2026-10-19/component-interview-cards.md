# Component savings: interview cards

19 October 2026. Read the bold sentence aloud; use the evidence below if challenged. Examples explain mechanisms, not confirmed Stellantis projects. No workbook changes.

## Opening answer — about 30 seconds

“I first broke the vehicle into physical systems—body, powertrain, chassis, thermal, electronics and interior—rather than treating component spending as one reducible lump. For each, I asked what function must be preserved, what drives cost, and what could actually change. Then I matched those systems to specific engineering levers and outside evidence. That supports a roughly 9% benchmark-informed assumption, with explicit uncertainty around transferability and rollout, rather than a claim that every part becomes 9% cheaper.”

## How we decomposed the problem

**Vague question → physical systems → cost drivers and constraints → specific changes → comparable evidence → portfolio-level assumption.**

This is a summary of our existing [24-category system map](system-map.csv), not a newly invented cost allocation. The interview groupings below organize the original categories; they do not imply equal spending weights or independently measured dollar pools.

| System group | What we put inside it | Specific question we could then investigate |
|---|---|---|
|**Body, structure and closures** (A1–A3)|Frame/unibody, crash structures, doors, bed, latches, joining and coatings|Can geometry or part consolidation reduce steel and joints while retaining crash, cargo and corrosion performance?|
|**Combustion engine and emissions** (B1–B3)|Block/head, pistons, fuel injection, turbocharging, exhaust and catalysts|Can casting, machining or materials improve without compromising towing durability or emissions? A smaller engine may add costly boost/cooling equipment.|
|**Transmission and driveline** (C1–C2)|Gearbox, torque converter, transfer case, differentials and shafts|Can torque-rated modules be shared? Removing four-wheel drive is a content change, not equal-function efficiency.|
|**Electrified propulsion and batteries** (D1–D5, E1–E2)|Motors, inverters, charging, mild-hybrid equipment, range extender, cells and pack|Which hardware actually exists on this powertrain? Is integration already present, and does a component saving increase cost elsewhere?|
|**Thermal management** (F1)|Cooling circuits, pumps, valves, radiators and cabin HVAC|Can housings/interfaces be shared or circuits simplified while meeting different temperature requirements?|
|**Chassis and road contact** (G1–G2)|Suspension, steering, brakes, wheels and tires|Which variants are genuinely needed for payload, ride, handling and stopping performance?|
|**Electrical distribution and computing** (H1–H2)|Harnesses, electrical centers, controllers, networks and software|Can we reduce harness variants and duplicate controllers while retaining safety and reliability?|
|**Interior, safety and customer-facing equipment** (I1–I3)|Seats, trim, displays, audio, restraints, ADAS, lights and mirrors|Which hidden parts can be shared, and which visible features drive willingness to pay?|
|**Residual / scope reconciliation** (J1)|Unmapped items and costs outside a comparable purchased-parts boundary|What did we omit, and have we mixed supplier prices with our own plant costs, tooling or engineering?|

**Important interfaces:** ADAS hardware is recorded under I3 but shares compute with H2; battery thermal hardware connects E2 and F1; range-extender engines connect D5 and B1–B3. These are functional research categories, not yet an audited, mutually exclusive bill of materials. Assign each economic saving to one owner before aggregation.

## What we asked inside every system

- **Function:** What must this part do for the customer, safety or regulation?
- **Cost driver:** Is the expense metal, precision machining, semiconductor content, supplier scale, unique tooling, or complexity?
- **Change:** Can we substitute, reshape, integrate, standardize or delete something while retaining the required function?
- **Evidence:** Is the number a realized result, supplier claim, management target, engineering estimate or our assumption? What is its denominator?
- **Timing:** Is this a carryover change or a new-platform redesign? What portion of production receives it by 2028?
- **Accounting:** Does the benefit reduce purchased parts, own-plant conversion costs, warranty, R&D or capex? Where might we count it twice?

**Fixed versus variable:** a purchased component normally scales with vehicles built, but its supplier price also recovers tooling, engineering and capacity. Sharing a module can spread those fixed costs across more units. That does not make all of the supplier's saving an immediate Stellantis purchase-price reduction.

## One worked reasoning chain

**Start with body structure → isolate the strut-top assembly → identify overlapping metal and weld operations → test a single formed part → compare cost at equivalent structural performance → determine which future vehicle programs could adopt it.** The Ricardo example below supplies an engineering comparator. It does not give us a verified Ram saving or permission to apply its percentage to the whole vehicle.

**Systems describe where the money goes; levers describe how the money can be reduced.** Standardization can touch seats, wiring and driveline simultaneously. Conversely, one wiring project can involve design-to-value, complexity reduction and electronics integration. One project is still one saving.

## How this work supports the model—and where it stops

We built a granular **functional and mechanistic map**, not 24 independently verified Stellantis cost pools. System-level purchase prices remain largely unknown. The map helps test whether an industry benchmark makes physical sense, identify exclusions and direct evidence gathering. Our current roughly 9% comes from the filtered McKinsey benchmark below, not from summing 24 measured system-level forecasts.

With complete data, we would sum: **system cost base × achievable reduction × implementation coverage**, using consistent baseline quantities and netting overlaps/offsets. In the current model, the evidence supports an aggregate assumption with rollout uncertainty; it does not justify filling missing subsystem costs with invented precision.

## User direction and how it improved the analysis

- **Start from the physical car:** the user pushed beyond a generic cost-cutting percentage toward essential systems and actual parts.
- **Broaden beyond an isolated anecdote:** the user challenged repeated emphasis on a $40 electrical project; the research expanded to multiple systems and an aggregate benchmark.
- **Test applicability:** the user challenged EV-only evidence; we separated common vehicle mechanisms from battery-specific opportunities.
- **Keep the explanation concrete:** the user requested physical examples and interview-ready reasoning, then asked us to restore the system decomposition to that narrative.
- **Result:** an inspectable chain from category to mechanism to evidence to assumption, with unknowns retained rather than concealed. These are research decisions and user interventions, not a claim of access to confidential vehicle cost data.

## Eight concrete examples

1. **Change the shape, not just the metal thickness.** McKinsey illustrates a 1.5-mm grooved bracket replacing a 2.5-mm design while retaining stiffness and structural integrity. Engineering intuition: forming ribs changes bending resistance, allowing less metal. **Do not call this a 40% part-cost saving**: thickness is not total cost, and forming/validation still matter. *Lever 2; illustrative design, no quoted dollar saving.* [McKinsey](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/building-profitable-evs-ten-structural-design-moves-to-cut-material-costs)

2. **Replace five joined metal pieces with one formed piece.** Ricardo's front strut-top concept removes four welding processes and overlapping weld flanges. Its figure shows **$37.30 → $26.20 per piece**, excluding assembly. Less overlapping steel and fewer operations explain the saving; the whole front-structure study indicates 10% piece-cost reduction. *Lever 2/4; virtual feasibility study, not realized OEM results. Count once. Report narrative uses a different approximate percentage; use the figure's explicit cost boundary.* [WorldAutoSteel/Ricardo, PDF p4](https://www.worldautosteel.org/wp-content/uploads/2026/05/WorldAutoSteel-A4-PC-Study_512.pdf)

3. **Stop manufacturing hundreds of versions of the same wiring bundle.** Ford reduced Explorer main-harness variants **500 → 14**, estimating **$7m/year** savings. General mechanism: longer repeat production runs, fewer unique parts and simpler stocking/sequencing. *Lever 5; Ford estimate, not verified realized savings. Do not add it again under electronics.* [Ford CMD, PDF pp8–9](https://s201.q4cdn.com/693218008/files/doc_events/2023/May/22/capital-markets-day-transcript-5-22-23.pdf)

4. **Ask whether a part still needs to exist.** Ford identified a cable included as a manufacturing aid and projected **$11m/year** from deleting it. A requirement left over from how a vehicle was built can keep imposing cost on every subsequent unit. *Lever 8; prospective savings; affected unit count undisclosed. Don't extrapolate to every cable.* [Ford CMD, PDF p8](https://s201.q4cdn.com/693218008/files/doc_events/2023/May/22/capital-markets-day-transcript-5-22-23.pdf)

5. **Buy the specification the function requires.** Ford projected **$35m/year** from material changes to exhaust manifolds, mounts and front rails. This supports material substitution on gasoline vehicles; Ford does not disclose the precise substitute alloys. *Lever 2; do not invent steel grades or interpret this as cutting crash protection.* [Ford CMD, PDF p8](https://s201.q4cdn.com/693218008/files/doc_events/2023/May/22/capital-markets-day-transcript-5-22-23.pdf)

6. **Share computing rather than duplicating it around the car.** Aptiv's satellite approach centralizes ADAS processing and simplifies sensors; its sustainability report claims **10% system-cost savings for equivalent features**. Common computation can avoid duplicated hardware while preserving the driver's functionality. *Lever 10; supplier claim for ADAS, not 10% of total vehicle cost. Safety redundancy still has to be retained.* [Architecture explanation](https://downloads.aptiv.com/libraries/docs/default-source/aptiv-storage/2025_aptiv_ces_knowbeforeyougo.pdf?sfvrsn=5da8637_4), [cost claim, p22](https://downloads.aptiv.com/libraries/docs/default-source/aptiv-storage/2020_aptiv_sustainability_report_f.pdf?sfvrsn=f2ae913e_2)

7. **Reuse the hidden vehicle building blocks.** Renault–Nissan CMF shares compatible engine-bay, cockpit, underbody and electrical modules across different models. Aggregating orders and avoiding bespoke tooling are the economic mechanisms. Announcement targeted **20–30% component-purchasing savings**, separately from engineering/investment savings. *Levers 7/9; 2013 multiyear target, not verified outcome or additional percentage to stack on McKinsey.* [Nissan](https://usa.nissannews.com/en-US/releases/common-module-family-cmf-a-new-approach-to-engineering-for-the-renault-nissan-alliance)

8. **Integrate plumbing and controls into a module.** EFESO's hybrid/EV thermal-module supplier case combined technical redesign, material substitutions, sourcing and assembly-process work; **>10% material/manufacturing savings indicated**. General integration mechanism: shared housing/interfaces can remove separate connections and assembly steps. *Lever 4; those specific deletions are engineering interpretation, not individually quantified EFESO changes. Supplier manufacturing savings count for STLA materials only to the extent reflected in purchase prices.* [EFESO](https://www.efeso.com/client-results/product-cost-optimization-for-automotive-thermal-management-system/)

## Two useful nuances if pressed

- **The cheaper system can contain a more expensive part.** A McKinsey instrument-cluster case standardized on the most expensive of three variants; reduced complexity elsewhere outweighed the hardware increase. Reported 3% savings in that example. This is why inventory, warranty and engineering savings cannot all be booked as materials. [Complexity study](https://www.mckinsey.com/capabilities/operations/our-insights/calculating-complexity-maximizing-the-value-of-customization)
- **Removing features is a different bet from improving engineering.** McKinsey's roughly $250 seat example removes ventilation/adjustable cushions and substitutes synthetic leather. That may be appropriate for an affordable trim, but sacrificing willingness to pay could offset the saving. Keep it separate from equal-function efficiency. [McKinsey](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/building-profitable-evs-ten-structural-design-moves-to-cut-material-costs)

## Where “about 9%” comes from

Transcribed from the user's supplied McKinsey exhibit; values are contributions to the original EV material-cost denominator. They are not independently estimated STLA project savings.

| Included lever | Low | High | Midpoint |
|---|---:|---:|---:|
|2 Design to value|2.3%|6.1%|4.20%|
|4 System integration, conditional transfer|0.7%|1.9%|1.30%|
|5 Trim complexity|0.6%|1.6%|1.10%|
|7 Flexible platforms|0.5%|1.4%|0.95%|
|8 Requirements review|0.3%|0.8%|0.55%|
|9 Supplier modules|0.3%|0.8%|0.55%|
|10 Electronics integration|0.2%|0.6%|0.40%|
|**Total**|**4.9%**|**13.2%**|**9.05%**|

Arithmetic is reproducible in [the audit](ten-lever-audit/calculations.json). Exclude #1 battery downsizing and #3 EV technology mix; exclude #6's heavily EV-specific subsystem examples from this selected subtotal. Without conditional #4, midpoint is 7.75%. Design-to-value provides nearly half the selected midpoint, making remaining overengineering/content tradeoffs a key sensitivity.

## Close the answer accurately

“These examples make the mechanisms credible; they do not independently prove the 9%. My forecast transfers an illustrative benchmark to Stellantis, then needs an implementation schedule. On our estimated €35bn reference component pool, 9% means €3.15bn annual benefit at full implementation. If only reached in December 2028, that is an exit run rate—not €3.15bn recognized throughout 2028.”

**If asked what could go wrong:** existing designs may already capture the savings; launch/tooling work may slip; suppliers may retain benefits; quality or customer appeal may deteriorate; gross savings may be offset by inflation/new content. Distinguish purchased-material savings, own-plant efficiencies and capex avoidance, and count each project once. These notes add no new forecast inputs.
