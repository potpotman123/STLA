# Fable: single Research Support tab

Prepared 14 October 2026. This package consolidates the current NA research inputs, calculations, sensitivity cases and model evidence. It does not manufacture missing consolidated IS assumptions or replace underlying source documents. No workbook has been edited.

## Import files and priority

- `support-data.csv`: searchable long-form export of canonical research JSONs, including historical calibration, assumptions, calculations, model evidence and sensitivities. Preserve `section`, `metric_path`, type and source fields. A null means unknown/unestimated, never automatically zero.
- `model-calculations.csv`: 2027–28 gross customer sales, substitution deductions, net customer sales, assumed wholesale ratio, implied shipments, net effective RPU and revenue by US model row. Units are vehicles, EUR per vehicle and EUR millions as labeled. These are proposed forecasts, not reported model wholesale results.
- `manifest.json`: exact source files, hashes, calculation scripts and evidence notes. Underlying linked dossiers contain primary-source provenance and qualifications.
- `build_support_pack.py`: regenerates exports and checks model totals against current regional forecast; reads research files only.

`CURRENT_CASE` governs the latest proposed net volumes and AOI offsets. `RPU_CALIBRATION` and `VOLUME_EVIDENCE` preserve earlier gross forecasts and evidence; do not add those gross units to current net units. VCP is a conditional benchmark-transfer proposal. Neither inclusion here nor user authorization to investigate makes every AI-selected rate a user-approved investment conclusion.

## Suggested visible tab layout

Columns: A block; B metric/model; C geography; D units; E source period; F 2025A; G 2026 actual/YTD; H 2026E; I 2027E; J 2028E; K calculation; L evidence classification; M source document/page or URL; N repository evidence link; O assumption owner; P caveat/validation status.

1. Definitions, cutoff, version and units. Separate US customer sales from NA shipments, annual savings from incremental savings, actual from estimated quarters.
2. Reported historical anchors: regional revenues, shipments, AOI and model sales. Reuse verified workbook actuals and research provenance. Do not label estimated model RPU or an inferred pickup split reported.
3. US model volume: gross forecast, donor deduction, net sales, growth, launch timing and causal rationale. Keep detailed quarterly allocations from existing volume work where available; annual forecasts alone do not justify equal quarters.
4. Channel/country reconciliation: US 98%/100% shipment-to-sales ratios; Canada 115,000 and Mexico 91,000 shipments; net inventory implication. Net US inventory draw = customer sales minus shipments, not an independently observed dealer-stock forecast.
5. RPU and incentives: calibrated reference by model, incremental support EUR500/EUR250, resulting net RPU; Canada EUR38,500/Mexico EUR30,000. Revenue = shipments × net RPU / 1,000,000. Do not deduct support twice. Reference prices already contain baseline support.
6. VCP: estimated pool × savings rate × annual recognition; quarterly recognition = annual/4; AOI bridge uses year-on-year change in recognized savings. EUR35bn components ×9%, EUR7bn manufacturing cash ×8.3%, EUR1.5bn logistics ×17%. Warranty/other indirect: no quantified savings credited, not no potential. Show historical analogue limits beside rates. Annual recognition 10%/40%/100% is a planning case, not three years of full terminal savings.
7. 2026 AOI anchor: H1 reported 547 minus 400 refund =147 normalized; H2 volume delta at EUR5,000/vehicle and assumed EUR240m incremental raw-material cost. Q3/Q4 aggregate rebases are unallocated estimates, not identified savings. Sources and assumptions in latest resolution README.
8. 2027–28 AOI: prior AOI + volume/mix contribution + support change + incremental VCP − refund expiry − commodity annualization − labor inflation − incremental reinvestment. Show each calculation and annual versus cumulative distinction.
9. Sensitivities and reconciliation: scenario effects, regional revenue/shipments checks, AOI identity, no double counting. Sensitivities are one-at-a-time and not additive.
10. Source index and assumption decision log. Put raw long-form import below these visible sections or in grouped rows within the same tab, rather than presenting 2,698 raw records as the readable model.

## Calculation and provenance rules

- Keep formulas live when implementing in Excel; CSV values are reproducible reference outputs, not an instruction to hardcode derived cells.
- Read `research/forecast-resolution-2026-10-14/calculate.py` for exact ordering, inflation, donor deductions and bridge formulas. All financial figures there are EURm; quantities are units.
- Each numerical input should show reported / derived / proxy / assumed / unknown. The package-level status is not enough to call all entries observed. Preserve embedded `source_types`, model evidence and rationale.
- Remaining non-NA, financing, tax, minority-interest and share-count assumptions must come from separately identified workbook inputs or evidence. This NA support pack does not substantiate those automatically.
- Source artifacts and research calculations are in Git. The user's source workbook and every downloaded licensed PDF are not uploaded by this package; it is not a complete archive of third-party documents.
- For the independent AI comparison use `docs/AI-FORECAST-BRIDGE-TAB.md`. The previous main-workbook comparison in CURRENT_CASE is a version diagnostic, not the independent AI baseline.
