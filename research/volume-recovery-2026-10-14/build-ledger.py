"""Rebuild derived research tables from small, frozen public-source inputs.
No network requests; no workbook changes. Run from any directory.
Forecast values are analyst judgments, not results of a statistical fit.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read(name):
    return json.loads((ROOT / name).read_text())
def save(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
raw = read('sales-source-tables.json')
old = read('support/2023-2024-model-sales.json')
peers = read('support/historical-peer-comparison.json')
ram = read('support/ram-quarterly-history.json')

def num(s):
    try:
        return int(s.replace(',', '').strip())
    except (ValueError, AttributeError):
        return None
tables = {}
for key, entry in raw.items():
    table = {}
    for cells in entry['tables'][0]:
        c = cells[1:8] if key == 'fy_2019' else cells
        if len(c) == 7 and num(c[1]) is not None and num(c[4]) is not None:
            table[c[0]] = {'quarter_current': num(c[1]), 'quarter_prior': num(c[2]),
                           'ytd_current': num(c[4]), 'ytd_prior': num(c[5])}
    tables[key] = table
save('normalized-source-observations.json', {'classification':'observed; values copied from source tables, without vintage adjustment', 'tables':tables})

# Sum known children within a family. A missing row is unknown, not a reported zero.
families = {
 'ram_ld':('Ram light-duty pickups',['Ram LD PU']),
 'ram_hd':('Ram heavy-duty pickups',['Ram HD PU']),
 'ram_pickups_unallocated':('Ram pickups, historical unsplit',['Ram P/U','Ram pickups']),
 'promaster':('Ram ProMaster',['ProMaster Van','ProMaster']),
 'promaster_city':('Ram ProMaster City',['ProMaster City']),
 'grand_cherokee':('Jeep Grand Cherokee',['Grand Cherokee']),
 'wrangler':('Jeep Wrangler',['Wrangler']),
 'compass':('Jeep Compass',['Compass']),
 'gladiator':('Jeep Gladiator',['Gladiator']),
 'cherokee':('Jeep Cherokee / returning HEV',['Cherokee','Cherokee HEV']),
 'wagoneer_family':('Jeep Wagoneer / Grand Wagoneer',['Wagoneer','Grand Wagoneer','Wagoneer/G. Wagoneer']),
 'wagoneer_s':('Jeep Wagoneer S',['Wagoneer S']),
 'recon':('Jeep Recon',['Recon']),
 'minivans':('Chrysler Pacifica / Voyager',['Pacifica','Voyager']),
 'charger_family':('Dodge Charger / Challenger transition family',['Charger','Charger ICE','Charger BEV','Challenger']),
 'durango':('Dodge Durango',['Durango']),
 'hornet':('Dodge Hornet',['Hornet']),
 'renegade':('Jeep Renegade runoff',['Renegade']),
 'chrysler_300':('Chrysler 300 runoff',['300']),
 'other_legacy':('Other named legacy models',['Patriot','Town & Country','Dart','Viper','Journey','Caravan','200','Avenger']),
 'fiat_alfa':('Fiat and Alfa Romeo',['FIAT BRAND','ALFA ROMEO']),
}
records = {}
for period, source, field in [
 ('2018A','fy_2019','ytd_prior'),('2019A','fy_2019','ytd_current'),
 ('2025A','fy_2025','ytd_current'),('2024Q4A','fy_2025','quarter_prior'),('2025Q4A','fy_2025','quarter_current'),
 ('2025Q1A','q1_2026','quarter_prior'),('2026Q1A','q1_2026','quarter_current'),
 ('2025Q2A','q2_2026','quarter_prior'),('2026Q2A','q2_2026','quarter_current'),
 ('2025Q3A','q3_2026','quarter_prior'),('2026Q3A','q3_2026','quarter_current'),
 ('2025YTDQ3A','q3_2026','ytd_prior'),('2026YTDQ3A','q3_2026','ytd_current')]:
    t = tables[source]
    records[period] = {k:sum(t[n][field] for n in names if n in t)
                       if any(n in t for n in names) else None
                       for k,(label,names) in families.items()}
    records[period]['reported_us_total'] = next(t[n][field] for n in ['FCA US LLC','STELLANTIS US','Stellantis'] if n in t)
for year in ['2023','2024']:
    t = {r['model']:r['units_'+year] for r in old['rows']}
    records[year+'A'] = {k:sum(t[n] for n in names if n in t) if any(n in t for n in names) else None for k,(label,names) in families.items()}
    records[year+'A']['fiat_alfa'] = sum(old['reported_brand_totals'][b][year] for b in ['Fiat','Alfa Romeo'])
    if year=='2024':
        records[year+'A']['ram_ld']=tables['fy_2025']['Ram LD PU']['ytd_prior']
        records[year+'A']['ram_hd']=tables['fy_2025']['Ram HD PU']['ytd_prior']
        records[year+'A']['ram_pickups_unallocated']=None
    records[year+'A']['reported_us_total']=old['reported_us_totals'][year]
records['2022A_partial'] = {k:None for k in families}
for r in peers['rows']:
    k={'Ram pickups':'ram_pickups_unallocated','Jeep Grand Cherokee':'grand_cherokee','Jeep Wrangler':'wrangler','Jeep Compass':'compass'}.get(r['model'])
    if k:
        records['2022A_partial'][k]=r['units']['2022']
records['2022A_partial']['reported_us_total']=None
for r in ram['quarterly_total_sales']:
    period='2024'+r['period']+'A'
    records.setdefault(period,{k:None for k in families})
    records[period]['ram_ld']=r['LD']['2024_units']
    records[period]['ram_hd']=r['HD']['2024_units']
    records[period].setdefault('reported_us_total',None)
for period, r in records.items():
    r['unlisted_or_reporting_residual'] = (r['reported_us_total']-sum(v for k,v in r.items() if k!='reported_us_total' and v is not None)) if r['reported_us_total'] is not None else None

ledger=[]
for k,(label,names) in families.items():
    history={p:r[k] for p,r in records.items()}
    prev,current=history['2023A'],history['2024A']
    loss=(prev-current) if prev is not None and current is not None else None
    ledger.append({'id':k,'family':label,'source_names':names,'annual_and_quarterly_sales_units':history,
       'share_2025_us_pct':history['2025A']/records['2025A']['reported_us_total']*100 if history['2025A'] is not None else None,
       'share_2026_ytd_us_pct':history['2026YTDQ3A']/records['2026YTDQ3A']['reported_us_total']*100 if history['2026YTDQ3A'] is not None else None,
       '2023_to_2024_loss_units':loss,'share_net_us_decline_2024_pct':loss/223520*100 if loss is not None else None})
# Full historical pickup loss cannot be assigned to LD/HD without the 2023 split.
pickup_loss=444926-373120
notes=[
 'All counts are US customer sales (retail plus fleet), excluding Maserati; they are not wholesale shipments or model revenue.',
 'Null means not separately observed in that source vintage, not zero. Unlisted/reporting residual preserves coverage; it is not a new model or a causal bucket.',
 '2018/2019 and 2023 pickups remain unsplit; do not add the historical unsplit line to LD/HD in other years.',
 'Only selected 2022 models and 2024 quarterly Ram data are populated. Quarterly reporting vintages are retained rather than forced to sum.',
 'Pacifica/Voyager are combined because later 2026 comparative Pacifica figures appear to include Voyager. The exact published classification policy was not obtained.',
 'Charger/Challenger historical family compares the combined outgoing customer footprint with new Charger ICE/BEV and residual Challenger. It is not a claim that all customers transfer.',
 '2026 Q1 Cherokee is a mixed legacy/returning nameplate line; Q2 separates HEV; Q3 lists HEV only. No spurious precise HEV Q1 reconstruction.',
 'Wagoneer and Grand Wagoneer are combined to avoid a misleading label/mix shift. Wagoneer S stays separate.',
 'Fiat/Alfa brand totals are used; all their published models remain accessible in normalized source observations. Historical Grand Caravan stays in other legacy, not current Chrysler minivans.',
 '2023–24 loss weights describe model composition, not causal attribution or revenue contribution.'
]
checks={
 'reported_totals':{p:r['reported_us_total'] for p,r in records.items()},
 'coverage_residuals':{p:r['unlisted_or_reporting_residual'] for p,r in records.items()},
 'ram_pickup_2024_loss_units':pickup_loss,
 'ram_pickup_share_2024_net_decline_pct':pickup_loss/223520*100,
 '2026_q2_published_h1_minus_original_q1_plus_q2':634345-305902-328284,
 '2026_q3_ytd_minus_original_q1_q2_q3':958463-305902-328284-324277,
 '2026_q3_ytd_minus_published_h1_plus_q3':958463-634345-324277,
 '2025_minivan_q3_comparative_pacifica_minus_old_pacifica_ytd':90173-(110006-31642),
 '2025_voyager_ytd_from_fy_less_q4':15792-3983,
 '2026_q1_minivan_combined':21804+3612,
 '2026_q2_h1_minivan_less_q2':67120-41704,
 '2026_q3_charger_combined_yoy_pct':(3679/3014-1)*100,
 '2026_ytd_charger_combined_yoy_pct':(8796/8943-1)*100,
 '2026_q3_jeep_delta':128542-160564,
 '2026_q3_cherokee_compass_gc_delta':(10344+10811+38027)-(131+28086+54553),
 '2026_ytd_us_delta':958463-928023,
 '2026_ytd_ram_ld_delta':202147-143264,
 '2026_ytd_ex_ram_ld_delta':(958463-202147)-(928023-143264),
 '2026_ytd_ex_ram_ld_growth_pct':((958463-202147)/(928023-143264)-1)*100,
}
save('historical-sales-ledger.json',{'as_of':'2026-10-14','classification':'observed source counts; derived family groupings/shares/residuals','notes':notes,'rows':ledger,'period_reconciliations':checks})

# Units below are thousands. Down/base/up are conditional analyst scenarios,
# not probabilities, regression estimates, source forecasts or calibrated intervals.
plans = [
 ('ram_ld',[250,310,350],[260,320,370], 'Recent pace', 'Q3 76,650 x4 = 306,600; YTD annualized 269,529. Base holds the better Q3 pace, then adds only 3% in 2028. Downside loses part of the ramp; upside needs sustained retail growth and mix availability. No separate HEMI or dealer-bonus additive uplift.'),
 ('ram_hd',[155,175,190],[155,180,200], 'Partial normalization', '2025 169,920; Q3 annualized 164,428; 2024 186,107. Base modestly exceeds the 2025 level and stays below 2024 through 2028. Recovery from the 2025 transition is not already proved by a weak Q3.'),
 ('promaster',[50,60,70],[50,63,75], 'Recent pace', 'YTD annualized 58,707; Q3 annualized 65,256; 2025 57,591. Base lies inside current annualized paces; old 2023 81,663 is not mechanically restored. Commercial fleet demand matters.'),
 ('grand_cherokee',[155,205,230],[160,215,245], 'Partial normalization', '2025 210,082; 2024 216,148; current YTD annualized 186,352 and Q3 annualized 152,108. Base assumes planned shutdown/availability effects ease, returning near 2025–24 rather than the 2023 peak. Largest continuing-Jeep supply-versus-demand risk.'),
 ('wrangler',[155,180,190],[155,180,200], 'Recent pace', 'YTD annualized 174,681; Q3 annualized 179,028; 2025 167,322. Base holds about current pace for both years; no restoration of 2019 228,032. Bronco and aging/mix competition cap assumed gains.'),
 ('compass',[40,65,85],[40,70,90], 'Constrained partial recovery', 'YTD annualized 63,783; Q3 annualized 43,244; 2025 101,997. Base starts near the YTD pace, with only limited 2028 recovery. Cherokee expansion and overlapping customers prevent simultaneous full restoration of both nameplates.'),
 ('gladiator',[35,43,55],[35,45,60], 'Recent pace', 'YTD annualized 41,259; Q3 annualized 47,644; 2025 56,790. Base lies within current paces; 2025 rebound is not a reliable full-year new baseline after renewed 2026 decline.'),
 ('wagoneer_family',[40,55,65],[40,58,70], 'Recent pace', 'YTD annualized 56,856; Q3 annualized 49,980; 2025 combined 45,040. Base broadly holds YTD scale with small additional growth. Label consolidation and high-price demand/incentives remain risks.'),
 ('cherokee',[30,60,80],[40,80,110], 'Conditional launch judgment', 'Q3 HEV 10,344 = 3,448/month; base requires 5,000/month in 2027 and 6,667 in 2028. H1 2027 competitive trims are a management plan, not measured conversion. Base is conditional on broader profitable availability. Not an independently calibrated launch curve; never restore old 191k peak automatically.'),
 ('charger_family',[10,20,30],[12,30,45], 'Conditional launch judgment', 'Q3 new ICE+BEV 3,679 = 1,226/month. Base requires about 1,667/month then 2,500/month, supported directionally by ICE rollout but not by order data. Gasoline growth currently offsets BEV decline; old Charger+Challenger 120,858 in 2023 is not assumed recoverable.'),
 ('durango',[70,85,100],[70,85,105], 'Recent pace', '2025 81,168; YTD annualized 81,773; Q3 annualized 91,020. Base is near current scale in both years. New V8 derivatives sit inside this family, not additive launch forecasts; age and price constrain sustained gains.'),
 ('minivans',[115,140,150],[115,145,160], 'Recent pace', '2025 Pacifica+Voyager 125,798; current YTD annualized 135,481 and Q3 annualized 137,964. Base stays close to current pace, then grows modestly. This includes fleet and depends on the apparent Voyager reporting consolidation.'),
 ('promaster_city',[5,10,20],[10,20,30], 'Conditional launch judgment', 'Dealer arrival is planned Q1 2027; old 2019 nameplate sold 12,920. Base requires 833/month then 1,667/month. Different product/use and launch risks make old sales a scale check, not a causal calibration. This is the least secure included base input.')
]
byid={r['id']:r for r in ledger}
forecast=[]
for k,p27,p28,method,rationale in plans:
    h=byid[k]['annual_and_quarterly_sales_units']
    ref=h['2026YTDQ3A']+h['2026Q3A']
    f={'id':k,'family':families[k][0],'classification':'assumed / provisional analyst judgment',
       'method':method,'rationale':rationale,'2025A_units':h['2025A'],
       '2026_flat_q4_reference_units':ref,
       '2026_reference_definition':'YTD actual + Q3 repeated as hypothetical Q4; not a FY actual or approved forecast',
       '2027_units':dict(zip(['downside','base','upside'],[x*1000 for x in p27])),
       '2028_units':dict(zip(['downside','base','upside'],[x*1000 for x in p28]))}
    f['2028_base_growth_vs_2025_units']=f['2028_units']['base']-h['2025A']
    f['2028_base_growth_vs_2026_reference_units']=f['2028_units']['base']-ref
    f['2028_base_growth_vs_2027_units']=f['2028_units']['base']-f['2027_units']['base']
    forecast.append(f)
totals={y:{s:sum(r[y+'_units'][s] for r in forecast) for s in ['downside','base','upside']} for y in ['2027','2028']}
totals['2025_comparable_actual']=sum(r['2025A_units'] for r in forecast)
totals['2026_comparable_flat_q4_reference']=sum(r['2026_flat_q4_reference_units'] for r in forecast)
totals['2025_us_sales_coverage_pct']=totals['2025_comparable_actual']/1260344*100
totals['2026_ytd_us_sales_coverage_pct']=sum(byid[r['id']]['annual_and_quarterly_sales_units']['2026YTDQ3A'] for r in forecast)/958463*100
growth=totals['2028']['base']-totals['2026_comparable_flat_q4_reference']
for r in forecast:
    r['share_2028_base_growth_from_2026_reference_pct']=r['2028_base_growth_vs_2026_reference_units']/growth*100
save('proposed-volume-inputs.json',{
 'as_of':'2026-10-14','status':'research scenarios only; no workbook/baseline edits; no user-approved forecast',
 'scope':'13 US model families, customer retail plus fleet sales. Operating-lineup subtotal, not complete US/NA volume or shipments.',
 'rows':forecast,'totals':totals,
 'unallocated':['Dakota and compact/Rampage North American 2028 launches: month of customer availability and mature sales scale unverified',
 'Chrysler new crossovers: no individual verified customer launch dates',
 'Recon, Wagoneer S, Hornet, Fiat/Alfa and legacy residual: retain actuals; no numerical recovery assumption supported'],
 'country_rows':[
 {'country':'Canada','2023A_rounded':158000,'2024A_rounded':130000,'2025A_rounded':115000,'2027_base_placeholder':115000,'2028_base_placeholder':115000,'assumption':'0% versus last verified FY country baseline; flat convention only, replace with 2026 country exit before workbook admission'},
 {'country':'Mexico','2023A_rounded':97000,'2024A_rounded':94000,'2025A_rounded':91000,'2027_base_placeholder':91000,'2028_base_placeholder':91000,'assumption':'same flat convention; full reported country scope, not US-brand-only Mexico sales'}],
 'country_source':'FY2025 Stellantis Annual Report p17, country sales in thousands, excludes Maserati; sources.json AR25',
 'quarterly_translation':'No fabricated seasonality curve. Hold annual totals as research assumptions; allocate only after settling current-product seasonality and dated customer availability. New 2028 launches need month-specific eligibility; no full-year mature volumes at SOP.',
 'new_launch_accounting':'No separate add-on for HEMI, Rumble Bee, Durango R/T, Trailhawk or Charger ICE; they sit within family forecasts. Cherokee/ProMaster City are gross family sales; replacing outgoing products and cannibalization must be evaluated through the combined portfolio, not deducted again without evidence.',
 'limits':['Scenario bounds are judgments, not calibrated confidence intervals. A base label does not imply a quantified probability.',
 'Flat Q4 reference only makes current exit comparisons visible; growth versus 2025 includes recovery already achieved in 2026.',
 'Jeep Cherokee+Compass+Grand Cherokee base is assessed jointly; no measured customer-transfer coefficient is claimed.',
 'No macro recession/SAAR forecast or price elasticity estimated. Downside/upside are coherent directional operating scenarios, not exhaustive stress cases.',
 'Canada/Mexico flat placeholders are not fresh country forecasts. Adding them to a partial US subtotal does not produce complete North America shipments or financial revenue.']})

periods=['2018A','2019A','2023A','2024A','2025A','2026YTDQ3A']
fmt=lambda x:'—' if x is None else f'{x:,}'
lines=['# Historical model-family sales and coverage','', 'US customer sales, retail plus fleet; units. A dash means not separately established, not zero. Source vintages and quarterly values are in the JSON companion.','',
 '| Family | 2018 | 2019 | 2023 | 2024 | 2025 | YTD Sep 2026 | 2025 US share |',
 '|---|---:|---:|---:|---:|---:|---:|---:|']
for r in ledger:
    lines.append('| '+r['family']+' | '+' | '.join(fmt(r['annual_and_quarterly_sales_units'][p]) for p in periods)+' | '+('—' if r['share_2025_us_pct'] is None else f"{r['share_2025_us_pct']:.2f}%")+' |')
lines.append('| Unlisted/reporting residual | '+' | '.join(fmt(records[p]['unlisted_or_reporting_residual']) for p in periods)+' | — |')
lines.append('| **Reported US total** | '+' | '.join(fmt(records[p]['reported_us_total']) for p in periods)+' | **100%** |')
lines+=['','Every full-year/YTD denominator reconciles after the explicit residual. This is accounting coverage, not equal research confidence across models. The Ram historical unsplit line is populated only when the LD/HD split is absent.','']+[f'- {n}' for n in notes]
lines+=['','## Historical decline composition','',f'2023–24 reported US sales fell **223,520** units. Ram pickups accounted for **{pickup_loss:,} / {pickup_loss/223520:.1%}**; the 2023 LD/HD split remains unavailable. The remaining material contributions are below. Negative values offset the decline. These are unit shares, not revenue or causal weights.','', '| Family | Lost units | Share of net decline |','|---|---:|---:|']
for r in sorted([x for x in ledger if x['2023_to_2024_loss_units'] is not None],key=lambda x:x['2023_to_2024_loss_units'],reverse=True):
    lines.append(f"| {r['family']} | {r['2023_to_2024_loss_units']:,} | {r['share_net_us_decline_2024_pct']:.1f}% |")
lines+=['','## Reconciliation issues','', '- Published H1 2026 total is 159 units above original Q1 plus Q2. Q3 YTD equals the sum of the original three quarterly releases, and is 159 below published H1 plus Q3. Preserve both vintages.',
 '- 2025 YTD Pacifica in the Q3 2026 comparative is 11,809 above old Pacifica FY less Q4; that exactly equals Voyager FY less Q4. Q1 2026 Pacifica+Voyager also exactly reconciles to the later H1 less Q2 minivan figure. Combining the family avoids a misleading nameplate growth signal, but the formal classification explanation remains unverified.',
 '- Quarterly and YTD model rows can differ across releases; missing runoff and minor sales appear in the explicit residual. Do not silently force a per-model quarterly bridge.',
 '- Latest source provides Charger ICE and BEV separately; the older statement that current powertrains cannot be separated is superseded for the disclosed periods. Historical ICE figures still include outgoing Charger, so they are not all new SIXPACK sales.',
 '- Published household/fleet splits are incomplete. No fixed retail percentage is applied to model counts.']
(ROOT/'historical-sales-ledger.md').write_text('\n'.join(lines)+'\n')
lines=['# Proposed annual volume inputs','', 'These are provisional **analyst scenarios**, not reported guidance, statistically estimated demand or approved workbook inputs. Values below are thousands of US retail-plus-fleet sales. Family groupings match the historical ledger.','',
 '| Family | 2025 actual | 2026 flat-Q4 reference | 2027 down / base / up | 2028 down / base / up | 2028 base increase vs 2026 reference |',
 '|---|---:|---:|---:|---:|---:|']
for r in forecast:
    scenarios=lambda y:' / '.join(f'{r[y+"_units"][s]/1000:g}' for s in ['downside','base','upside'])
    lines.append(f'| {r["family"]} | {r["2025A_units"]/1000:.1f} | {r["2026_flat_q4_reference_units"]/1000:.1f} | {scenarios("2027")} | {scenarios("2028")} | {r["2028_base_growth_vs_2026_reference_units"]/1000:+.1f} |')
lines.append('| **Covered-family subtotal** | '+f'{totals["2025_comparable_actual"]/1000:.1f} | {totals["2026_comparable_flat_q4_reference"]/1000:.1f} | '+' / '.join(f'{totals["2027"][s]/1000:g}' for s in ['downside','base','upside'])+' | '+' / '.join(f'{totals["2028"][s]/1000:g}' for s in ['downside','base','upside'])+f' | {growth/1000:+.1f} |')
lines+=['',f'The quantified families represent **{totals["2025_us_sales_coverage_pct"]:.1f}% of 2025 US sales** and **{totals["2026_ytd_us_sales_coverage_pct"]:.1f}% of YTD September 2026 US sales**. This is not a complete 2028 US forecast: future unallocated launches can become material even if current omitted models are small.',
 '', '**Reference convention:** 2026 YTD actual plus Q3 repeated as a hypothetical Q4. This is a transparent comparison device, not a claim about seasonality or an approved 2026 forecast. It prevents giving the 2027–28 recovery credit for gains already achieved by 2026.', '', '**Scenario logic:** downside means stalled availability repair, persistent payment pressure and weak launches; base means current successful families hold their pace and selected gaps partly close; upside needs sustained retail conversion, broader attractive supply and no offsetting inventory build. The endpoints are rounded judgments, not evidence-backed causal coefficients.','']
for r in forecast:
    lines += [f'**{r["family"]} — {r["method"]}.** {r["rationale"]}', '']
lines+=['**Numerically unallocated:** Dakota/compact Ram launches, new Chrysler crossovers, Recon, Wagoneer S, Hornet and small-brand/runoff volumes. No assumed zero economic potential; evidence is insufficient to size a recovery. The launch register records the gates.',
 '', '**Country convention:** Canada 115k and Mexico 91k held flat in both years as explicit placeholders from the FY2025 reported rounded country baseline. Replace with the latest validated 2026 country exit before admitting them as forecast inputs. No separate detailed country schedules.',
 '', '**Quarterly application:** this pass supports annual scenarios, not a defensible twelve-quarter demand curve. Current-product seasonality, quarter-specific availability and launch dates must be reconciled before allocating annual units. A 2028 production start cannot justify four quarters of mature customer sales.',
 '', '**Portfolio check:** base 2028 Cherokee + Compass + Grand Cherokee = 365k, versus 312.6k in 2025 and 330.7k in 2024. Cherokee expansion is paired with Compass below its previous level; no assumption that all three fully recover independently. This is a portfolio constraint, not measured cannibalization. Base new-model gross sales and legacy replacement effects must not be counted a second time in a launch uplift row.',
 '', '**Model admission:** observed sales can populate history after the stated grouping/reconciliation checks. Current-pace scenarios are usable as provisional assumptions. Conditional launch scenarios require explicit user judgment; unallocated launches and dealer economics remain gates. Do not multiply these US customer volumes directly by revenue per wholesale shipment.']
(ROOT/'proposed-volume-inputs.md').write_text('\n'.join(lines)+'\n')

assert checks['2026_q3_ytd_minus_original_q1_q2_q3']==0
assert checks['2025_minivan_q3_comparative_pacifica_minus_old_pacifica_ytd']==checks['2025_voyager_ytd_from_fy_less_q4']
assert checks['2026_q1_minivan_combined']==checks['2026_q2_h1_minivan_less_q2']
assert sum(r['2028_base_growth_vs_2026_reference_units'] for r in forecast)==growth
for r in forecast:
    for year in ['2027','2028']:
        s=r[year+'_units']; assert s['downside']<=s['base']<=s['upside']
save('validation.json',{'status':'passed arithmetic and schema checks; not independent forecast validation','checks':checks,'forecast_totals':totals,'all_scenarios_ordered':True,'growth_contributions_reconcile':True})

# Present the required 14-field recovery ledger in one place, without overwriting
# independently authored qualitative evidence or mixing it into the sales data.
mechanisms=read('model-mechanisms.json')
mechanism_map={
 'ram_ld':0,'ram_pickups_unallocated':0,'ram_hd':1,'grand_cherokee':2,
 'wrangler':3,'compass':4,'gladiator':5,'cherokee':6,'wagoneer_family':7,
 'promaster':8,'promaster_city':9,'minivans':10,'charger_family':11,
 'durango':12,'hornet':13,'wagoneer_s':14,'recon':14,
 'renegade':15,'chrysler_300':15,'other_legacy':15,'fiat_alfa':15}
forecast_map={r['id']:r for r in forecast}
integrated=[]
lines=['# Model-by-model recovery ledger','',
 'Cutoff 14 October 2026. Customer sales are US retail plus fleet, not NA wholesale. All annual/available quarterly observations, shares and vintage residuals are in the linked historical ledger; compact rows below pair the sales evidence with mechanisms and proposed inputs. Null forecasts are deliberately unallocated, not zero.','',
 'Numerical coverage reconciles to reported totals through an explicit residual. Causal coverage is weaker for commercial vans, small brands and some launch cohorts. The older unsplit pickup row must never be added to modern LD/HD totals.','']
for h in ledger:
    m=mechanisms['families'][mechanism_map[h['id']]]
    f=forecast_map.get(h['id'])
    row={**h,'qualitative_evidence':m,'proposed_forecast':f,
       'new_product_net_incremental_units':None,
       'net_incremental_limitation':'No measured owner migration/cannibalization matrix. Family portfolio scenarios incorporate overlap qualitatively; gross launch sales are not independent additive company uplift.'}
    integrated.append(row)
    hist=h['annual_and_quarterly_sales_units']
    loss=h['2023_to_2024_loss_units']
    lines += [f'## {h["family"]}', '',
      f'**Observed scale:** 2025 {fmt(hist["2025A"])}; YTD September 2026 {fmt(hist["2026YTDQ3A"])} units. '+('2025 US share not separately known.' if h['share_2025_us_pct'] is None else f'2025 US share {h["share_2025_us_pct"]:.2f}%.')+' '+('2023–24 loss not separately allocable.' if loss is None else f'2023–24 lost units {loss:,} ({h["share_net_us_decline_2024_pct"]:.1f}% of net US decline; negative is an offset).'),
      '', f'**Earlier trajectory:** {m["pre_disruption_trajectory"]}',
      '', f'**Hypotheses:** '+ '; '.join(m['causal_hypotheses'])+'.',
      '', f'**Support / counterevidence:** {m["strongest_support"]} {m["counterevidence"]}',
      '', f'**Operational change and milestone:** {m["operational_change_status"]} Next: {m["forward_milestone"]}',
      '', f'**Pricing, overlap and inventory dependency:** {m["pricing_cannibalization_dependency"]} Sell-through and replenishment must support the family forecast; brand days supply is not model inventory.',
      '', f'**Confidence / falsifier:** {m["confidence"]} {m["next_falsifier"]}', '']
    if f:
        lines += [f'**Proposed annual judgment:** base 2027 {f["2027_units"]["base"]:,}, 2028 {f["2028_units"]["base"]:,}; 2028 downside/upside {f["2028_units"]["downside"]:,}/{f["2028_units"]["upside"]:,}. {f["rationale"]}', '']
    else:
        lines += ['**Forecast treatment:** unallocated or historical context only. No automatic rebound, no fabricated zero, no independent launch uplift.', '']
    lines += ['**Evidence locators:** '+', '.join('`'+s+'`' for s in m['source_refs'])+' in [mechanism source map](model-mechanisms.json); current quantitative values in [sales ledger](historical-sales-ledger.json).','']
save('recovery-ledger.json',{'as_of':'2026-10-14','scope':notes,'rows':integrated,'reconciliation':checks,'qualitative_sources':mechanisms['sources'],'forecast_totals':totals})
(ROOT/'recovery-ledger.md').write_text('\n'.join(lines).rstrip()+'\n')
print(json.dumps({'checks':checks,'forecast_totals':totals},indent=2))
