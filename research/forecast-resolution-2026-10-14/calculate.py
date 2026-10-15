"""Proposed assumptions for Fable; never opens or edits an Excel file.
Financial units EURm. Policy judgments are explicit, not reported guidance.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
R=P.parent
rpu=json.loads((R/'rpu-working-assumptions-2026-10-14.json').read_text())
vcp=json.loads((R/'vcp-schedule-2026-10-14/schedule.json').read_text())
audit=json.loads((R/'workbook-2026-anchor-audit-2026-10-14/inspection.json').read_text())
old=audit['summary']
inputs={
 'status':'AI-recommended implementation case under user instruction to resolve assumptions; judgments remain estimates, not independently observed outcomes',
 'h1_2026_aoi_eurm':547,'h1_2026_shipments':824000,
 'na_q1_2026_ieepa_adjustment_eurm':400,
 'group_H2_vs_H1_2026_raw_material_headwind_eurm':600,
 'NA_share_of_incremental_raw_material_headwind':.40,
 'NA_all_in_labor_inflation_2027_and_2028':.03,
 'incremental_SGA_execution_envelope_vs_2026_eurm':{'2027':200,'2028':400},
 'internal_substitution_share_of_four_launch_families':.20,
 'warranty_operational_savings_credited_eurm':{'2026':0,'2027':0,'2028':0},
 'future_tariff_policy_change_beyond_refund_expiry':0,
 'additional_post_H2_2026_raw_material_price_inflation':0,
 'further_FX_RD_change':0,
 'volume_coefficient_eur':5000,
 'q3_2026_shipments_preliminary':357000,'q4_2026_shipments_assumed':399625,
 'source_types':{'na_q1_2026_ieepa_adjustment_eurm':'reported NA interim report p20',
 'group_H2_vs_H1_2026_raw_material_headwind_eurm':'derived from CFO approx1000 combined less400 adjustment',
 'NA_share_of_incremental_raw_material_headwind':'assumed rounded35/88 purchasing-pool allocation proxy',
 'NA_all_in_labor_inflation_2027_and_2028':'assumed planning rate, not UAW rate applied to NA payroll',
 'incremental_SGA_execution_envelope_vs_2026_eurm':'assumed additional spending envelope; scale anchored to management group0.6pp, not regional guidance',
 'internal_substitution_share_of_four_launch_families':'assumed planning reserve, not measured cannibalization'}}

def build(substitution=.20,rawshare=.40,labor_rate=.03,sga_scale=1,terminal_recognition=1,raw_h2=600,further_material_inflation=0):
    na_raw=raw_h2*rawshare
    quarterly26={}
    for q,ship,prev_aoi,prev_ship in [('Q3',357000,-475,404000),('Q4',399625,-471,422000)]:
        normalized_h1_quarter=(547-400)/2
        volume=(ship-824000/2)*.005
        raw=-na_raw/2
        target=normalized_h1_quarter+volume+raw
        old_volume=(ship-prev_ship)*.005
        # Visible aggregate rebase, NOT identified industrial saving. Main YoY bridge preserved.
        rebase=target-(prev_aoi+old_volume+99.65)
        quarterly26[q]=dict(shipments=ship,normalized_H1_quarter_AOI=normalized_h1_quarter,
            sequential_volume=volume,additional_raw_material=raw,aoi=target,
            aggregate_reference_rebase_before_raw_material=rebase-raw,
            required_aggregate_other_rebase_in_existing_yoy_bridge=rebase)
    a26=547+sum(x['aoi'] for x in quarterly26.values())
    years={'2026':{'shipments':1580625,'revenue':old['2026']['revenue_eurm'],'AOI':a26,
        'margin':a26/old['2026']['revenue_eurm']}}
    prior_labor_extra=0
    prior_support=0
    prior_saving=vcp['annual_total_eurm']['2026']
    prior_material_extra=0
    models={}
    for y,ratio,support,recog in [('2027',.98,500,.4),('2028',1,250,terminal_recognition)]:
        # Donors are explicit. Keep new-launch gross rows; subtract from incumbent rows once.
        launch={'2027':{'city':10000,'chrysler':10000,'dakota':0,'compact':0},
                '2028':{'city':13000,'chrysler':50000,'dakota':20000,'compact':10000}}[y]
        donor={'promaster':launch['city']*substitution,
          'grand_cherokee':launch['chrysler']*substitution*.5,
          'compass':launch['chrysler']*substitution*.5+launch['compact']*substitution*.5,
          'ram_ld':launch['dakota']*substitution+launch['compact']*substitution*.5}
        rows=[]
        for r in rpu['model_rows']:
            gross=r['forecast_units_'+y]
            units=gross-donor.get(r['id'],0)
            assert units>=0
            price=r['rounded_reference_before_incremental_support_EUR']-support
            rows.append({'id':r['id'],'gross_customer_sales':gross,'donor_deduction':donor.get(r['id'],0),
                         'net_customer_sales':units,'net_rpu_eur':price})
        ussales=sum(r['net_customer_sales'] for r in rows)
        usship=ussales*ratio
        ships=usship+206000
        revenue=(sum(r['net_customer_sales']*r['net_rpu_eur'] for r in rows)*ratio+115000*38500+91000*30000)/1e6
        previous=years[str(int(y)-1)]
        vol=(ships-previous['shipments'])*.005
        curr_support=usship*support/1e6
        price_delta=prior_support-curr_support
        recognized=3986*recog
        saving_delta=recognized-prior_saving
        refund=-400 if y=='2027' else 0
        # H2 additional half-year cost persists for a full year in2027. No new shock assumed thereafter.
        raw_delta=-na_raw if y=='2027' else 0
        material_extra=(35000-35000*.09*recog)*((1+further_material_inflation)**(int(y)-2026)-1)
        raw_delta+=prior_material_extra-material_extra
        labor_saving=5500*.083*recog
        labor_extra=(5500-labor_saving)*((1+labor_rate)**(int(y)-2026)-1)
        labor_delta=prior_labor_extra-labor_extra
        sga_delta=-200*sga_scale
        delta=sum([vol,price_delta,saving_delta,refund,raw_delta,labor_delta,sga_delta])
        aoi=previous['AOI']+delta
        years[y]={'us_customer_sales':ussales,'us_shipments':usship,'shipments':ships,
          'revenue':revenue,'AOI':aoi,'margin':aoi/revenue,'substitution_units':sum(donor.values()),
          'bridge':{'prior_AOI':previous['AOI'],'volume_mix':vol,'price_support':price_delta,
          'incremental_VCP':saving_delta,'refund_nonrepeat':refund,'raw_material_annualization':raw_delta,
          'labor_inflation':labor_delta,'SGA_execution_reinvestment':sga_delta,'AOI_delta':delta},
          'cumulative_additional_labor_cost':labor_extra,
          'variance_vs_inspected_workbook_AOI':aoi-old[y]['aoi_eurm']}
        prior_support=curr_support;prior_saving=recognized;prior_labor_extra=labor_extra
        prior_material_extra=material_extra
        models[y]=rows
        assert abs(aoi-previous['AOI']-delta)<1e-7
    return {'quarterly_2026':quarterly26,'annual':years,'model_inputs':models}

base=build()
variants={
 'zero_substitution':dict(substitution=0),
 'forty_pct_substitution':dict(substitution=.4),
 'raw_material_NA_share_25pct':dict(rawshare=.25),
 'raw_material_NA_share_55pct':dict(rawshare=.55),
 'no_further_labor_inflation':dict(labor_rate=0),
 'labor_inflation_5pct':dict(labor_rate=.05),
 'no_additional_SGA_execution_envelope':dict(sga_scale=0),
 'further_material_inflation_1pct_annually':dict(further_material_inflation=.01),
 'VCP_2028_recognition_70pct':dict(terminal_recognition=.7)}
sens={k:build(**args)['annual'] for k,args in variants.items()}
assert abs(base['annual']['2026']['AOI']-117.125)<1e-7
assert base['annual']['2027']['substitution_units']==4000
assert base['annual']['2028']['substitution_units']==18600
out={'inputs':inputs,**base,'one_at_a_time_sensitivities':sens,
 'scope':'Research implementation packet only. Workbook unchanged. 2026 quarter rebases are explicitly unallocated aggregate estimates, not identified savings.'}
(P/'proposal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'quarterly_2026':base['quarterly_2026'],'annual':base['annual'],
 'sensitivity_2028_margin':{k:x['2028']['margin'] for k,x in sens.items()}},indent=2))
