"""Teaching calculations only. Never reads or writes workbooks or assumptions."""
import json
from pathlib import Path


def l2_annual_saving(baseline_system_cost, eligible_sold_units, reduction=0.70):
    """Currency follows B; no assumed dollar baseline is supplied."""
    if baseline_system_cost is None or eligible_sold_units is None:
        return None
    return baseline_system_cost * reduction * eligible_sold_units


def payback_units(upfront_spend, net_saving_per_vehicle):
    if upfront_spend is None or net_saving_per_vehicle is None:
        return None
    if net_saving_per_vehicle <= 0:
        return None
    return upfront_spend / net_saving_per_vehicle


out = {
    "status": "illustrative parameterized arithmetic; not proposed forecast",
    "aptiv_electrical_example": {
        "reported_USD_per_vehicle": 40,
        "illustrative_eligible_sold_units": 100000,
        "annual_savings_USD_before_unreported_rollout_cost": 40 * 100000,
        "illustrative_upfront_cost_USD": 1000000,
        "break_even_units_before_discounting_and_other_costs": payback_units(1000000, 40),
        "price_year": None,
        "fx_conversion": None,
        "stla_adoption": "unknown"
    },
    "stla_l2_example": {
        "formula": "0.70 * B * N",
        "B": "verified comparable baseline L2+system cost per equipped vehicle in a common currency/priceyear",
        "N": "eligible vehicles sold with replacement system; not all Ram/Jeep vehicles",
        "per_100000_eligible_vehicles": "70000 * B currencyunits, or0.07 * B million currencyunits",
        "per_100_currencyunits_of_B_at_100000_units": 0.70 * 100 * 100000,
        "interpretation": "7million for each100currencyunits of verified B; scale ruler, not B assumption",
        "annual_na_2028_saving": l2_annual_saving(None, None),
        "payback": "upfront_cost / (0.70 * B) eligible units, only if0.70B is net recurring comparable cost reduction"
    }
}
assert out["aptiv_electrical_example"]["annual_savings_USD_before_unreported_rollout_cost"] == 4000000
assert out["aptiv_electrical_example"]["break_even_units_before_discounting_and_other_costs"] == 25000
assert out["stla_l2_example"]["annual_na_2028_saving"] is None
Path(__file__).with_name("calculations.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
