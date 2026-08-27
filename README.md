# Amazon Seller Analyzer — Python SDK

Python client for the [Amazon Seller Analyzer Apify Actor](https://apify.com/apivault_labs/amazon-seller-revenue-strategy-analyzer). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/amazon-seller-revenue-strategy-analyzer)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Daily, monthly and annual sales estimates
- Seller portfolio revenue ranges
- Buy Box and offer signals
- Strategy-change snapshots

The Actor uses public marketplace signals and returns estimates or ranges where a platform does not publish exact figures.

## Install

```bash
pip install git+https://github.com/apivault-labs/amazon-seller-analyzer-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from amazon_seller_analyzer import AmazonSellerAnalyzerClient

client = AmazonSellerAnalyzerClient(api_token="apify_api_xxxxxx")
rows = client.run({'sellerIds': ['A2L77EE7U53NWQ'], 'marketplace': 'us', 'maxProductsPerSeller': 10})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `sellerUrls` | `array` | `—` | Add Amazon seller profile URLs that contain a seller parameter, for example an /sp?seller=... URL. |
| `sellerIds` | `array` | `—` | Add Amazon merchant IDs directly. A seller ID normally contains 13–14 uppercase letters and numbers. |
| `marketplace` | `string` | `us` | Choose the marketplace where the seller operates. This controls catalog discovery, local prices, and output currency. |
| `maxProductsPerSeller` | `integer` | `10` | Maximum number of unique products analyzed for each seller. Billing applies only to products successfully analyzed. |
| `includeOffers` | `boolean` | `True` | Inspect publicly visible offer and Buy Box information for better attribution of listing demand to the target seller. |
| `trackStrategy` | `boolean` | `True` | Save an observation baseline and compare visible price, rank, availability, promotion, and seller-position signals on later runs. |
| `maxConcurrency` | `integer` | `4` | Number of products processed in parallel. The load-tested value balances speed and marketplace reliability. |
| `proxyConfiguration` | `object` | `{"useApifyProxy":true,"apifyProxyGroups":["RESIDENTIAL"]}` | Apify Residential Proxy is recommended for reliable marketplace access. Proxy traffic is billed by Apify as platform usage. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/amazon-seller-revenue-strategy-analyzer).

## Pricing

Pay per delivered result through Apify, starting around **$5/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
