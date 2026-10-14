"""Reproduce proposed NA VCP scenarios. No network, workbook or third-party packages."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
inputs = json.loads((HERE / "vcp-savings-inputs.json").read_text())
years = inputs["years"]
cases = ("downside", "base_case", "upside")
result = {"as_of": inputs["as_of"], "units": inputs["units"], "cases": {}}

for case in cases:
    drivers = {}
    totals = [0.0] * len(years)
    gross_total = 0.0
    expense_totals = [0.0] * len(years)
    for name, d in inputs["drivers"].items():
        a = d[case]
        assert 0 <= a["addressable"] <= 1 and 0 <= a["reduction"] <= 1
        assert len(a["recognition"]) == len(a["AOI_expense_allowance"]) == len(years)
        assert all(0 <= f <= 1 for f in a["recognition"])
        eligible = d["base"] * a["addressable"]
        if name == "quality":
            assert eligible <= d["base"] - d["excluded_remeasurement_pool"]
        gross = eligible * a["reduction"]
        pre_expense = [gross * f for f in a["recognition"]]
        net = [g - e for g, e in zip(pre_expense, a["AOI_expense_allowance"])]
        gross_total += gross
        for i, value in enumerate(net):
            totals[i] += value
            expense_totals[i] += a["AOI_expense_allowance"][i]
        drivers[name] = {
            "eligible_cost": eligible, "mature_gross_annual_saving": gross,
            "annual_gross_recognized": dict(zip(years, pre_expense)),
            "annual_AOI_expense_allowance": dict(zip(years, a["AOI_expense_allowance"])),
            "annual_recognized_net_AOI_benefit_vs_2025": dict(zip(years, net)),
            "effective_net_savings_rate_on_entire_base": dict(zip(years, [n/d["base"] for n in net])),
        }
    increments = [totals[0]] + [totals[i]-totals[i-1] for i in range(1, len(years))]
    assert abs(sum(increments)-totals[-1]) < 1e-9
    result["cases"][case] = {
        "drivers": drivers,
        "mature_gross_annual_saving": gross_total,
        "annual_AOI_expense_allowance": dict(zip(years, expense_totals)),
        "annual_recognized_net_AOI_benefit_vs_2025": dict(zip(years, totals)),
        "incremental_net_AOI_benefit_YoY": dict(zip(years, increments)),
        "each_quarter_net_AOI_benefit_vs_corresponding_2025_quarter": dict(zip(years, [n/4 for n in totals])),
        "each_quarter_incremental_net_AOI_benefit_YoY": dict(zip(years, [n/4 for n in increments])),
    }

base_total = result["cases"]["base_case"]["annual_recognized_net_AOI_benefit_vs_2025"][2028]
mat = inputs["drivers"]["components"]
a = mat["base_case"]
q = inputs["drivers"]["quality"]
qa = q["base_case"]
log = inputs["drivers"]["logistics_indirect"]
la = log["base_case"]
result["base_2028_sensitivities_EURbn"] = {
    "components_eligible_reduction_plus_minus_1pp": mat["base"]*a["addressable"]*0.01*a["recognition"][-1],
    "components_addressable_share_plus_minus_10pp": mat["base"]*0.10*a["reduction"]*a["recognition"][-1],
    "components_cost_base_plus_minus_5bn": 5*a["addressable"]*a["reduction"]*a["recognition"][-1],
    "components_annual_recognition_plus_minus_10pp": mat["base"]*a["addressable"]*a["reduction"]*0.10,
    "quality_eligible_reduction_plus_minus_10pp": q["base"]*qa["addressable"]*0.10*qa["recognition"][-1],
    "logistics_cost_base_plus_minus_1bn": la["addressable"]*la["reduction"]*la["recognition"][-1],
    "all_2028_AOI_expense_allowances_doubled": -result["cases"]["base_case"]["annual_AOI_expense_allowance"][2028],
    "one_pp_net_price_decline_on_2025_revenue_external": -0.01*inputs["external_offset_illustrations"]["NA_2025_net_revenue"],
    "ten_percent_VCP_giveback_in_price_external": -0.10*base_total,
}

ext = inputs["external_offset_illustrations"]
w = ext["US_general_wage_rate"]
avg2025 = (8*w["pre_September_2025"] + 4*w["September_2025"])/12
average_wages = [
    (8*w["September_2025"] + 4*w["September_2026"])/12,
    (8*w["September_2026"] + 4*w["September_2027_held_in_2028"])/12,
    w["September_2027_held_in_2028"],
]
uplifts = [v/avg2025-1 for v in average_wages]
result["illustrative_US_wage_offsets_only_not_deducted"] = {
    "annual_average_GWI_vs_2025": dict(zip(years, uplifts)),
    "2028_cost_headwind_range_at_unchanged_paid_hours": [ext["US_loaded_labor_pool_assumed"]*s*uplifts[-1] for s in ext["US_wage_sensitive_share_assumed"]],
    "warning": "Excludes COLA, progression, benefits, profit sharing, new bargaining and Canada/Mexico. Under actual labor savings apply inflation to remaining wage-sensitive hours to avoid cross-term double count."
}
result["accounting_normalization"] = inputs["accounting_normalization"]

def rounded(obj):
    if isinstance(obj, float):
        return round(obj, 6)
    if isinstance(obj, dict):
        return {k: rounded(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [rounded(x) for x in obj]
    return obj

(HERE / "vcp-savings-results.json").write_text(json.dumps(rounded(result), indent=2) + "\n")
for case, data in result["cases"].items():
    print(case, "mature gross:", round(data["mature_gross_annual_saving"], 3),
          "annual net:", [round(v, 3) for v in data["annual_recognized_net_AOI_benefit_vs_2025"].values()],
          "YoY:", [round(v, 3) for v in data["incremental_net_AOI_benefit_YoY"].values()])
print("Base 2028 by driver:", {k: round(v["annual_recognized_net_AOI_benefit_vs_2025"][2028], 3) for k,v in result["cases"]["base_case"]["drivers"].items()})
