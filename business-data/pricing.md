# Pricing Reference

Fill in your real numbers. `quote-estimator` reads this file before calculating any quote — if it's still full of placeholders, it will ask you for real values instead of guessing.

## Material cost (per gram)

| Material       | Cost/g | Notes                        |
|----------------|--------|-------------------------------|
| PLA            | $0.02  |                                |
| PETG           | $0.025 |                                |
| ABS            | $0.025 |                                |
| Resin (standard) | $0.08 |                              |
| Resin (tough/flexible) | $0.12 |                        |

## Machine time

- Hourly machine rate (electricity + depreciation + wear): **$1.50/hr**
- Rate covers unattended print time, not labor.

## Labor & post-processing

- Hourly labor rate (setup, supports removal, sanding, painting, assembly): **$20/hr**
- Design/modeling work (if not just slicing a provided file): **$25/hr**

## Overhead & fees

- Packaging cost per order: **$1.50**
- Platform fee (Etsy: ~6.5% transaction + 3%+$0.25 payment processing; adjust for your platform): **~10%**
- Failed-print buffer (built into price to cover reprints): **10%** of material+time cost

## Minimums & multipliers

- Minimum order price: **$15**
- Rush order (< 3 day turnaround) surcharge: **+25%**
- First-time complex/custom design surcharge (covers extra iteration risk): **+15%**

## Standard formula

```
material_cost   = grams_used * cost_per_gram
machine_cost    = print_hours * hourly_machine_rate
labor_cost      = labor_hours * hourly_labor_rate
design_cost     = design_hours * design_rate (only if modeling was required)
subtotal        = material_cost + machine_cost + labor_cost + design_cost + packaging
subtotal        *= 1.10   (failed-print buffer)
subtotal        *= 1.25   (if rush)
platform_fee    = subtotal * 0.10
price           = max(subtotal + platform_fee, minimum_order_price)
```

## Turnaround times (for customer-facing quotes)

- Standard: **5-7 business days**
- Rush: **2-3 business days** (+25%)
