# North American VCP: addressability and achievable savings

14 October 2026. Proposed assumptions for review; **no workbook or preserved AI baseline changed**. EUR billions unless stated otherwise.

**Subsequent method change:** The user has approved one effective rate per full cost pool and requested historical/peer calibration. The two-factor scenarios below are preserved research history, not current recommended inputs. See [replacement benchmark assessment](vcp-historical-benchmark-replacement.md) and the revised model architecture. Changing the formula does not independently validate these old rates.

## Conclusion and model admission

Our conditional base case is **€2.1bn of annual operational AOI benefit recognized in 2028 versus 2025**, with €0.7bn downside and €3.6bn upside. This is after assumed program-related AOI expenses, but **before separately modeled wage/material inflation, tariffs, FX, changes in warranty coverage, volume/mix and net pricing**. It is not a forecast that reported NA AOI rises by exactly €2.1bn.

Mechanisms are supported; the precise eligible shares, reductions and annual timing are analyst judgments. The bounded search did not independently establish those percentages. Use these as transparent scenario inputs, not measured actuals or statistically calibrated forecasts. Numerical confidence is low, especially in the regional component allocation, payroll and indirect-cost bases.

The independently built base case falls below management's **more than €3bn NA target**. Our mature gross opportunity is €2.43bn; annual timing and assumed AOI expense allowances reduce 2028 recognition to €2.09bn. This separates a genuine execution disagreement from a timing disagreement. It does not prove management's target is impossible.

| Driver | 2025 annual base | Addressable by end-2028 | Reduction on eligible spending | Mature gross annual saving | 2028 recognized AOI benefit | Numerical confidence |
|---|---:|---:|---:|---:|---:|---|
| Components/direct materials | 35.0 | 60% | 7% | 1.470 | 1.293 | Low |
| Manufacturing — plant labor | 5.5 | 50% | 10% | 0.275 | 0.233 | Low; base unvalidated |
| Manufacturing — cash plant costs | 1.5 | 70% | 12% | 0.126 | 0.108 | Low |
| Manufacturing — depreciation | 1.8 | 0% | 0% | 0 | 0 | No supported saving mechanism |
| Quality/warranty | 3.0 | 50% | 25% | 0.375 | 0.304 | Low; early-quality trend observed |
| Logistics/eligible indirect | 2.5 | 60% | 12% | 0.180 | 0.152 | Low |
| **Total benefit** | — | — | — | **2.426** | **2.090** | **Conditional scenario** |

The three manufacturing rows form **one workstream**, worth about €0.34bn recognized in the base case. These cost pools are not a complete revenue-to-AOI expense statement. Quality eligibility excludes the approximately €0.9bn remeasurement pool: €1.5bn eligible is about 71% of the remaining rounded €2.1bn, not 50% of that smaller denominator.

## Method and definitions

Start with the provisionally accepted [cost bases](three-other-vcp-bases.md), [cash plant estimate](cash-plant-cost-estimate.md) and [labor limitations](manufacturing-input-validation.md). Re-read relevant May Investor Day and Q2 materials. Then test mechanisms against supplier filings, union terms, a named logistics implementation and warranty accounting/coverage. Two bounded parallel checks covered components and manufacturing; no bulk extraction, paid data or plant-by-plant collection was used. Further generic descriptions would not identify the unknown rates, so discovery stopped.

For each driver:

`Base × share feasible by end-2028 × reduction on eligible spending = mature gross annual saving`

`Mature gross saving × annual-average recognition fraction − incremental expense within AOI = recognized annual operational benefit`

Addressability concerns spending with a feasible intervention; reduction concerns its economic yield. Recognition captures deployment through the year and inventory/provision timing, not another probability haircut. The detailed factors remain research support. The workbook can use the resulting effective percentage of each full cost base.

The base-case mature total of €2.426bn loses €0.261bn to annual timing/recognition and €0.075bn to assumed incremental AOI expenses in 2028. The latter are **explicit allowances, not disclosed budgets**. They cover supplier support, validation, training, software and transition/service preservation. Capex, settlement of old provisions and restructuring excluded from AOI must instead follow their own accounting. Doubling these allowances lowers the base result by another €75m.

No quarterly project curve is introduced: **annual recognized benefit divided by four**. Annual assumptions are still necessary to distinguish a year-end run rate from a full-year income-statement benefit.

## Annual scenarios

All figures below are annual benefits relative to the same 2025 base, not three-year cumulative cash savings.

| Annual recognized operational benefit | 2026 | 2027 | 2028 |
|---|---:|---:|---:|
| Downside | 0.132 | 0.397 | 0.730 |
| Base | 0.484 | 1.322 | 2.090 |
| Upside | 1.007 | 2.559 | 3.602 |
| **Base incremental improvement versus prior year** | **0.484** | **0.838** | **0.768** |
| Base annual benefit divided by four | 0.121 | 0.330 | 0.522 |

For a year-over-year quarterly AOI bridge, the base VCP additions are approximately €121m in each 2026 quarter, €210m in each 2027 quarter and €192m in each 2028 quarter. Do not add the full €522m to 2027 AOI again in 2028. Existing 2026 reported results already include some savings: these estimates cannot be layered on top of actual industrial improvement as if entirely incremental.

| Scenario assumptions: eligible share / reduction | Downside | Base | Upside |
|---|---|---|---|
| Components | 45% / 4% | 60% / 7% | 75% / 10% |
| Labor | 35% / 5% | 50% / 10% | 60% / 12% |
| Cash plant | 60% / 8% | 70% / 12% | 75% / 14% |
| Quality | 30% / 15% | 50% / 25% | 60% / 30% |
| Logistics/indirect | 40% / 8% | 60% / 12% | 65% / 14% |

Downside assumes many engineering reviews fail commercial or validation tests and labor flexibility remains limited. Base assumes meaningful carryover-product cost changes and selective paid-cost removal. Upside assumes materially broader component redesign and faster execution, with more moderate improvements elsewhere. All cases keep the same cost bases, zero depreciation savings and zero automatic accounting releases. They do not combine favorable volume, commodity or pricing assumptions. These are coherent scenarios, not probability bounds.

Base annual recognition fractions for 2026/27/28 are components 25/60/90%; labor and cash plant 15/55/90%; quality 20/55/85%; logistics 20/60/90%. Existing purchasing activity supports nonzero 2026 benefit; late-2026 implementation and engineering lead times support a larger 2027 contribution. Quality needs credible lifetime-cost evidence. None of these exact fractions is disclosed. [Inputs](vcp-savings-inputs.json) retain all cases and expense allowances; [results](vcp-savings-results.json) show driver-by-year benefits and effective full-base rates. Reproduce with `python3 research/investor-day-2026-05-21/calculate-vcp-savings.py` from the repository root.

## Driver judgments and revision tests

### Components: largest opportunity, largest uncertainty

Management proposes commercial negotiations and technical changes. Its >80% NA/Europe component review coverage and approximately 35% first wave are **review scope**, not savings or implementation. Lear confirms annual OEM price reductions are already routine; Magna reports typical new-program award-to-production lead times of 2–4 years. These establish bargaining and engineering constraints, not a representative savings rate. [S1, S3, S5, S6]

We assume 60% of the €35bn base can be affected by end-2028, allowing for sole-source content, contracts, tooling, validation and changes with poor economics. The 7% eligible-cost reduction is a judgmental three-year total: roughly three percentage points commercial and four technical, on the same original denominator with overlap removed. This is about 2.4% annually compounded on eligible spending before timing. It is not a claim that suppliers can surrender seven margin points.

Existing-model negotiations and running engineering changes can arrive before platform replacement. Conversely, large platform consolidation extends beyond 2028; it cannot be applied to the entire carryover fleet. Suppliers may demand compensation or recover commodity inflation. Cheaper specifications that damage customer appeal are not sustainable savings at unchanged product performance.

**Revision trigger:** an NA bridge separating material price, technical consumption/content, supplier compensation, FX and commodities, plus dated deployment by nameplate. A clean €35bn regional denominator is also missing. Our €30–40bn base sensitivity changes 2028 component benefit by approximately ±€189m; vehicle selling prices do not validate this cost premium.

### Manufacturing: remove paid costs, not merely idle capacity

OPE measures production effectiveness, not cash payroll. Management reported roughly 89% NA OPE and improvement of 870 basis points, while also identifying benefits from higher output. Theoretical hours per vehicle can fall with unchanged total paid hours. We count only lower overtime/agency invoices or actual payroll removal at unchanged reference output. Redeployment and avoided hiring for growth are not reductions in the 2025 bill. [S3]

Labor eligibility of 50% with a 10% reduction equals a mature 5% reduction in the whole loaded labor pool. The remaining spending reflects minimum staffing, fixed benefits, income protections and launch needs. It requires demonstrable changes in paid hours or staffing, not base-wage cuts. UAW wage increases work in the opposite direction; Canadian bargaining remained unresolved in the October 6 union update. No Brampton closure saving is booked. [S7–S9]

Cash-plant eligibility is higher at 70%, with a 12% reduction: purchasing terms, energy consumption, repair frequency and service design can change, but taxes, minimum utility charges, safety and preventive maintenance constrain cuts. Management's predictive-maintenance example supports the mechanism, not the percentage. Underinvestment or new automation could require more spending. No depreciation saving is credited: higher utilization does not reduce annual depreciation, and avoided capex is not immediately an AOI benefit. [S2]

**Revision trigger:** matched-output paid payroll and overtime/agency costs; utility consumption and purchased-service invoices; investment required; and actual agreement terms. Until then, manufacturing remains a conditional €0.34bn contribution, not an OPE-derived calculation.

### Quality: lower expected lifetime cost, not claims count alone

The €3bn reference contains a rounded €0.9bn actuarial remeasurement retained in 2025 AOI. Exclude it from the operational eligibility pool. The base addresses €1.5bn of the remaining €2.1bn, with a 25% reduction and 85% annual recognition in 2028. This implies approximately €304m after the expense allowance. The percentage is judgment, informed by the direction of early-quality improvement, not mathematically derived from 3MIS. [S3, S4]

Stellantis accrues expected lifetime warranty costs when it recognizes the vehicle sale. Thus better new vehicles can lower provision expense before the old fleet has fully left warranty; cash claims can lag. Older vehicles, recall campaigns, severity inflation and revised estimates can nevertheless swamp that benefit. Supplier recoveries must be counted net and once. A fall in repair frequency does not establish the same fall in euros per vehicle.

The 2025 actuarial revision made reserves more responsive to claims experience. The absence of another labelled remeasurement does **not** establish €0.9bn lower expense on future vehicles: revised expected costs may remain embedded. We therefore book **zero automatic normalization in all three operating scenarios**, and show 0/€0.45bn/€0.9bn only as separate conditional sensitivities. Any subsequent credit must be reconciled with operational quality improvements to avoid overlap. [S4]

Ram's 10-year/100,000-mile extension on eligible 2026 US vehicles also increases coverage relative to earlier terms. This is a potential offset to better reliability; it is not a quantified new cost in this forecast. Since the offer began in 2025, only incremental exposure versus the 2025 baseline belongs in future offsets. [S11]

**Revision trigger:** cohort-level new-vehicle warranty accrual per unit, frequency/severity, legacy estimate revisions, recall expense, supplier recoveries and coverage changes. 3MIS alone is insufficient. May's 44% and Q2's 38% NA improvements use different production-cohort windows and are not a clean sequential deterioration series.

### Logistics and indirect: credible intervention, unmeasured economics

The May 18 supplier announcement identifies a real NA ICL/Agillence project for multimodal routing, dealer delivery and port/vehicle-processing-center constraints. It reports no savings amount. This corroborates implementation, while remaining a vendor's account rather than independent outcome measurement. [S10]

The base assumes 60% eligible and a 12% reduction over the horizon. One perimeter interpretation is 70% of the €1.5bn logistics estimate plus 45% of the €1bn eligible-indirect allowance. Carrier commitments, service standards, fuel surcharges and migration costs constrain savings. We do not treat all SG&A, advertising or IT as reducible. Discounts, fewer vehicles and lower inventory are not routing efficiency.

Stellantis's older European logistics program is counterevidence to treating every logistics improvement as newly created by VCP: it had already targeted substantial reductions before the 2025 baseline. Its percentages are neither a NA benchmark nor an additional 2026–28 saving. [S12]

**Revision trigger:** transport cost per comparable shipment/distance, expedited-freight frequency, load factors, warehouse invoices and service performance, plus net migration fees. Without these, €152m remains a scenario allowance.

## Guidance reconciliation and external offsets

Management's global €6bn target is against 2025 and described as an annual run rate by 2028; the NA presentation identifies more than €3bn. May financial materials separate VCP from utilization and nonrepeat 2025 adjustments. Q2 reiterates 40% initiative implementation by end-2026 and €2.4bn global benefit in 2027, expected to flow to AOI. Review/project counts do not independently establish value. One sentence in the public Q2 transcript says “2026” for the €2.4bn; the repeated adjacent statements explicitly say 2027. Use 2027, not an average or a second target. [S1–S3]

Our base 2027 NA benefit of €1.32bn is directionally compatible with NA supplying a substantial part of the global €2.4bn, but this is a comparison, not the construction method. The 2028 target requires more eligible material savings, higher yield, more quality benefit or another identified mechanism than our base assumes. The upside exceeds €3bn primarily through broader material cost-down. Management's €6bn language varies between run-rate and annual-benefit framing; our annual recognition is explicitly defined rather than silently treating those as identical.

Q2 industrial improvement is not a clean validation sample: it combines purchasing, warranty, manufacturing/logistics, volume effects and other changes. A large warranty item was European recall nonrecurrence. Do not annualize the global industrial bridge or allocate it by NA revenue and call it VCP delivery. [S3]

| Separate item | Treatment and scale |
|---|---|
| US contractual wage increases | September 2026 +3% and September 2027 +5%, before COLA. Illustrative calendar weighting gives +10.3% versus average 2025 by 2028, holding the final rate thereafter. Applied only to an assumed wage-sensitive portion of the provisional US pool, this gives roughly €234–277m at unchanged hours. Not a total NA payroll forecast; Canada/Mexico, benefits, progression and future bargaining are unresolved. |
| Commodities, tariffs and FX | Separate bridge assumptions; not inferred from technical savings. No commodity price forecast made here. |
| Pricing/incentives | A one-percentage-point decline on €60.962bn 2025 NA revenue is about €610m. Ten percent of the €2.09bn benefit given back in price is €209m. These are sensitivities, not forecasts. |
| Warranty coverage | Separate from frequency/severity improvement; incremental exposure versus 2025 not quantified. |
| Accounting normalization | No automatic credit. Up to €0.9bn is a conditional upper sensitivity, not a booked saving. |
| Higher volume/mix | Variable cost and savings must scale with appropriate units/content; fixed labor does not scale automatically. Do not call higher fixed-cost absorption VCP. |

The final AOI forecast must include those external effects. They are **unestimated here, not assumed zero**. For payroll, inflation applies to remaining wage-sensitive hours after operational reductions, avoiding the interaction being counted twice. An increase in total cost can coexist with lower cost at constant volume.

## Sensitivities, accounting boundaries and next evidence

At base assumptions, 2028 recognized benefit changes by approximately:

- €189m per one percentage point of component reduction on eligible cost.
- €221m per ten percentage points of component addressability.
- €147m per ten percentage points of component annual recognition.
- €128m per ten percentage points of quality reduction on eligible cost.
- €65m per €1bn change in the logistics/indirect base.

**Do not add overlapping pools:** component prices retain supplier-embedded freight unless explicitly removed; logistics then excludes it. Plant technicians sit in labor, purchased repairs in cash plant. Savings on scrapped component material sit in components; paid factory rework hours sit in manufacturing labor; post-sale claims sit in quality. Supplier defect recoveries cannot enter both component and quality savings. Purchased factory services stay out of indirect overhead. Fixed-cost absorption stays in its chosen volume/industrial bridge location once. None of the €0.9bn potential normalization is also in operational savings.

A classification refinement is needed before workbook population: direct-material, factory and warranty savings generally enter Industrial; eligible back-office/IT savings may enter SG&A. The current architecture's instruction to put VCP in Industrial must not cause the same indirect saving to be included in both lines. Allocate by expense nature; keep total benefit unchanged. This note flags the refinement without modifying the agreed architecture or workbook.

**What changed:** We moved from cost bases to explicit proposed saving rates; rejected treating review coverage or OPE as dollar savings; separated actuarial accounting from sustainable quality improvements; found a named NA logistics project; and incorporated supplier lead times and union constraints. The research supports a credible recovery mechanism, not proof of a durable cost advantage over peers. Much of it repairs prior execution problems; competitive pricing can still absorb the benefit.

**Highest-value next evidence:** an actual NA VCP bridge by material/quality/manufacturing/logistics, supplier price-versus-engineering decomposition, and warranty accrual per vehicle by cohort. A purchasing or plant-finance expert who can distinguish booked invoice savings from volume absorption is more useful than another generic turnaround interview. Without those records, retain ranges rather than expanding into weak proxy collection.

## Memo-readiness review: mechanistic support still required

User follow-up, 14 October 2026: explain and substantiate the economic mechanism behind each denominator, eligible share and saving rate. A lower analyst scenario alone does not demonstrate that management's target is unrealistic. No numbers changed in this review.

| Component input | What actually supports it today | Evidence needed to defend the selected number |
|---|---|---|
| €35bn NA purchase/expense proxy | Global purchases above €88bn; shipment-weighted allocation with an assumed 1.8x NA/rest component-cost ratio. Equal cost per vehicle yields €23.6bn; a 1.5x ratio gives €31.2bn. | Model/powertrain-weighted purchased bill of materials, regional direct-material consumption or a credible comparable-cost benchmark; reconcile purchases with expense and geographic perimeter. |
| €21bn addressable | €35bn multiplied by an assumed 60%. Management's review coverage and supplier lead times constrain the concept, but do not measure the excluded €14bn. | Spend by component family and feasible intervention, contract/rebid dates, sole-source/tooling constraints and validation/launch timing. Do not claim a measured exclusion list exists. |
| 7% reduction | Judgmental three-year commercial-plus-technical scenario. The illustrative three-point/four-point decomposition was not independently estimated. | Price-concession evidence on the correct negotiable denominator, plus quantified engineering projects weighted by affected spend; deduct compensation, tooling/validation expense and overlap. |

The improved method should calculate savings by component family and mechanism, then derive an effective aggregate eligible share and rate. Commodity pass-through, supplier conversion value and technical material-use changes are different economic objects. The same part can support more than one intervention; assign each saving once. Preserve constant performance, volume and mix when attributing benefits to VCP. Independent evidence may support a higher or lower result than the current scenario. This is a research priority, not a retrospective justification of 60% or 7%.

## Historical anchors and simpler proposed method

User direction, 14 October 2026: prefer historical outcomes to unsupported addressability/reduction splits. Keep two factors only where they have distinct evidential support. Otherwise use **one effective savings rate per cost pool**, not a common rate across all pools. The earlier 60% × 7% assumptions imply 4.2% mature gross savings on the entire component pool. Collapsing the formula does not validate that 4.2%.

Five targeted discovery queries covered Renault, GM, Ford and Nissan, followed by selective primary-source checks. Findings:

| Historical case | Company-reported result | Mechanism / relevance | Limitation for STLA calibration |
|---|---|---|---|
| Nissan Revival Plan, FY2000–01 | By May 2002, management reported achieving 20% purchasing-cost reduction; the FY2001 portion was 9%, with ¥245bn accounting benefit. | Supplier-base consolidation, global purchasing, Renault-Nissan purchasing cooperation and engineering-led changes. Parts suppliers reduced 40% to about 700. | Exceptional turnaround, old industry structure, broader purchasing perimeter. Not a transferable annual direct-material rate; no assumption STLA retains the same unexploited opportunity. Figures in the May review were preliminary. |
| Renault, 2024 | €792m cost benefit, attributed primarily to purchasing and partly to favorable raw materials. | Recent procurement execution, useful for gross-to-net and scope reconciliation. | No clean component-purchase denominator or commodity split established in this bounded pass. Do not divide by revenue and label it a purchasing savings rate. |
| Renault, 2025 | Achieved €400 reduction in variable COGS per vehicle; purchasing and initial Horse Powertrain synergies identified. | Recent per-vehicle outcome with a named operating mechanism. | Variable COGS is broader than components; euros per Renault vehicle cannot be applied directly to a different vehicle mix. Future €400 annual ambition is guidance, not further achieved history. |
| Ford Model e, Q3 2024 | $500m year-over-year cost improvement was offset by industry pricing pressure. | Demonstrates why realized operational savings do not establish retained margin expansion. | EV segment and mixed cost scope; not a components percentage benchmark. |

These cases establish that meaningful reductions can occur, while differing scope and exceptional starting conditions prevent a pooled average. Nissan is evidence against assuming that a large target is inherently implausible. Renault offers a more recent operating anchor; Ford supplies counterevidence on retention. GM's broad fixed-cost program was not admitted as a material-cost rate.

**Proposed calculation:** reference cost pool × effective cumulative operational savings rate recognized in each forecast year − incremental AOI execution expense. Annual rates already include deployment/recognition timing; do not apply an additional addressability or timing factor afterward. Keep wage/material-price changes, volume/mix, tariffs and selling-price effects separate. This changes the proposed estimation method, not workbook figures.

Before replacing the placeholder rate, establish comparable scope: component or broader variable cost; annual versus multiyear reduction; realized versus targeted; commodity/volume/mix treatment; and remaining improvement opportunity after earlier programs. A usable rate can be based on normalized comparable outcomes and explicit STLA adjustments. Unsupported numerical discounts to Nissan's 20% would merely recreate the original problem. No new empirically calibrated STLA percentage is claimed from this bounded pass, and the prior scenario is not a validated management-target rebuttal.

Primary sources for this update:

- [Nissan FY2001 business review, May 9, 2002](https://www.nissan-global.com/EN/DOCUMENT/HTML/FINANCIAL/SPEECH/2002/fs_speech20020509.html), NRP update and operating-profit bridge. Achieved results as reported by management, with preliminary-results caveat.
- [Renault 2024 results, February 20, 2025](https://media.renaultgroup.com/2024-results-solid-growth-record-operating-profit-and-net-cash-financial-guidance-exceeded/?lang=eng), Automotive operating-margin bridge.
- [Renault 2025 financial report](https://events.renaultgroup.com/app/uploads/sites/7/2026/02/RG_2025_FY_Results_Financial-Report_EN.pdf), PDF pp4 and15 for achieved €400/vehicle; p6 separates future ambition.
- [Ford Q3 2024 results](https://www.fromtheroad.ford.com/us/en/articles/2024/third-quarter-2024-financial-results), Model e discussion. All retrieved 14 October 2026.

## Source provenance

All accessed/rechecked 14 October 2026. Reported facts are distinguished above from derived arithmetic, peer/supplier observations and analyst assumptions. Original licensed transcripts remain local; no full licensed text is republished.

- **S1 — Stellantis, May 21, 2026 Investor Day:** [financial overview transcript](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Financial-Overview.pdf), pp1–3, plus supplied slide deck full PDF p58 for NA target and finance presentation pp12–13 for cost bridge. [Official event page](https://www.stellantis.com/en/investors/events/stellantis-investor-day-2026). Primary guidance, not independent feasibility validation.
- **S2 — Stellantis, May 21 Investor Day Q&A:** [official transcript](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Q-A-Session.pdf), pp3–5; maintenance, timing and net benefit. Group scope, no NA manufacturing split.
- **S3 — Stellantis, July 30 Q2 2026:** [official call transcript](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-Q2-2026-Financial-Results-Call-Transcript.pdf), pp5–8 and 12–13; original supplied presentation pp5,25,27 for quality cohorts and NA bridges. [Reporting index](https://www.stellantis.com/en/investors/reporting/quarterly-results-materials). Supplied preliminary transcript pagination differs from official publication.
- **S4 — Stellantis 2025 annual report:** [original report](https://www.stellantis.com/content/dam/stellantis-corporate/investors/financial-reports/Stellantis-NV-20251231-Annual-Report.pdf), pp236,284–285,316; warranty recognition, reserve changes and AOI exclusions. Approximately €4.2bn NA remeasurement less rounded €3.3bn excluded gives the approximately €0.9bn retained proxy; do not imply exact precision from rounded values.
- **S5 — Lear 2025 10-K, filed February 13, 2026:** [primary filing](https://ir.lear.com/node/25461/html), pp18,22,44–46; annual price reductions, engineering responses and recoveries. Supplier perspective; no clean concession percentage.
- **S6 — Magna 2026 annual information form:** [primary filing](https://www.magna.com/docs/default-source/financial-reports-public-filings/annual-information-forms/magna-2026-annual-information-form.pdf?sfvrsn=5b103a01_11), printed pp21–22/PDF pp23–24; 2–4-year new-program lead time and pricing/tooling pressures. Does not imply every running change takes that long.
- **S7 — UAW 2023 Stellantis hourly agreement highlights:** [primary wage table](https://uaw.org/wp-content/uploads/2023/11/Stellantis_HourlyHighlighter.pdf), General Wage Increases table. Verified in indexed primary text; direct PDF returned 403, so page number is not claimed. COLA projection is not realized payroll.
- **S8 — Unifor, September 16, 2026:** [membership update](https://autotalks.uniforautohub.ca/stellantis_membership_update_2026_09_16), income-security extension. Union account; actual future cost not disclosed.
- **S9 — Unifor, October 6, 2026:** [bargaining update](https://autotalks.uniforautohub.ca/unifor_moves_to_strike_authorization_votes_at_stellantis), impasse and planned October 17–18 authorization votes. Authorization is not itself a strike.
- **S10 — Agillence, May 18, 2026:** [supplier announcement](https://www.prnewswire.com/news-releases/stellantis-north-america-selects-icl-and-agillence-to-enhance-finished-vehicle-logistics-network-optimization-302775105.html). Named NA implementation and constraints; no quantified result. Interested vendor, not independent measurement.
- **S11 — Mopar/Ram:** [2026 limited powertrain warranty terms](https://www.mopar.com/content/dam/mopar/pdf/warranty/Ram_2026MY_10-100_Limited_Powertrain_Warranty-Jun17v2.pdf), p1; [June 18, 2025 announcement](https://blog.stellantisnorthamerica.com/2025/06/18/ram-brand-announces-americas-best-full-size-truck-and-van-limited-powertrain-warranty-10-years-100000-miles/). Applies to eligible first-owner US vehicles, not all global/fleet sales; do not generalize the perimeter.
- **S12 — Stellantis 2024 Investor Day Europe:** [primary transcript](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2024/transcript/Stellantis-Investor-Day-2024-Transcript-Enlarged-Europe.pdf), p4; earlier European delivery-logistics targets. Excluded as a NA rate benchmark and as new post-2025 savings.
