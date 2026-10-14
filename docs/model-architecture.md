# Stellantis model architecture

Agreed with the user on 14 October 2026; VCP method revised at the user's direction the same day. This is the implementation specification for the research-informed model, not a populated forecast. It supersedes earlier proposals for configuration splits, country inventory schedules, target days' supply, VCP implementation curves and unsupported addressable-share × eligible-reduction assumptions.

## Scope and conventions

- Seven tabs, with quarterly forecasts through 2028 and annual summaries. Include 2025 actuals and earlier operating history where available and useful.
- Mark reported actuals, company preliminary estimates, derived figures, modeled estimates and assumptions separately. Missing data is unavailable, not zero.
- Use EUR millions for financial totals; explicitly label vehicle units and per-vehicle prices. Convert currencies consistently.
- Flow: customer sales -> inventory change -> wholesale shipments -> net pricing -> revenue -> AOI -> consolidated earnings.
- No forecast assumptions have been populated or approved by this specification.

## 1 Historical data and sources

Store quarterly US model sales; aggregate Canadian and Mexican customer sales; reported regional consolidated shipments, revenue and AOI; reported AOI bridge movements; observed dealer inventory; consolidated financials; management targets and definitions.

Record source URL, publication and collection date, page/table, units, period, geography and input classification. Preserve reporting restatements and do not fabricate quarterly financial actuals from half-year disclosures.

## 2 Customer sales inventory and shipments

Use US model/family blocks: Ram light-duty pickups, heavy-duty pickups, ProMaster and relevant new models; major Jeep models; Chrysler minivans; Dodge models; other brands and runoff needed to reconcile totals. Final row coverage must reconcile to reported sales. No trim or affordable/premium configuration split.

Rows for each model/family:

1. Customer sales, generally retail plus fleet.
2. Year-over-year growth: calculated historically, an input for forecasts.
3. Beginning dealer inventory.
4. Inventory increase/decrease: explicit forecast input.
5. Ending dealer inventory = beginning inventory + inventory change.
6. Wholesale shipments = customer sales + inventory change, on a matched scope.

New models use a quarterly unit ramp rather than growth from zero. Starting model inventory allocations are estimates constrained to observed aggregate inventory where available. No required days'-supply input; it can remain an optional diagnostic. Supply constraints can override normal delivery assumptions only where specifically warranted.

Canada and Mexico each get one customer-sales row with a simple flat growth assumption, not separate country schedules. Initially assume zero inventory change for those countries and identify this assumption. Combine with US modeled shipments; disclose any remaining geographic, channel, transit or reporting-scope differences.

Reported regional shipments override modeled historical shipment totals. Do not change known shipments merely to satisfy an assumed inventory roll-forward. Inventory can instead be a reconciliation/check, subject to matched definitions.

## 3 Prices incentives and North American revenue

For each US model/family:

1. Wholesale shipments linked from Tab 2.
2. Estimated pre-incentive wholesale revenue per vehicle.
3. Forecast price change.
4. Manufacturer-funded incentives per vehicle.
5. Net revenue per vehicle = pre-incentive price minus incentives.
6. Model revenue = shipments times net revenue per vehicle.

Canada and Mexico each use an aggregate revenue-per-vehicle assumption alongside their single volume row. Sum vehicle revenues, add an explicitly identified other-revenue/reconciliation estimate, and reconcile to North American reported revenue. Calculate aggregate regional revenue per shipment as a diagnostic.

Changing model weights captures model-mix effects automatically; do not add another mix uplift. Within-model configuration mix stays embedded in the average-price assumption.

Model wholesale prices and incentive costs are generally estimates, not disclosed actuals. Calibration to regional revenue does not independently validate each component. Do not substitute MSRP or dealer advertised prices for manufacturer revenue. Do not subtract incentives again from a price already net of incentives. Dealer-funded discounts do not automatically reduce manufacturer revenue. Check the accounting classification of finance support before treating it as a revenue deduction.

## 4 VCP savings

Four management workstreams: components/direct materials; manufacturing/transformation; quality/warranty; logistics/indirect costs.

User-approved manufacturing subgroups (14 October 2026):

| Subgroup | Annual cost base | Reduction assumption / recognition |
|---|---|---|
| Plant labor | Eligible production staff, supervisors, plant engineering, contractor labor and overtime | Sustainable reduction in actual expense; payroll anchor alone is not reported factory labor cost |
| Maintenance, energy and other cash plant costs | External maintenance, spare parts, utilities, consumables and eligible site overhead | Separately assessed reduction for this combined subgroup; exclude labor already above and costs assigned to other VCP workstreams |
| Depreciation | Eligible annual factory equipment, buildings and tooling depreciation | Recognize reductions only with an identifiable asset/depreciation mechanism; no automatic efficiency haircut |

Use the seven rows below for each subgroup, then sum their recognized savings into one manufacturing subtotal. The workbook uses the annual NA reference cost pool; global anchors and NA allocation calculations remain in research support, with source/status attached. Unsupported bases remain blank / not estimated, not zero. The disclosed global machinery and building depreciation amounts are research anchors, not approved factory-only or NA inputs. Maintenance employee costs belong in labor once; external servicing and replacement parts belong in cash plant costs once.

Machinery purchases are capital expenditure, not an immediate AOI expense reduction. Higher-volume fixed-cost absorption is tracked separately from VCP same-volume efficiency. Do not translate the OPE improvement into an equivalent percentage cost reduction.

For each category and forecast year:

1. Total annual NA reference cost pool, with a consistent baseline year (initially 2025).
2. Effective cumulative operational reduction recognized in that year, as a percentage of the entire reference pool.
3. Annual operational saving = reference pool times effective reduction.
4. Incremental execution/transition expense recognized in AOI, if not already included in the effective rate.
5. Annual recognized net saving = operational saving minus execution expense.
6. Quarterly recognized net saving = annual recognized net saving divided by four.
7. Incremental year-over-year saving = current-period net saving minus comparable prior-period net saving.

One effective rate per cost pool is the approved default. Do not use the same rate across different workstreams. The rate already incorporates annual delivery and accounting recognition; do not multiply it again by an addressable share, implementation fraction or recognition haircut. Two-stage decomposition may remain in research support only if the two inputs have distinct evidence. Merely converting the old components assumption of 60% × 7% to 4.2% does not validate it.

Anchor replacement rates to comparable achieved historical outcomes, with explicit judgments for scope, starting efficiency, product mix, existing supplier relationships and execution capability. Preserve reported versus targeted, gross versus net, annual versus cumulative, and cost-pool versus revenue denominators. Do not treat an old turnaround outlier as an industry average. Peer cost-per-vehicle comparisons must match purchasing/expense scope, production versus wholesale units, currency/period, vehicle content and make-versus-buy boundaries. Missing comparable component costs remain unknown; broader COGS is not a substitute.

Rates can be presented as cumulative full-year effects relative to 2025. A 2028 rate of 5% means a 5% saving against the reference pool in that year, not an additional 5% cut on top of 2027. If a benchmark is already net of execution costs, identify that status and do not deduct those expenses again. Accounting normalization and external wage/material inflation, tariffs, FX and selling-price/incentive changes remain outside operational VCP rates.

No implementation curve, quarterly cost-exposure weighting, seasonality or separate annualized-run-rate forecast schedule. Annual reduction assumptions may differ across years. Equal quarterly allocation is an explicit simplification, not management guidance.

Use a defined cost baseline and identify savings already embedded in the starting financials. Cost bases are reported where available and otherwise labeled estimates. Distinguish global from North American savings; only the NA portion feeds NA AOI. Retain management targets as comparison points with original definitions: a run-rate target is not automatically savings recognized throughout the year. Avoid counting lower activity as an efficiency saving.

## 5 North American financial summary and AOI bridge

Rows:

1. North American net revenue, linked from Tab 3.
2. Consolidated shipments, linked from Tab 2.
3. Revenue per shipment.
4. Prior-year comparable-quarter AOI.
5. Volume & Mix.
6. Vehicle Net Price.
7. Industrial.
8. SG&A.
9. R&D.
10. FX & Other.
11. Current-quarter AOI = prior-year AOI plus bridge movements.
12. AOI margin = AOI divided by revenue.

Use the reported bridge categories, not an invented detailed regional expense statement. Volume/mix profit effects still require contribution assumptions even though model mix already affects revenue. Pricing/incentive effects must be consistent with Tab 3. Map incremental VCP savings once by expense nature: materials, manufacturing, warranty and relevant logistics generally enter Industrial; eligible back-office/IT savings may enter SG&A. Do not also place those indirect savings in Industrial. Other bridge effects remain separately explainable.

The June 2026 6-K provides revenue reconciliation and net-profit-to-AOI reconciliation, not a full NA revenue-to-AOI expense breakdown. Its Q2 NA revenue is EUR18,193m and AOI EUR284m. Their difference, EUR17,909m, is a derived net adjusted operating-cost residual, not disclosed materials, manufacturing, logistics, SG&A or R&D expense. SG&A/R&D in the year-over-year AOI bridge are movements, not absolute costs.

## 6 Consolidated quarterly income statement

Rows: revenue by reported region/segment; consolidation adjustments where applicable; consolidated revenue; cost of revenues; gross profit; SG&A; expensed R&D; other operating items; reported operating income; net financial income/expense and other applicable items; pretax profit; tax; net income; noncontrolling interests and applicable shareholder adjustments; common-shareholder income; diluted shares; EPS.

Use simpler revenue and AOI assumptions for regions outside North America, without replicating the US model-level build. Reconcile regional AOI to consolidated reported operating income. Do not forecast two inconsistent operating-profit totals; label any derived balancing cost line. Annual revenues/profits sum quarters; margins and EPS use appropriate annual denominators.

## 7 Baselines revisions and variance bridges

Keep the supplied illustrative benchmark, independently generated AI first pass, and user-revised model distinct. Preserve the independent AI workbook unchanged even if it uses a different architecture. This jointly designed architecture is research-informed and must not be described as an unaided AI baseline.

Compare customer sales, inventory changes, shipments, prices/incentives, VCP savings, NA revenue/AOI and consolidated earnings/EPS. Show baseline, revised figure, difference, evidence and financial impact. Use a fixed bridge order and explicit interaction treatment so changes reconcile exactly. Do not invent human revisions.

## Q3 2026 shipment inputs

Source: Stellantis 6-K dated 13 October 2026, Exhibit 99.1, PDF pages 3-4, inspected 14 October 2026. Company-reported estimates are unaudited and subject to adjustment. Units below are thousands.

| Region | Q3 2025 | Q3 2026 |
|---|---:|---:|
| North America | 404 | 357 |
| Enlarged Europe | 534 | 588 |
| Middle East and Africa | 95 | 75 |
| South America | 252 | 251 |
| Asia Pacific | 16 | 15 |
| Group | 1,300 | 1,286 |

North American nine-month shipments = 824 H1 + 357 Q3 = 1,181 thousand. Full-year 2026 shipments = 1,181 thousand plus Q4 forecast. Q3 revenue and AOI remain estimates unless a subsequent financial release is available by the model cutoff.

The release gives approximate NA shipment changes: Grand Cherokee -25k, Compass -25k, Ram +17k. These constrain estimates, but are not complete model-level shipment totals. Planned downtime is management's explanation, not independently established causality. Regional totals can differ slightly from the sum of displayed rounded components.

Local source filenames: `Stellantis N.V._6-K_2026-10-13_English.pdf` (Q3 shipments); `Stellantis N.V._6-K_2026-06-30T00_00_00_English.pdf` (Q2 reconciliations); `Stellantis N.V._EP_2026-06-30_English.pdf`, slide 25 (NA AOI bridge). Source documents are not uploaded with this specification. Add verified public URLs when populating the workbook.

## Validation before delivery

- Customer model totals and regional shipment totals reconcile, with scope differences explained.
- Inventory identities hold; no negative inventory without a flagged model error.
- Model revenue ties to regional revenue; price/incentive estimates are visible.
- VCP quarters sum to annual savings and incremental benefits exclude already embedded savings.
- AOI categories contain no duplicate VCP, price or mix effects.
- Regional AOI reconciles to consolidated operating income.
- Quarterly totals, annual margins, EPS, units, FX and variance bridges are checked.
- Missing or weak evidence is labeled rather than hidden in precision.
