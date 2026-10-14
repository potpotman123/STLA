# Stellantis volume forecast audit

Current research proposal: **D098, 14 October 2026**. This supersedes D097's forecast methodology, not its preserved source observations. No independent AI baseline or workbook has been edited.

- [Audit and model-by-model underwriting](audit.md): findings, numerical constructions, scenarios, price/mix implications, management comparison and limits.
- [Proposed model inputs](proposed-forecast-inputs.json): 25 rows, historical sales, prior and proposed values, reasons and source IDs.
- [Assumption audit](assumption-audit.json): which old assumptions were retained, revised or rejected.
- [Quarterly scenarios](quarterly-scenarios.json): selected observed seasonal patterns and explicitly assumed launch ramps. Other quarters remain unpopulated.
- [Sources](sources.json), [peer calculations](comparisons.json), [limited historical anchor check](anchor-backcheck.json) and [validation](validation.json).
- [Preserved baseline manifest](baseline/manifest.json): immutable copies and hashes of the prior research inputs for the variance bridge.

The gross central cases are 1,354,950 US units in 2027 and 1,430,700 in 2028, **before launch-related losses from incumbent models**. They are not final net company forecasts. The 2028 change versus the old incomplete subtotal comprises a 68,100-unit reduction in previously quantified rows and 80,700 units newly allocated to previously blank rows. Newly allocated is not synonymous with incremental customer demand.

The new Chrysler, Dakota and compact Ram contributions are conditional launch scenarios. Chrysler timing has direct management support, but individual arrival dates, achievable volumes and substitution remain uncertain. The compact Ram estimate and undated optional launches have especially weak magnitude support. Do not describe the entire forecast as independently validated or fully underwritten.

The same US reporting scope reconciles to 1,260,344 vehicles in 2025, 958,463 through September 2026 and 324,277 in Q3 2026. Canada/Mexico retain the prior flat placeholders; no complete North American shipment or revenue forecast is implied.

Reproduce the calculations with `python3 build-audit.py` from this directory. Its checks confirm arithmetic and source snapshot preservation, not forecast accuracy.
