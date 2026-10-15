# Current workbook: 2026 starting forecast and Fable implementation instructions

**Subsequent resolution:** [new assumption packet](../forecast-resolution-2026-10-14/README.md) supplies the workingcase. It also corrects thisaudit's uncertainty aboutNArefundallocation: Q1interimreport'sNAsection explicitly locates theEUR400mIEEPAadjustment there. Preservebelow asoriginalaudit,notcurrentimplementationguidance.

14 October 2026. **Read-only audit; no spreadsheet edited, saved, exported or recalculated.** User delegates workbook implementation to Fable. This note supersedes the previous claim that the current workbook lacks a2026 starting forecast. The downloaded file has advanced since the earlier audit.

Source: `/Users/kwu/Downloads/FINAL KW STLA MODEL.xlsx`. SHA256 `b30afe31bac76bcd0fd59d8976cce8e1ba77e951115e0d72f96a2073224c13dc`. Hash unchanged before/after inspection. [Selected formulas, inputs and cached values](inspection.json); [read-only extraction and independent arithmetic](inspect_workbook.py). No proprietary source documents or workbook binaries uploaded. If Fable has a different version, locate rows by labels and reconcile differences before applying instructions.

## What is already populated

| Current main-model results |2026E|2027E|2028E|
|---|---:|---:|---:|
|NA shipments|1,580,625|1,533,851|1,636,700|
|NA revenue, EURm|65,834.1|62,871.8|66,526.2|
|NA AOI, EURm|−546.6|−248.6|2,963.5|
|NA margin|−0.83%|−0.40%|4.45%|

Locators: `NA AOI Bridge` rows6,8,31,32, columnsH/M/R. Cached outputs are inspected, and key AOI arithmetic independently reconstructed; this is not whole-workbook Excel-engine validation. Existing checks passing does not validate economic assumptions.

The workbook already implements the current2027/28 volumes, support taper, fixed-reference price interaction and VCP schedule. Do not reapply our EUR3.212bn2028 uplift: it is already in the workbook. Its2027 uplift is onlyEUR298.0m: −233.870m volume/mix −663.9255m support +1,195.8m VCP. Starting at−546.575m produces−248.5705m; adding2028uplift3,212.0955m produces2,963.525m.

## 2026 source and assumption classification

- Q1/Q2 NA shipments379k/445k, revenueEUR16,114m/18,193m, AOI263m/284m: main-model historical anchors; retain actuals. H1AOI547m.
- Q3 shipments357k: verified against [October13 official preliminary shipment release](https://www.stellantis.com/en/news/press-releases/2026/october/stellantis-reports-q3-2026-estimated-consolidated-shipments-of-1-3-million-units-down-1-percent-year-over-year). It reports−47k YoY and production shutdowns. Preliminary shipments are not Q3 financial results. `NA Volume Build!F77` reads `NA_Quarterly!J8*1000` from the AI-section historical/preliminary source.
- Q3 revenueEUR14,889.8m andAOI−610.35m are forecasts, not reported results.
- Q4 shipments399,625 equal modeled customer sales, using100%country conversion (`Model Assumptions!H65:H67`). US343,400; Canada/Mexico combined56,225. Model overrides remain fromD097, while2027/28were updated toD098; `NA Volume Inputs!A181` explicitly says so. This is a documented mixed forecast vintage, not a new independently researchedQ4case.
- Q4 US overrides in `NA Volume Inputs!G49:G75`: RamLD75k,HD47k,ProMaster15k; GrandCherokee45k,Wrangler43k,Gladiator12k,Compass15k,Cherokee13k,Wagoneer14k; minivans35k; Durango24k,Charger4.5k,Hornet100,otherbrands800. Minivan split is a proxy; total35k is the relevant demand input. Do not relabel individual allocations reported.
- Q4 revenueEUR16,637.24m andAOI−483.225m are forecasts.

## Main finding: the starting profit assumption needs review

`NA AOI Bridge!F31` = prior-yearQ3AOI−475 −235volume +99.65VCP +0other = **−610.35m**.

`NA AOI Bridge!G31` = prior-yearQ4AOI−471 −111.875volume +99.65VCP +0other = **−483.225m**.

Together H2AOI is−1,093.575m, compared with H1actual+547m. TheEUR5,000 contribution coefficient is extended toQ3/Q42026 as an AI choice (`Model Assumptions!T14`); the user selection originally covered2027/28. `G17:H20` explicitly uses zero placeholders for non-VCP industrial, SG&A, R&D andFX/other. Thus old costs are carried forward unchanged YoY, including any adverse items not separately normalized. Zero change does not mean zero cost. A severeH2result is not automatically wrong, but is not established just by shipment weakness.

**Reference test, not replacement forecast:** hold H1 economics and all non-volume conditions constant. H2shipments756,625 versus824,000 inH1 gives−336.875m atEUR5,000. H2AOI would be547−336.875=**210.125m**. No extra VCP added because existing schedule assumes identical quarterly attribution inH1/H2. Difference versus workbookH2 is**EUR1,303.7m**. If only that starting-point difference flowed through unchanged later bridges,2028AOI would beEUR4,267.225m, or6.41%, rather than4.45%. This demonstrates anchor sensitivity, not evidence to select6.41%. Seasonality, pricing, tariffs, inflation, mix, launch costs and attribution may invalidate frozenH1economics.

**Recommended Fable action:** preserve the current2026 case as a comparison, retain the YoY main bridge, and add a clear explanation/sensitivity for theH2 anchor. Do not replace the2026 AOI with twiceH1 or the sequential test. Establish the non-VCP movements relative to2025 before calling it a fully supported central forecast. Label zero placeholders as economically unestimated; if the model needs numeric values, visibly identify the flat-change convention instead of presenting it as evidence.

## Specific implementation queue

### 1. Correct annual US shipment aggregation (confirmed formula inconsistency)

`NA RPU Build!M285` currently uses annual country mix fallback because the annual ratio control is not numeric. It returns1,331,427.28, while its four forecast quarters sum to1,327,851, the intendedUS98%conversion. Difference3,576.28units.

Use annual sums consistently: `H285=SUM(D285:G285)`, `M285=SUM(I285:L285)`, `R285=SUM(N285:Q285)`, with existing missing-input guards. Verify all three annual columns. **Do not change row286price totals:** they already sum correct quarter-level effects, giving−663.9255m/+306.2505m. This displayed annual helper error currently does not alter those totals.

### 2. Preserve separate Wagoneer S economics inside the combined row

The workbook groups600WagoneerS units with55,000Wagoneer/GrandWagoneer units. Research inputs price S atEUR48,000 before support and the conventional family atEUR61,000. The aggregate uses the higher reference across all55,600vehicles, explaining the exact revenue difference from the reconciled research: **EUR7.644m2027 andEUR7.800m2028**.

In the existing Wagoneer-family block beginning row107, use a forecast-only weighted pre-support RPU `(55,000*61,000 + 600*48,000)/55,600`, or the corresponding live underlying mix; then deduct support once. Do not change historical observations or reclassify this as a list-price cut. Keep the workbook's compact row structure. Expected NA revenue after only this correction: **EUR62,864.130m2027; EUR66,518.425m2028**. No separateAOIprice penalty: this is model-mix allocation, already approximated by the volume/mix coefficient. AOI numerator unchanged under existing architecture.

### 3. Repair reference-period descriptions and price carryover treatment

`NA RPU Build!A283:A289` saysFY2025reference, but the approved support change is relative to the embeddedH12026price environment. Correct labels to the approved reference. Q3/Q42026price formulasF286/G286 take current incremental support deviation only; withzero deviation they producezero. That does **not** demonstrate zero YoY pricing versus2025. Do not add fullH1price benefit123m automatically either. Record2025-to-H12026carryover as unresolved for theH2YoYbridge, distinct from2027/28incremental support.

### 4. Keep VCP history attribution explicit

`VCP Build!F52:G52` usesQ42026as a proxy for unreportedQ1/Q22026savings attribution. This matches our10%annual placeholder mathematically, but is not actual quarterly attribution. Preserve disclosure. H1reported industrial improvement745m includes many items and must not be relabeledVCP. All2027/28incremental figures already match research; no re-addition.

### 5. Preserve historical totals and disclose model calibration residuals

`NA RPU Build!C260:E260` shows modeled-minus-reported revenue of−496.534mFY2025,−358.837mQ12026,+310.404mQ22026. MainIS/bridge historical revenue uses reported values, so these residuals do not presently overwriteactuals. Show the residual as estimated model-allocation error, or perform an explicitly labeled historical calibration. Do not invent parts/service revenue or infer pricing from it. Do not silently recalibrate forecast references to eliminate a historical error.

### 6. Keep the independent AI model separate

AI-section `NA_Quarterly!L28` forecasts2026AOI+647.34m, unlike the main case−546.575m. Its H2bridge in `NA_AOI_Bridge!B16:B25` uses a different coefficient and explicit mix/pricing/cost assumptions. These are comparison inputs, not approved substitutes. In particular its−400mrefund normalization allocates the entire disclosedgrouprefund toNA; regional attribution is not established. Do not import this figure as verifiedNAexpense. Preserve the independent baseline and record any main-case changes for the Point72variance bridge.

### 7. Remove stale implementation notes, without changing the underlying assumptions

`NA Volume Inputs!A182` says shipment ratios remain blank; they are populated. Update the note. The mainISannotation saysH1shipments exceededcustomer sales by55k; mainvolume rows showFY2026difference55,519 andQ3difference−22,599 withQ4zero, implyingH1difference78,118. Correct timing, and retain scope caveat: shipments−customer sales is not automatically a pure dealer-stockchange.

## Offset evidence Fable should retain

[July2026 release](https://www.stellantis.com/en/news/press-releases/2026/july/second-quarter-2026-financial-results) guidesgroup2026nettariffcostEUR1.0–1.2bn, versusH1EUR0.3bn includingEUR0.4bnrefund. ImpliedH2groupcostEUR0.7–0.9bn is a directional challenge to frozenH1costs, not anNAallocation. It saysH2weightedtoQ4; this does not guaranteepositiveNAprofit or validate any particularQ4number. Old-charge cash payments are not automatically currentAOIexpense. [Prior offset audit](../na-aoi-reconciliation-2026-10-14/README.md) retains inflation, SG&A and timing evidence and explicit unknowns.

## Validation for Fable after implementation

Preserveactuals andAIbaseline; reconcile selected2026AOI to quarterlybridge; confirm2027/28rollforwards; sum annualUSshipments fromquarters; reconcile correctedcountryrevenue; deduct supportonce; separate pricecarryover from mix; preserveVCPyear-to-year telescoping; showmissingassumptions rather than a falselycompleteforecast. Recalculate andinspectoutputs in the spreadsheetengine. Our read-only checks do not replace that step.

Stop short of choosing a preciseH2normalization uplift without evidence. The next substantive research question is which2025industrial/priceheadwinds persist or reverse inH22026, not whether we need a new starting-forecast architecture. All readily identifiable implementation fixes and open assumptions are recorded above forFable.
