"""Research sensitivities and admission controls. No workbook reading or writing.
Unknown eligibility/cost is None, never automatically converted to zero.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
R=P.parent
proposal=json.loads((R/'forecast-resolution-2026-10-14/proposal.json').read_text())
na2028=proposal['annual']['2028']['shipments']
vol={r['id']:r['net_customer_sales'] for r in proposal['model_inputs']['2028']}
pool=35e9; rate=.09; annual=pool*rate; u25=1472000
reconciliation={
 'currency':'EUR','price_year':'estimated2025pool; frozencomparablevolume/content',
 'estimated_pool':pool,'assumed_cumulative_reduction':rate,'terminal_annual_saving':annual,
 'reference_NA_shipments_2025':u25,'implied_component_purchase_proxy_per_reference_unit':pool/u25,
 'required_saving_per_reference_unit':annual/u25,
 'proposed_NA_shipments_2028':na2028,'target_divided_by2028_units_scale_ruler_not_volume_rescaling':annual/na2028,
 'implied_NA_to_nonNA_cost_intensity_if_global_purchase_floor88bn_treated_as_point':(35*(5.484-1.472))/(53*1.472),
 'three_equal_annual_reductions_equivalent':1-(1-rate)**(1/3),
 'two_equal_annual_reductions_equivalent':1-(1-rate)**.5,
 'coverage_sensitivities':[{'implemented_spend_share_assumed':s,'required_average_reduction_on_that_spend':rate/s} for s in [1,.8,.5,.35]],
 'warning':'Management35/80percent are reviewcoverage not implementedspend. Sensitivities do not reinterpret them as actualadoption.'}
# An untranslated historical supplier case is deliberately kept in its source currency.
conditional_units={'ram_ld_plus_grand_cherokee_US':vol['ram_ld']+vol['grand_cherokee'],
                   'all_NA_upper_bound_including_ineligible_vehicles':na2028}
aptiv={k:{'assumed_eligible_sold_units':n,'USD40_if_captured_unchanged_source_price_year_unknown':40*n,
          'verified_eligibility':False,'EUR_forecast_admission':None} for k,n in conditional_units.items()}
# Investment thresholds, not fabricated capex estimates. Baseline package unchanged.
case_A={'label':'Technical reference subpackage','project':'Aptiv electrical-center substitution only; retains propulsion/body/otherfunctions',
 'net_reference_saving_per_vehicle_USD':40,'price_year':None,'full_vehicle_cost':None,
 'vehicle_validation':'UnnamedOEMdemonstration,notSTLAcertifiedwholevehicle','total_frontier_STLA_EUR':None}
case_B={'label':'Economic admission test','net_recurring_unit_saving_USD':40,
 'thresholds':[{'remaining_lifetime_units_assumed':n,'maximum_undiscounted_incremental_investment_USD_at_full_price_capture':40*n} for n in [50000,100000,200000]],
 'actual_investment':None,'economically_approved_package':None,
 'caveat':'Deduct validation,transition,integration,warranty,maintenance/repair penalties; applydiscounting. Suppliermayretainpartofbenefit.'}
case_C={'label':'2028realizable assessment','verified_stla_eligible_2028_units':None,'verified_net_EUR_per_vehicle':None,
 'verified_NA_EUR_total':None,'conditional_scale_examples_only':aptiv,
 'admission':'No incremental change to currentforecast; examplesnotan approvedestimate.'}
case_D={'label':'Explicit delay scenario, not blanket haircut','event':'New architecture launches after2028',
 '2028_vehicles_receiving_that_change':0,'2028_saving_from_that_change':0,
 'existing_architecture_purchasing_savings':'Unchanged/unknown; do notzeroallVCP'}
weighted_rows=[]
for r in proposal['model_inputs']['2028']:
 weighted_rows.append({'model':r['id'],'forecast_US_customer_sales':r['net_customer_sales'],
 'forecast_US_wholesale_ratio':1,'powertrain_split':'Unknown here except explicitBEVmodels',
 'confirmed_project_fitment_share':None,'confirmed_unit_component_saving_EUR':None,
 'project_based_annual_saving_EUR':None})
for r in weighted_rows:
 if r['model'] in ['wagoneer_s','recon']:r['powertrain_split']='BEVmodel; actualbattery/projecteligible2028configurationstillunknown'
out={'reconciliation':reconciliation,'cases':{'A':case_A,'B':case_B,'C':case_C,'D':case_D},
 'NA_weighting':{'US_models':weighted_rows,'Canada_assumed_units':115000,'Mexico_assumed_units':91000,
 'Canada_Mexico_model_powertrain_split':None,'whole_NA_project_based_saving_EUR':None},
 'coverage':{'system_families_mapped':24,'priced_complete_Stellantis_BOMs':0,
 'verified_projects_with_EURcost_and_NA2028coverage':0,'project_based_estimate':None,
 'existing_target_not_substantiated_by_complete_project_build_EUR':annual,
 'interpretation':'Lack of publicprojectcoverage is not proofopportunityzero or upperbound;9percentremainsbenchmarkscenario.'}}
assert abs(annual-3150000000)<1
assert abs(sum(r['net_customer_sales'] for r in proposal['model_inputs']['2028'])+206000-na2028)<1
assert case_C['verified_NA_EUR_total'] is None
(P/'calculations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pool_reconciliation':reconciliation,'conditional_aptiv':aptiv,'coverage':out['coverage']},indent=2))
