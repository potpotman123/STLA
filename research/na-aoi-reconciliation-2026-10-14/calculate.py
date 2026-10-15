"""Reconcile existing proposals without inventing missing 2026 actuals or cost forecasts.
All financial outputs EUR million. Sensitivities are unselected assumptions.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = HERE.parent
rpu = json.loads((R/'rpu-working-assumptions-2026-10-14.json').read_text())
vcp = json.loads((R/'vcp-schedule-2026-10-14/schedule.json').read_text())
coefficient = json.loads((R/'aoi-volume-contribution-2026-10-14/calculations.json').read_text())['base_eur_per_vehicle']
annual = {}
for year, ratio, support in [('2027', .98, 500), ('2028', 1, 250)]:
    case = rpu['rounded_input_forecasts'][year]
    us = case['us_customer_sales'] * ratio
    na = us + 115000 + 91000
    # Match the existing rounded-case builder for every country, not just the US.
    revenue = (us*case['us_effective_rpu'] + 115000*round(rpu['canada_forecast_rpu']/500)*500 + 91000*round(rpu['mexico_forecast_rpu']/500)*500)/1e6
    annual[year] = dict(us_shipments=us, na_shipments=na, revenue_eurm=revenue,
        effective_rpu_eur=revenue*1e6/na,
        support_cost_vs_reference_eurm=us*support/1e6,
        recognized_vcp_eurm=vcp['annual_total_eurm'][year])
a,b = annual['2027'],annual['2028']
volume = (b['na_shipments']-a['na_shipments'])*coefficient/1e6
price = a['support_cost_vs_reference_eurm']-b['support_cost_vs_reference_eurm']
saving_delta = b['recognized_vcp_eurm']-a['recognized_vcp_eurm']
subtotal = volume+price+saving_delta
out = dict(status='Conditional research bridge, not a completed NA AOI forecast; workbook and original assumptions unchanged', annual=annual,
    yoy_2028_eurm=dict(volume_mix=volume, net_price_support=price, vcp=saving_delta, quantified_subtotal_before_other_changes=subtotal),
    yoy_2027_formula='AOI27 = AOI26 + (1,533,851 - NA_shipments26)*0.005 + 1,195.8 - 663.9255 + US_support_cost26_vs_reference + Other_delta27; AOI EURm, shipments units',
    cumulative_2026_to_2028_formula='AOI28 = AOI26 + (1,636,700 - NA_shipments26)*0.005 + 3,587.4 - 357.675 + US_support_cost26_vs_reference + Other_delta27 + Other_delta28',
    missing_inputs=['FY2026 comparable NA AOI and shipments', 'Full-year 2026 support deviation from H1 reference', '2027/28 non-VCP industrial, SG&A, R&D and FX/other movements'],
    controls={'2026_VCP_already_in_starting_AOI_eurm':398.6, '2028_price_naive_current_units_times_250_eurm':b['us_shipments']*250/1e6,
        '2028_price_volume_interaction_correction_eurm':-(b['us_shipments']-a['us_shipments'])*500/1e6},
    sensitivities={})
for name, benefit in [('current_gross_case', subtotal),
    ('2028_VCP_recognition_70pct', volume+price+3986*.7-1594.4),
    ('remove_all_manufacturing_VCP_in_both_years',subtotal-581*.6),
    ('remove_all_logistics_VCP_in_both_years',subtotal-255*.6),
    ('additional_2028_vs_2027_cost_headwind_500m',subtotal-500),
    ('additional_2028_vs_2027_cost_headwind_1000m',subtotal-1000)]:
    out['sensitivities'][name] = dict(yoy_2028_aoi_eurm=benefit,
        implied_2028_margin_if_2027_margin_2pct=(a['revenue_eurm']*.02+benefit)/b['revenue_eurm'])
out['margin_thresholds'] = {str(m): {'required_AOI2027_before_other_changes_eurm':m*b['revenue_eurm']-subtotal,
    'required_margin2027_before_other_changes':(m*b['revenue_eurm']-subtotal)/a['revenue_eurm']} for m in [.05,.08,.10]}
out['cost_sensitivities_not_forecasts'] = {
    'one_pct_inflation_on_post_savings_reference_components_eurm':35000*(1-.09)*.01,
    'one_pct_inflation_on_post_savings_reference_plant_labor_eurm':5500*(1-.083)*.01,
    'management_group_raw_material_1p4pp_applied_to_our_NA_2028_revenue_scale_only_eurm':b['revenue_eurm']*.014,
    'management_group_SGA_0p6pp_applied_to_our_NA_2028_revenue_scale_only_eurm':b['revenue_eurm']*.006}
assert abs(price-306.2505)<1e-6
assert abs(subtotal-3212.0955)<1e-6
assert abs(price-(out['controls']['2028_price_naive_current_units_times_250_eurm']+out['controls']['2028_price_volume_interaction_correction_eurm']))<1e-6
assert abs(398.6+1195.8+2391.6-3986)<1e-6
assert abs(b['revenue_eurm']/b['na_shipments']*1e6-rpu['rounded_input_forecasts']['2028']['na_effective_rpu'])<1e-6
(HERE/'bridge.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
