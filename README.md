# Business Agents

Two rosters of Claude Code subagents live in this repo: one built specifically for a custom-commission 3D printing shop, and a general-purpose set for taking any small business from zero to a self-sustaining, growing operation. Both are auto-discovered from `.claude/agents/*.md` — no separate install step.

## How to use any of them

Invoke by name — "use the market-research agent to check demand for X" — or just describe the task naturally and Claude Code routes to the matching agent based on its `description`. Run `/agents` to see the full list Claude Code has picked up.

---

## 3D Printing Shop Agents

For a custom-commission print shop (Etsy/Shopify-style, made-to-order).

| Agent | Use it for |
|---|---|
| `quote-estimator` | Pricing a new custom print request from specs, and drafting the quote reply |
| `customer-support` | Order status, shipping questions, complaints, refund/reprint requests, FAQs |
| `order-manager` | Logging confirmed orders and moving them through the production queue in ClickUp |
| `listing-marketer` | Writing Etsy/Shopify listings, social captions, and Canva promo graphics |
| `inventory-tracker` | Logging material usage and flagging filament/resin reorders in Notion |
| `finance-bookkeeper` | Recording revenue/costs per order, margins, and monthly summaries |

**Before these are useful:**
1. Fill in `business-data/pricing.md` with your real material costs, machine rate, labor rate, and minimums — `quote-estimator` won't guess at real numbers while it's still placeholder data.
2. Fill in `business-data/policies.md` with your actual turnaround times, revision policy, and refund/reprint rules.
3. Connect: Gmail (quotes/support), ClickUp (order queue), Notion (inventory), Canva (marketing graphics), Google Drive (bookkeeping ledger).

---

## Growth Engine Agents

For any small business starting from zero, organized around four stages: **Ignition** (before you have anything) → **Combustion** (first offer goes live) → **Acceleration** (getting and keeping customers) → **Cruise** (running without you touching every part).

| Stage | Agent | Use it for |
|---|---|---|
| Ignition | `market-research` | Sizing demand, mapping competitors, before you build anything |
| Ignition | `brand-positioning` | Defining who it's for, what's different, and the voice everything else uses |
| Ignition | `financial-modeling` | Pricing, unit economics, break-even, runway |
| Combustion | `copywriter` | Website copy, product descriptions, email sequences |
| Combustion | `landing-page-builder` | Building and shipping the live site (via Lovable) |
| Combustion | `legal-compliance` | Draft terms of service, privacy policy, contract templates |
| Acceleration | `content-marketing` | Content calendar, blog posts, launch campaigns |
| Acceleration | `seo-specialist` | Keyword research, on-page and technical SEO audits |
| Acceleration | `social-media-manager` | Platform captions, posting schedule, Canva graphics |
| Acceleration | `sales-outreach` | Lead qualification, personalized outreach, meeting booking |
| Acceleration | `customer-experience` | General support inbox — any business other than the print shop |
| Cruise | `bookkeeping` | Ongoing revenue/expense ledger, margins, monthly P&L |
| Cruise | `growth-analytics` | Funnel metrics, experiment prioritization |
| Cruise | `operations-manager` | Vendor tracking, SOPs, project coordination |
| Cruise | `hiring-recruiter` | Job postings, market-rate research, candidate screening, onboarding |

**Before these are useful:**
1. Fill in `growth-data/brand.md` — `copywriter`, `landing-page-builder`, `content-marketing`, `social-media-manager`, and `customer-experience` all read from it so the business sounds like one brand, not five.
2. Connect what each stage needs: Gmail + Google Calendar (outreach/support/scheduling), ClickUp + Notion (operations), Canva (graphics), Lovable (the actual site), Google Drive (financials), Indeed/ZipRecruiter (hiring).
3. Run roughly in stage order the first time through — `copywriter` is much better once `brand-positioning` has actually run, `landing-page-builder` is much better with real copy in hand, and so on. After the first pass, most agents get invoked independently as needed.

A presentation of this roster is published as an artifact; ask if you want the link again or a refreshed version after editing an agent.

---

Add new agents the same way: one `.md` file in `.claude/agents/`, a clear `description` (Claude Code uses this to route to it), and only the tools it actually needs.
