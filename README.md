# Product Hunt Launch Pricing & Website Intel

Top Product Hunt launches with the product's resolved website, live pricing page, plan tiers and lowest paid price.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/product-hunt-launch-pricing-intel) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/product-hunt-launch-pricing-intel/)

**from $2.80 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Product Hunt Launch Pricing & Website Intel reads Product Hunt leaderboards and goes one step further than a launch list: for every launch it follows the Product Hunt link to the product's real website, finds the pricing page and extracts the plans, prices, billing periods, free tier or trial, and the lowest paid price. You get clean, structured records you can export as JSON, CSV or Excel, call through the Apify API, or plug into n8n, Make and AI agents through MCP.
Pick a period, set a limit and run. With no dates it reads the latest finished day.

## Quick start

1. Open [Product Hunt Launch Pricing & Website Intel on Apify Store](https://apify.com/datagrit/product-hunt-launch-pricing-intel) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "period": "daily",
  "fetchPricing": true,
  "maxItems": 20
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `period` | string | Which Product Hunt leaderboard to read: daily, weekly, monthly or yearly. With no dates the latest finished period is read (yesterday for daily, last week, last month, last year). Each leaderboard page lists the launches Product Hunt shows on its first page, about 15 to 20. |
| `dates` | array | Optional periods to read, one per line, in the format of the chosen period: 2026-10-04 for daily, 2026-W40 for weekly, 2026-09 for monthly, 2025 for yearly. Leave empty for the latest finished period. At most 60 pages and products per run; entries that do not fit the period are skipped and named in the run status. |
| `productUrls` | array | Optional Product Hunt product links or slugs to look up directly, one per line, for example https://www.producthunt.com/products/notion or notion. Each is returned as one row with its website and pricing, without leaderboard fields. |
| `fetchPricing` | boolean | Open each product website, find its pricing page and extract plans, the lowest paid price and the pricing model. Switch off to return only the Product Hunt data and the website URL, which is faster. |
| `minVotes` | integer | Keep only launches with at least this many votes. Launches with no vote count are kept. |
| `topics` | array | Keep only launches in at least one of these Product Hunt topics, one per line, for example Artificial Intelligence or Developer Tools. Matching ignores case and accepts part of a topic name. |
| `pricingModel` | string | Keep only products with this pricing model: freemium, paid, free, usageBased or contactSales. Any keeps all. Needs Read pricing pages switched on; products whose pricing could not be read do not match a specific model. |
| `onlyNew` | boolean | Return only launches that an earlier run with the same period, dates, products, topics, minimum votes and pricing model has not returned yet. The memory is kept per combination of those settings in your account, so two monitors never hide each other's launches, and only returned launches are remembered. Use it with a schedule to get a stream of new launches. |
| `maxItems` | integer | Most launches to return in one run, in leaderboard order across all pages and products. |
| `proxyConfiguration` | object | Proxy used for requests to Product Hunt only (it blocks datacenter addresses); product websites are always fetched directly. The default is the Apify residential proxy, which keeps the run working. Switch it off only if you run from your own residential address. |

## Output

| Field | Type | Description |
|---|---|---|
| `source` | string | Where the row came from: leaderboard (a Product Hunt leaderboard page) or product (a product page you listed in the input). Null on the status row. |
| `period` | string | Leaderboard period the launch was read from: daily, weekly, monthly or yearly. Null for rows read from a product page. |
| `periodLabel` | string | The leaderboard page as a readable label, for example 2026-10-04 for a day, 2026-W40 for a week, 2026-09 for a month or 2025 for a year. |
| `rank` | integer | Position on the leaderboard page, 1 is the top launch. Product Hunt orders the page by its own ranking, so this is the rank Product Hunt shows. Null for product page rows. |
| `postId` | string | Product Hunt launch (post) ID. Stable across runs and used for the only-new memory. Null for product page rows. |
| `productName` | string | Name of the launched product. |
| `tagline` | string | One-line tagline from the launch. |
| `topics` | array | Product Hunt topics of the launch, for example Artificial Intelligence or Developer Tools. Empty for product page rows and the status row. |
| `votes` | integer | Upvotes on the launch at the time of the run. Null for product page rows. |
| `comments` | integer | Comments on the launch at the time of the run. Null for product page rows. |
| `featuredAt` | string | When Product Hunt featured the launch, ISO 8601 in UTC. Null for product page rows. |
| `productHuntUrl` | string | Link to the launch page, or to the product page for rows read from a product page. |
| `websiteUrl` | string | The product website the Product Hunt link redirects to, without tracking parameters (ref, utm_*), after following the site's own redirects. Null when the link did not resolve. |
| `websiteDomain` | string | Host of the website without www. |
| `websiteStatus` | string | ok when the website answered with an HTML page; blocked (HTTP 401, 403 or 429), unreachable (no HTML page, DNS or connection error), unresolved (the Product Hunt link could not be followed), noWebsite (Product Hunt has no website for the launch) or notChecked (pricing check switched off). Null on the status row. |
| `websiteTitle` | string | The title of the website home page. |
| `pricingStatus` | string | parsed when plan prices were found; noPrices when a page was read but showed no prices (usage or quote-only pricing, or prices drawn by scripts); blocked, notFound or unreachable when no pricing page could be read; notRequested when the pricing check is switched off. Null when the website itself could not be read. |
| `pricingPageUrl` | string | The page the prices were read from when pricingSource is pricingPage. |
| `pricingSource` | string | pricingPage when the prices come from a pricing page linked from the home page or found at /pricing; homepage when the home page itself shows plan prices. |
| `pricingModel` | string | freemium (a free plan and a paid plan), paid (paid plans only), free (no paid price found), usageBased (priced per use or credit), contactSales (a quote is needed for the paid plans) or unknown. Derived from the text and prices of the page, so check pricingConfidence. |
| `hasFreeTier` | boolean | True when the pricing page shows a free plan or a $0 price. |
| `hasFreeTrial` | boolean | True when the pricing page offers a free trial. |
| `contactSales` | boolean | True when a plan asks you to contact sales or request a quote. |
| `currency` | string | Currency of the prices, ISO 4217 code. |
| `lowestPaidPrice` | number | Price of the cheapest paid plan in the currency, per lowestPaidPeriod. Null when no paid price was found. |
| `lowestPaidPeriod` | string | Billing period of the lowest paid price: month, year, week, day, one-time, usage (priced per unit or credit) or null when the page does not say. |
| `pricingConfidence` | string | high when named plans with prices and billing periods were found, medium when some of that was missing, low when plans had no names or the price came from loose text. Treat low as a hint to check the page. Null when no prices were found. |
| `plans` | array | Plans found on the page, in page order. Empty when no prices were found. |
| `sourceUrl` | string | The Product Hunt page the row was read from. |
| `found` | boolean | True for a launch row, false on the single status row returned when nothing matched. |
| `scrapedAt` | string | When the run read the data, ISO 8601 in UTC. |

Sample record:

```json
{
  "source": "leaderboard",
  "period": "daily",
  "periodLabel": "2026-10-04",
  "rank": 1,
  "postId": "1259946",
  "productName": "CoreSpeed",
  "tagline": "Ship AI agents faster",
  "topics": [
    "Artificial Intelligence",
    "Developer Tools"
  ],
  "votes": 412,
  "comments": 37,
  "featuredAt": "2026-10-04T07:01:00.000Z",
  "productHuntUrl": "https://www.producthunt.com/posts/corespeed",
  "websiteUrl": "https://corespeed.io/",
  "websiteDomain": "corespeed.io",
  "websiteStatus": "ok",
  "websiteTitle": "CoreSpeed - AI agents",
  "pricingStatus": "parsed",
  "pricingPageUrl": "https://corespeed.io/pricing",
  "pricingSource": "pricingPage",
  "pricingModel": "freemium",
  "hasFreeTier": true,
  "hasFreeTrial": false,
  "contactSales": false,
  "currency": "USD",
  "lowestPaidPrice": 20,
  "lowestPaidPeriod": "month",
  "pricingConfidence": "high",
  "plans": [
    {
      "name": "Starter",
      "price": 20,
      "currency": "USD",
      "period": "month",
      "perSeat": false,
      "priceText": "$20"
    }
  ],
  "sourceUrl": "https://www.producthunt.com/leaderboard/daily/2026/10/4",
  "found": true,
  "scrapedAt": "2026-10-06T12:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~product-hunt-launch-pricing-intel/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"period":"daily","fetchPricing":true,"maxItems":20}'
```

## FAQ

**How fresh is the data?**  
Every run reads Product Hunt and the product websites live.

**Can I schedule runs?**  
Yes, use Apify schedules with the "only new" option to get each launch once.

**Why is pricingStatus not "parsed" for some launches?**  
The website may be unreachable, may block automated requests, or may show prices only after a click. The row still has the website and the reason.

**Something looks wrong.**  
Open an issue with the input you used; layout changes at the source are fixed quickly.

## More from datagrit

- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [GLEIF LEI Lookup - Parents And Subsidiaries](https://github.com/getdatagrit/gleif-lei-ownership-tree) - GLEIF legal entity records with direct and ultimate parents, reporting exceptions and direct subsidiaries.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/product-hunt-launch-pricing-intel). Examples are MIT licensed.
