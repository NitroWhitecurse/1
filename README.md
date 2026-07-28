# 3D Printing Business Agents

A set of Claude Code subagents for running and scaling a custom-commission 3D printing shop (Etsy/Shopify-style, made-to-order). Each agent covers one function so you can invoke it directly instead of re-explaining context every time.

## Agents

| Agent | Use it for |
|---|---|
| `quote-estimator` | Pricing a new custom print request from specs, and drafting the quote reply |
| `customer-support` | Order status, shipping questions, complaints, refund/reprint requests, FAQs |
| `order-manager` | Logging confirmed orders and moving them through the production queue in ClickUp |
| `listing-marketer` | Writing Etsy/Shopify listings, social captions, and Canva promo graphics |
| `inventory-tracker` | Logging material usage and flagging filament/resin reorders in Notion |
| `finance-bookkeeper` | Recording revenue/costs per order, margins, and monthly summaries |

## How to use them

Invoke by name, e.g. "use the quote-estimator agent to price this commission" — Claude Code will pick up the definition from `.claude/agents/<name>.md` automatically.

## Before these are useful

1. **Fill in `business-data/pricing.md`** with your real material costs, machine rate, labor rate, and minimums. `quote-estimator` refuses to guess at real numbers if this is still placeholder data.
2. **Fill in `business-data/policies.md`** with your actual turnaround times, revision policy, and refund/reprint rules.
3. **Connect the tools each agent needs**: Gmail (quotes/support), ClickUp (order queue), Notion (inventory), Canva (marketing graphics), Google Drive (bookkeeping ledger). If a connector isn't set up, the agent will tell you rather than silently failing.

## Scaling path

This roster is sized for a solo/small operation. As volume grows, the natural next splits are:
- **quote-estimator** → separate agents per product line if pricing logic diverges (e.g. minis vs. functional parts)
- **order-manager** → per-printer or per-shift scheduling once you're running more than a couple of machines
- **listing-marketer** → split content calendar/scheduling from one-off listing writing once posting cadence increases

Add new agents the same way: one `.md` file in `.claude/agents/`, a clear `description` (Claude Code uses this to decide when to route to it), and only the tools it actually needs.
