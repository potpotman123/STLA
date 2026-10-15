# Resolved working assumptions for Fable implementation

14 October2026. User requested resolution of the2026anchor, non-VCPcosts and launch substitution. **Research-only implementation proposal: no spreadsheet edited.** Keep the inspected workbook and independentAIbaseline for variance. This case selects explicit planning assumptions; it does not turn unobservable inputs into reported facts. [Machine-readable inputs, model forecasts and sensitivities](proposal.json); [reproducible calculation](calculate.py).

## Recommended case

|NA output|2026E|2027E|2028E|
|---|---:|---:|---:|
|Shipments|1,580,625|1,529,931|1,618,100|
|Revenue EURm|65,834.1|62,728.4|65,837.1|
|AOI EURm|117.1|−602.0|2,191.7|
|AOI margin|0.18%|−0.96%|3.33%|
|Inspected workbook AOI EURm|−546.6|−248.6|2,963.5|

This is not optimized to produce a bearish conclusion. A better2026anchor is offset by explicit2027costs and a modest launch substitution reserve. 2027weakness reflects lower wholesale shipments, increased support, refund expiry and cost carryover before fullVCP. Do not smooth this away without changing the underlying assumptions. Retain generous9%components,8.3%manufacturing and17%logistics terminal rates and40%/100%recognition2027/28. Warranty and other-indirect savings remain zero credited, not a forecast of zero opportunity.

## 1. New evidence changes the starting-point assessment

**Correction to our previous audit:** [Q1interim report, NA discussion on printedp20](https://www.sec.gov/Archives/edgar/data/1605484/000160548426000041/stellantisnv20260331interi.htm) explicitly attributes approximatelyEUR400mIEEPAadjustment toNA, offsettingQ1tariffcost. The prior claim that regional attribution was unestablished is superseded. H1reportedAOI547m therefore includes this benefit; normalizedH1AOI is147m. This is a profit normalization, not a claim about cash receipt timing.

[Julycall, printedp9](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-Q2-2026-Financial-Results-Call-Transcript.pdf) identifies approximatelyEUR1bn groupH2-versus-H1headwind from raw materials and nonrepeatIEEPAcredit. Removing400m implies roughly600mraw-material pressure. The same call discusses favorable mix/pricing and cost progress, but does not give a regional half-year profit target. We credit no separate unquantified mix/price uplift. We also avoid layering European recall normalization ontoNA.

**NAallocation assumption:**40% of600m=240m additionalH2cost. This uses the rounded35/88estimatedNA/globaldirect-material-purchasing share, not disclosedNAcommodityexposure. Sensitivity25–55% acknowledges different commodities, purchasing scope and hedges. Do not use40% toallocate the separately verifiedNArefund.

**2026forecast construction:**

`H2 AOI = (547 − 400) + (756,625 − 824,000) × EUR5,000 / 1m − 240 = −429.875m`

`FY2026 AOI = reported H1 547 + forecast H2 (−429.875) = 117.125m`

Keep existingQ3preliminary357k andQ4assumed399,625shipments. This extends the user-selectedEUR5kcoefficient to a sequential2026forecast; still an approximation to mix/absorption. HistoricalH1spending levels are the reference, including warranty/regulatory outcomes already reflected there. Do not add the2025warrantycatchup again. The existing equal-quarter2026VCPattribution gives no additionalH2versusH1VCPuplift; its potentialQ4acceleration remains upside rather than an invented new saving.

Quarter construction uses normalizedH1quarterAOI73.5m and412kshipments, with120mraw-materialcost perquarter: Q3AOI−321.5m; Q4−108.375m. Even cost phasing is a convention, not granular guidance. A Q2-onlyconstant-economics anchor would liftFY2026AOI by91m to208.125m at the same volume/raw-material assumptions; it is a sensitivity, not a reason to doubleH1profit. Tariffs beyondrefundexpiry and additionalpricing/mix remain held at the reference environment. This is a transparent forecast, not an identified causal decomposition of every2025cost.

## 2. Resolve remaining cost controls explicitly

|Control|Proposed treatment|Why / limitation|
|---|---|---|
|Tariff refund|−400m2027YoY; zero further2028change|2026reportedprofitcontainsQ1benefit,2027doesnot. H2normalization removes it from the referencehalf, but FY2026stillincludesactualQ1; thus2027nonrepeat is necessary, not doublecounting.|
|Raw-materialcarryover|−240m2027YoY; zero2028newshock|240madditionalcost occurs inH22026; maintaining that pricelevel forfourquarters costs480m2027 versus240m2026. Assume stable late2026commodityprices thereafter, not zero commoditycost.|
|Plantlaborinflation|3%annually2027/28 on remaining estimated laborpool|Planning judgment; established wage/COLA pressure makes flatcost implausible. This is not a contractual3%rate for everyNAworker. USbasewages, benefits, Canada/Mexico and2028renegotiation differ. Sensitivity0–5%.|
|SG&A/implementationreinvestment|Additionalannualexpense200m2027,400m2028 versus2026|Scale anchored to management group−0.6ppSG&Abridge, equivalent to~400m on ourNArevenue. Regional allocation and timing are judgment. Using this as additional expense from2026 is deliberately stronger than simply copying a2025–28groupbridge.|
|R&Dexpense,FX,newtariffpolicies|Hold referencelevel; zeroYoYchange|Explicitneutralassumption, not undisclosedresearch. No dependableNAexpense/FXforecast. Capitalspending is notAOIexpense; do not deductcapex/R&Dspend wholesale.|
|Warrantyoperatingimprovement|No separatecredit|Earlyclaimimprovement doesnotcalibrate lifetimeeurocost; higher new-car accruals and coverage matter.|

Laborcalculation: additionalcost versus no-new-inflationcounterfactual = `(5,500 − recognized labor VCP saving) × ((1.03)^(year−2026) − 1)`. Referencepool is frozenestimated2025, used as a scaleproxy, not rebuiltactual2026payroll. This gives159.522m in2027 and307.149m in2028; YoYdrag159.522m/147.627m. Savings are onreferencewages; inflationapplies toremaininglabor, so the interaction is not countedtwice. Manufacturingbenchmarkallocation to labor remains proportional, not a separatelyvalidatedoutcome.

The200m/400menvelope covers incrementalmarketing and AOI-recognized implementation/training/validation spending together; there is no second execution-cost haircut inVCP. It is an aggregate expensebudget housed inSG&Aforplanning; reclassify identifiableplantcost toIndustrial withoutchangingtotal. One-time restructuring excludedfromAOI, capex and settlements ofoldprovisions remain outside thisenvelope. This assumption is a material judgment: no extraenvelope would increase2028margin to3.94%.

The [financeoverview, pp1–2](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events/stellantis-investor-day-2026/transcript/Stellantis-Investor-Day-2026-FaSTLAne2030-Transcript-Financial-Overview.pdf) alreadyincludesraw-materialandSG&Aheadwinds. Do not subtract its fullgroupbridge on top of ourcontrols. [UAWcontractoverview](https://uaw.org/stellantis2023/) supports wagepressure, not our preciseall-inrate; a linkedsummaryPDFwas403blocked, so no new numerical contractualcalibration isclaimed. The strongest ratefacts remain management disclosures; the rest are planningassumptions with sensitivities.

## 3. Launch substitution: choose a reserve, not a fictional measured rate

Use20%ofgrossnewvolumes for City, newChryslercrossovers,DakotaandcompactRam as a **planningreserve**. This is the previouslydocumentedlower substitution sensitivity, now selectedfor a workingcase. There is no public customer-origin dataset validating20%. Range0–40%; the question is economically important but not worth pretending we can identify the exact rate with weak forum proxies. Do not confuse brandloyalty with cannibalization: anexistingowner replacing anoldcar is not necessarily a sale lost from our forecastincumbents.

Keepgrosslaunchrows; subtractdonors once:

|Donor incumbent|2027deduction|2028deduction|Assumed overlap|
|---|---:|---:|---|
|ProMasterlargevan|2,000|2,600|SomeCitybuyers otherwise choose largevan|
|GrandCherokee|1,000|5,000|Half ofChryslercrossoversubstitution|
|Compass|1,000|6,000|Otherhalf ofChrysler; halfcompactRampickupsubstitution|
|RamLD|0|5,000|Dakota4k plusotherhalfcompactRam1k|
|Total|4,000|18,600||

NetUSsales1,350,950/1,412,100; NAshipments1,529,931/1,618,100 withunchangedcountryratios. Model-specificpostdeductionvolumes andprices areinJSON. Quarterdonordeductionsfollow thecorrespondinglaunchquartervolumes, not anextrauniformannualhaircut. Do notdeductfromlaunchrows aswell. Incumbentrecoveryassumptionspreviouslyweregrosswithout anexplicitdonordeduction; iflatermodelresearchalreadyembeds substitution, remove thisreserve ratherthancountit twice. Donorrelationships arehypotheses, notverifiedmigrationflows. Zeroreserve gives2028margin3.43%;40%gives3.23%, lessimportantthanVCPtiming.

## 4. Fable cell-level implementation

Apply against auditedworkbookhash in[priorread-onlyaudit](../workbook-2026-anchor-audit-2026-10-14/README.md); inspectnewversionsfirst. PreserveindependentAItabs. Do notapply newadjustments toalreadyrevisedvalues twice.

1. KeepQ1/Q22026actuals andQ3preliminaryshipments. KeepQ4modelvolumes as thecurrentconditionalforecast; documentD097vintage. Currentpacket doesnotclaimnewQ4modeldiligence.
2. PreserveexistingYoYAOIstructure. In`Model Assumptions!G17:H17`, set−120/−120raw-materialcost. In`G20:H20`, use **408.85/494.85** as explicitlylabeled **aggregate reference-period reassessment**, not identifiedFXorindustrialefficiency. These figurestranslate theindependentlyconstructednormalizedH1forecast into theexistingYoYbridge; theirsum903.7m is not a newlydiscoveredcostsaving. WithcurrentVCP99.65mperquarter andvolume effects, endingQ3/Q4AOI must be−321.5/−108.375. An adjacentcalculation/note shouldshow theconstruction above. Do not claimtheaggregate rebaseis a sourced line-itemdecomposition. If a descriptivehelper isused, mainbridge canlinkitsresult; never feed from aChecksarea.
3.2027Industrialother(`J17:M17`): Q1−559.8805m (refund400+rawcarry120+labor39.8805); Q2−159.8805m; Q3/Q4−39.8805meach.2028(`O17:R17`):−36.9067875meach. Thesequarterinputs sum to−799.522m/−147.62715m. RefundgoesQ1only; rawcarryQ1/Q2only. Futuretariffrelief remainszero.
4. SG&Aother`J18:M18` and`O18:R18`:−50mperquarter, producing−200mYoY ineachyear. R&DandFXotherfuturechanges remainexplicitzero. The2026aggregate rebase isnot repeatedin2027/28; prior-yearAOIalreadycarriesit.
5. KeepincrementalVCP1195.8m/2391.6m andsupport500/250. Applydonorreductions to`NA Volume Build` LDrow7,ProMaster11,GrandCherokee20,Compass26 viaowningvolumeinputs, preservinggrossversions forvariance. Usefullprecisionderivedcountryshipments, notroundedannualratios.
6. ApplypriorauditannualUSshipmentaggregation andWagoneerSweightedpricingfixes. CurrentJSONrevenue alreadyincludes bothcorrectscope andseparateSpricing. Recalculatesupportusingchangedshipments:−661.9655m2027, +308.9405m2028. Do notretain oldsupporttotals afterchangingvolumes. Supportreference isH12026;2026YoYcarryoveris insideaggregatebaselineassessment, notassertedzeroeconomically.
7. UseJSONannualoutput ascontrol, nothardcodedoutput. Forbaselinevariance: +663.7m2026anchor revision; 2028delta versusinspectedworkbook−771.79915m. Decomposition: +663.7anchor,−400refund,−240rawcarry,−307.14915labor,−400reinvestment,−88.35netAOIeffect ofsubstitution (−93mvolume+4.65msupport). Sumreconciles. Wagoneerallocation changesrevenue, notprofitunderthecurrenteffectivevolume/mixshortcut.
8. Updateassumptionnotes andstatus. Label selectedjudgmentrates asassumed. Recalculate allquarters,regionalmargins,consolidatedlinks andvariance. Do not usefullgroup5%2028target asNAguidance; NA8–10%is2030.

## 5. Warranty resolution and remaining limits

The [FY2025call, printedp16](https://www.stellantis.com/content/dam/stellantis-corporate/investors/events-and-presentations/other-documents/Stellantis-2025-Full-Year-Results-Transcript-20260226.pdf) says only500mrelatingtoH1shouldbeexcluded fromthegroupH2warrantyAOIcharge tothinkabouttheforwardrunrate. That reinforceswhy reversingall900mestimatedNAretainedcharge would bewrong; the500mregionalallocation isnot disclosedhere. Noextra500m/900m isadded. Startingfromrecent2026actualsavoids requiringafabricated normalizationofeach2025warrantyitem. Warranty remains zerocredited until new-vehicleaccrualfrequency/severity/cohortdata support arate.

One-at-a-time2028margin sensitivities: base3.33%;25%/55%NAraw-materialallocation3.60%/3.06%;0%/5%laborinflation3.80%/3.01%; renewed1%annualcomponentinflation2.36%;70%terminalVCPrecognition1.50%. These are notprobabilityintervals. Thefullrecognitioncase remains ambitious. Holdinglate2026commodityprices andtariffpolicy stable is anexplicitneutralcase, not a predictionthatcostrisk disappears.

Research isbounded: reviewedpriorwork, companyquarterlycalls/NAinterimdisclosure, guidance andunioncontext. No bulkcollection oragentdelegation. Arithmeticchecks validateinputs/bridges, notcausality. We have nowprovided explicitworkingchoices andimplementationdirections instead ofunresolvedblankinputs. Remaininglimitations are economicuncertainty; Fable still mustimplement, recalculate andverifytheconsolidatedworkbook. A finalinvestmentconclusion should cite theassumption sensitivity rather than describe thisentirecase asproven.
