# RPU working assumptions for Fable

14 October 2026. User requested reasonable, rounded RPU estimates and bounded tests, with less research depth than the core investment drivers. This is the recommended working case, not reported model-level wholesale pricing. No workbook was edited.

## Use these inputs

- Hold comparable-model pricing before incremental incentive support flat relative to the calibrated H1 2026 reference below.
- **User-approved incentive revision:** additional manufacturer support versus the embedded reference is **€500 per US vehicle in 2027**, tapering to **€250 in 2028**. This is a pragmatic forecast assumption, not observed program spending. Support remains above the reference in 2028. The rationale is support for throughput and launches followed by partial normalization as inventory and product availability improve.
- Apply the same per-vehicle amount in each quarter of the relevant year; do not divide it by four. Canada/Mexico assumptions are unchanged. Test €500 and €1,000 additional US support ABOVE this revised base case.
- Retain [the original unchanged-support case](../research/rpu-working-assumptions-2026-10-14-zero-support-baseline.json) for the assumption-variance bridge. Comparable-model net RPU falls €500 versus reference in 2027 and recovers €250 in 2028, ending €250 below reference. No separate regular-price reduction is assumed; if one is introduced, include it alongside the incentive change so reduced rebates do not create a false margin benefit.
- Canada effective RPU: **€38,500**; Mexico: **€30,000**, held flat. Country price ratios are judgment, not observed averages.
- Use one family RPU for Pacifica/Voyager/LX; do not manufacture a separate trim-price forecast from the estimated sales split.
- New-model effective RPUs are launch scenarios. Recompute the weighted price of each Other/new-model row from its actual constituent volumes. Do not apply a single legacy price to newly added products.
- Leave zero-volume prospective products without revenue; their price scenario does not authorize adding launch units.

## Meaning and calibration

We use **effective RPU**, allocating total regional revenue to shipments. This deliberately simplifies the unsupported split between vehicle and other regional revenue. Set the separate other-revenue/reconciliation forecast to zero under this convention. It does NOT assert that parts or other revenue is economically zero. Do not add those revenues again. If Fable independently establishes a separate non-vehicle revenue forecast, subtract it from the calibration numerator and recalibrate the model RPUs first.

The workbook historical anchors are €61,165m / 1,474,000 shipments = €41,496 in FY2025 and €34,307m / 824,000 = €41,635 in H1 2026. The price ranking was seeded with rounded assumed net USD prices, compared with available brand ATP, older model ATP and selected invoice examples. It was then scaled to the H1 regional anchor using customer-sales weights as a proxy for shipment mix. Canada and Mexico were assumed at 90% and 70% of US effective RPU at calibration, respectively. Their resulting euro prices are then held fixed in the forecast.

Seed prices are **assumptions**, not extracted observations. The initial common scale adjustment is approximately −1.2%; that makes the basket consistent with reported aggregate economics but does not validate each model. FY2025 and H1 fits are calibration, not out-of-sample tests. The ~−0.84% change between the two fitted scale factors is a composite residual potentially reflecting currency, channel/trim mix and other revenue. It is not an observed price cut and must not feed the AOI price bridge as one.

The 1.13 USD/EUR 2025 conversion used to express seed prices is supported by the [ECB annual series](https://data.ecb.europa.eu/data/datasets/EXR/EXR.A.USD.EUR.SP00.A). The common currency scale cancels in calibration. Forward euro prices are held flat as a modeling convention, not a forecast of exchange rates. An explicit FX scenario must be applied once, not both inside RPU and as duplicate revenue translation.

## Why these relative prices are reasonable starting points

- **Ram LD versus HD:** $54k/$65k net seed assumptions place HD above LD, consistent with its heavier-duty/diesel positioning. The Ram brand's December 2025 ATP was approximately $64.6k before consumer incentives, and the older Ram 1500 model ATP was about $62.7k. The precise HD premium is assumed; it receives a sensitivity test.
- **Grand Cherokee/Wrangler:** $45k/$46k net seeds reflect current invoice examples and a mix of mainstream and premium configurations. They are below old shortage-period model ATPs. The invoice examples do not reveal the sales-weighted configuration mix.
- **Minivans:** $43k net seed is below the approximately $47.7k December 2025 Chrysler ATP before incentives. Fleet and entry configurations support a discount to that observation, but its exact size is judgment.
- **Compass/Cherokee:** $30k/$33k seeds preserve their lower market positioning and the returning Cherokee's premium to Compass. Neither is a claimed observed OEM average.
- **Wagoneer:** $70k seed allows for premium configurations above entry invoice examples. Family mix and support are uncertain.
- **ProMaster, Gladiator, Durango and Charger:** seeds use existing positioning and price benchmarks as scale checks; renewal, fleet mix and powertrain changes mean old ATPs are not carried over as actuals.
- **New Chrysler crossovers:** $32k net seed is an assumed blend of lower-priced entrants and a higher-positioned midsize product. It does not assume all three models will sell below $30k. Test ±20% on this price instead of pretending to know the launch mix.
- **Other and runoff products:** rounded low-materiality assumptions; no extensive research justified at present.

Source observations and their limitations are in [RPU evidence](../research/rpu-evidence-2026-10-14.json). Calculated inputs, source snapshots and tests are in [working-case data](../research/rpu-working-assumptions-2026-10-14.json).

## Workbook implementation

1. The table separates the effective reference and net RPU after the approved incentive changes. Enter either the reference plus the separate incentive deduction, OR the already adjusted net RPU; never deduct the same support twice. Historical reported regional revenue/shipments stay actual; historical model-level prices remain estimates or blank, not newly asserted facts.
2. Label the reference period explicitly. The existing reference column is labeled FY2025; do not paste H1 2026 reference prices into it as FY2025 actual prices. Either use a separate reference input or clearly relabel the assumption while preserving historical actual outputs.
3. Current brand incentive levels remain unknown. Use a control labeled **change in manufacturer support versus embedded reference**, set to €500 for each US brand in 2027 and €250 in 2028. These are additions to embedded spending, not absolute incentive levels. If preserving the existing absolute-level design, a separately sourced or explicitly assumed baseline is still required; subtract only changes from it. For a YoY AOI bridge, the per-unit pricing effect is −€500 in 2027 versus the unchanged-support reference and +€250 in 2028 versus 2027; apply appropriate shipment populations and handle volume interaction consistently.
4. Use model volumes to calculate mix. Do not add an extra mix uplift or treat aggregate RPU change as pure pricing in the AOI bridge. Do not substitute the hypothetical shipment count used in sensitivity illustrations for the volume forecast.
5. Round reference model inputs to €500, then deduct the annual support assumption exactly. Do not round away the €250 incentive taper. Recompute weighted RPU from these inputs. Keep formula precision in calculations. Expect small differences from the exact calibrated reference.
6. Q3/Q4 2026 may use these latest reference prices as forecast assumptions until better financial actuals are available. Do not label such estimates actuals. Use each quarter's model sales weights; annual RPU is shipment-weighted.
7. Sensitivity calculations use D098 gross customer-volume scenarios, before cannibalization, and proxy shipment mix with customer mix. They do not override the user's selected volumes. Recalculate when the model builder resolves volume differences.

## Model reference prices and tests

| Model/family | Reference EUR | 2027 net RPU EUR | 2028 net RPU EUR |
|---|---:|---:|---:|
| Ram light-duty pickups including Classic | 47,000 | 46,500 | 46,750 |
| Ram heavy-duty pickups;2500/3500, chassis scope unresolved | 57,000 | 56,500 | 56,750 |
| Grand Cherokee including L and 4xe | 39,500 | 39,000 | 39,250 |
| Wrangler including former 4xe | 40,000 | 39,500 | 39,750 |
| Chrysler Pacifica / Voyager / Pacifica LX | 37,500 | 37,000 | 37,250 |
| Ram Pro Master large van | 37,500 | 37,000 | 37,250 |
| Gladiator | 36,500 | 36,000 | 36,250 |
| Compass | 26,000 | 25,500 | 25,750 |
| Cherokee / returning HEV | 29,000 | 28,500 | 28,750 |
| Wagoneer / Grand Wagoneer combined | 61,000 | 60,500 | 60,750 |
| Dodge Durango | 36,500 | 36,000 | 36,250 |
| Dodge Charger gasoline plus Daytona BEV | 39,500 | 39,000 | 39,250 |
| Other US brands Fiat and Alfa Romeo | 33,000 | 32,500 | 32,750 |
| Dodge Hornet | 24,500 | 24,000 | 24,250 |
| Dodge legacy runoff excluding GLH | 28,000 | 27,500 | 27,750 |
| Ram Pro Master City old runoff and returning midsize van | 29,000 | 28,500 | 28,750 |
| Chrysler Airflow / Arrow / Arrow Cross combined | 28,000 | 27,500 | 27,750 |
| Ram Dakota North American midsize pickup | 32,500 | 32,000 | 32,250 |
| Ram compact / Rampage-based North American pickup | 26,000 | 25,500 | 25,750 |
| Ram large SUV / Ramcharger on2030map | 57,000 | 56,500 | 56,750 |
| Wagoneer S BEV | 48,000 | 47,500 | 47,750 |
| Recon BEV / possible later ICE | 48,000 | 47,500 | 47,750 |
| Dodge GLH possible replacement | 26,000 | 25,500 | 25,750 |
| Legacy Jeep / unlisted residual | 22,500 | 22,000 | 22,250 |
| Chrysler legacy runoff | 28,000 | 27,500 | 27,750 |

### Weighted result

- 2027: approximately €41,001 per NA shipment using rounded reference inputs and revised incentives.
- 2028: approximately €40,642 per NA shipment using rounded reference inputs and revised incentives.

The cheaper-product mix in 2028 more than offsets the partial incentive recovery. These are revenue allocation scenarios, not observed prices.

### 2028 sensitivities

Changes below are versus the revised base, using unrounded reference prices.

| Test | Change in NA effective RPU, EUR/vehicle |
|---|---:|
| Extra EUR500 support per US vehicle ABOVE revised base | -437 |
| Extra EUR1000 support per US vehicle ABOVE revised base | -874 |
| Ram LD and HD relative RPU -10%; no recalibration | -1,412 |
| Ram LD and HD relative RPU +10%; no recalibration | +1,412 |
| Grand Cherokee and Wrangler relative RPU -10%; no recalibration | -886 |
| Grand Cherokee and Wrangler relative RPU +10%; no recalibration | +886 |
| Canada and Mexico RPU -10% | -438 |
| Canada and Mexico RPU +10% | +438 |
| New Chrysler family RPU -20% | -171 |
| New Chrysler family RPU +20% | +171 |

These are assumption stresses, not confidence intervals. At an illustrative 1.6m NA shipments, €100 of RPU changes annual revenue by €160m. Actual revenue must use the independently selected shipment forecast. AOI treatment must separate price, volume and mix effects.
