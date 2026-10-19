# Component savings: interview cards

19 October 2026. Read the bold sentence aloud; use the evidence below if challenged. Examples explain mechanisms, not confirmed Stellantis projects. No workbook changes.

## Opening answer — about 30 seconds

“I looked for ways to remove cost without damaging what customers buy the vehicle for: shape metal more efficiently, consolidate parts, eliminate redundant hardware, and reuse modules across models. I filtered McKinsey's EV framework to remove battery-specific opportunities, then checked mechanisms against Ford, suppliers and engineering studies. The retained seven levers have a 4.9–13.2% illustrative range, midpoint about 9%. I use that as a benchmark-informed assumption, not a measured Stellantis outcome; rollout and existing optimization determine what can be achieved by 2028.”

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
