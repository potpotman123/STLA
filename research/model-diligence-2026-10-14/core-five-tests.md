# Five core families: forecast tests

As of 14 October 2026. D093. These tests audit existing proposed assumptions; no forecast or workbook inputs changed. All figures are US customer sales including retail and fleet. Pacifica includes Voyager.

## Concentration and numerical anchors

Together: 877,261 units in 2025 (69.6% of 1,260,344); 697,734 through September 2026 (72.8% of 958,463). These are unit shares, not North American revenue shares.

| Family | 2025 actual | 2026 YTD annualized | Q3 annualized | Trailing four quarters | Proposed 2028 | Monthly required |
|---|---:|---:|---:|---:|---:|---:|
| Ram light-duty pickups | 204,139 | 269,529 | 306,600 | 263,022 | 300,000 | 25,000 |
| Ram heavy-duty pickups | 169,920 | 164,268 | 164,428 | 173,999 | 170,000 | 14,167 |
| Jeep Grand Cherokee | 210,082 | 186,352 | 152,108 | 195,625 | 205,000 | 17,083 |
| Jeep Wrangler | 167,322 | 174,681 | 179,028 | 170,279 | 180,000 | 15,000 |
| Chrysler Pacifica / Voyager | 125,798 | 135,481 | 137,964 | 137,236 | 140,000 | 11,667 |

Annualizations are attainable-pace checks, not independent validation, seasonal forecasts or estimates of household demand. The trailing period is Q4 2025–Q3 2026. Precise observed counts do not make rounded forecast judgments precise.

## Model mechanisms and tests

**Ram light-duty — 300k: current pace supports it; durability remains conditional.** Prior work identifies launch/trim availability problems, powertrain transition and Classic runoff, alongside affordability. Q3 2026 reached 25,550 units/month against the forecast’s 25,000. But trailing sales are only 263,022: the assumption requires retaining recent acceleration, not simply maintaining the past year. Earlier retail recovery preceded HEMI’s return, so HEMI cannot explain the whole rebound. Q3 total LD growth of roughly 73% exceeds reported Ram1500 retail growth of 42%; scope and channel mix must not be assumed identical. Dated factory-order advertisements show dealers soliciting replenishment, while large stocked-vehicle discounts show continued clearance. Neither proves profitable completed reorders. Test fails if sustained comparable-channel sales fall materially below 25k/month after launch recovery or require increasing support. No unique 300k causal estimate is established.

**Ram heavy-duty — 170k: broadly a maintenance case, not a major recovery.** 2025 already delivered 169,920. The trailing year delivered 173,999, whereas YTD and Q3 annualized rates are about164k. Updated powertrain/transmission and serviceability are credible product improvements, not quantified sales effects. Cummins descriptions do not establish lower actual fleet downtime. Ford’s higher Super Duty production is not a comparable measure of customer demand. Retain170k provisionally; do not award an automatic rebound simply because LD is improving. A sustained rate below roughly14k/month would weaken this assumption; commercial and household channels may move differently.

**Grand Cherokee — 200k in2027 /205k in2028: the least settled core case.** Sales were244,594 in2023,216,148 in2024 and210,082 in2025. H1 2026 annualizes to203,474, but Q3 to152,108. Thus200k represents restoration of an observed H1 pace; it does not require the old peak. Management’s shutdown explanation is plausible but lacks a quantified model-level lost-production/recovery bridge. Explorer YTD sales increased17.6% while GC fell about9.4%: a universal segment-demand collapse cannot alone explain the divergence. Product, channel and availability differences prevent a clean causal control. Ended4xe production is verified on the current product page, but its undated timing cannot explain a specific2026 quarter. Existing proposed205k adds5k beyond the200k anchor without separately measured demand evidence; label that as low-confidence judgment. A full post-disruption quarter around50k would support the restoration case, but Q4 is not yet observed as of this report.

**Wrangler — 180k: modest current-rate extension, not restoration of2018.** 2025 delivered167,322; Q3 2026 annualizes to179,028, YTD to174,681. The180k forecast requires15k/month versus14,919 in Q3. Bronco’s record sales challenge the idea that Wrangler should regain its former peak merely because supply improves. Current Wrangler program listings show a $7k bonus restricted to vehicles carrying code49H, with other codes receiving different support. Do not assume every new order receives those economics, stack alternative programs, or infer the tagged vehicles’ age. Retaining sales without increasing stock-specific support would be stronger evidence than clearance volume alone. 4xe exit creates an unresolved customer-retention risk; no unsupported conversion percentage is used.

**Pacifica/Voyager — 140k: best supported by a full year of recent pace.** 2025 delivered125,798; trailing sales137,236 and Q3 annualized137,964.140k is only about2% above these anchors. Voyager-to-PacificaLX regrouping must not create artificial growth. Sienna YTD grew11.7%, versus12.7% for the combined Chrysler family; both are benefiting, so this is not evidence of exceptional Chrysler conquest. New entry positioning supports affordability, but hybrid competition, PHEV exit and fleet exposure remain risks. Historical2019 Pacifica/Voyager excludes Dodge Grand Caravan, so it is not the whole former minivan franchise. No large “return to old demand” uplift is needed.

## Worked affordability check

The October9 broker offer [G1] is a commercial illustration, not a national transaction panel. Its $368 advertised GC payment recomputes to $368.39 using the stated cap cost, residual and money factor. With $3,062 due at signing including the first payment, the effective advertised cost is ($3,062 +23×$368)/24 = **$480.25/month before tax**, with a7,500-mile allowance. It includes $5,250 regional lease cash plus $1,000 bonus cash and a separate $4,800 dealer discount. Dealer discount is not automatically OEM-funded. Removing only the regional cash would add about$229/month under unchanged terms; that is a hypothetical sensitivity, not an observed alternative offer. No matched previous-month offer was available to establish improvement. This establishes how support can sustain affordability, not how many sales it caused.

## Decision and limits

The evidence supports different recovery mechanisms, not one common percentage uplift. Retain existing proposals as provisional research cases; confidence is highest in the minivan pace anchor, weakest in GC’s uninterrupted recovery, and conditional on recent acceleration for LD. Pricing improvement must not be assumed merely because volume improves. No model-level OEM net revenue or national dealer gross-profit series was obtained. Specific next observations are completed fresh-order economics for Ram, post-disruption GC sales, and Wrangler sales with comparable inventory-program eligibility. A wider low-yield web search cannot substitute for those observations.

The five proposed2028 volumes total995k. Smaller Cherokee and ProMasterCity still account for about51k of the wider portfolio’s roughly130k2026–28 increase; concentration in current sales does not eliminate their forecast sensitivity.

## Provenance and reproducibility

Observed histories and previous mechanisms are reused from historical-sales-ledger.json and the Ram/Jeep/Chrysler dossiers in this repository. core-five-tests.json preserves extracted inputs, derived calculations, source labels and the ledger hash. This focused pass adds competitor and offer evidence; it does not count repeated issuer tables as independent corroboration. D093 records the user’s intervention: prioritize five core families and require a mechanistic numerical justification, not simply rounded forecasts.

- [F1] [primary issuer](https://www.sec.gov/Archives/edgar/data/37996/000003799626000184/exhibit99q32026salesrele.htm): Explorer YTD +17.6% to 189210; Bronco Q3 38020 and YTD 114956. Super Duty figure is production, not sales.
- [T1] [primary issuer](https://www.prnewswire.com/news-releases/toyota-motor-north-america-reports-september-third-quarter-2026-us-sales-results-302896251.html): Sienna model-table YTD 84770 versus 75876. Use model table, not slightly different hybrid subtotal.
- [G1] [broker commercial offer; not executed transaction](https://www.reddit.com/r/autocompanion/comments/1x2kikf/jeep_grand_cherokee_lease_deals_finance_rates/): October 9 Northeast Laredo Altitude example: MSRP48000, dealer discount4800, bonus1000, regional lease cash5250, cap36950, residual31200, MF.00189,24months,7500mi/year; advertised368/month,3062DAS including first payment.
- [W1] [dealer advertised manufacturer programs; compatibility unverified](https://www.cabledahmercdjr.com/manufacturer-specials.aspx?make=Jeep&model=Wrangler&sc=1&sf=1&type=cash&year=2026): 2026 Wrangler select-inventory bonus41CTU3 $7000 requires sales code49H; other codes carry different amounts. No stacking, age or national average inferred.
