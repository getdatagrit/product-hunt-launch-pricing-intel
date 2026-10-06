# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/product-hunt-launch-pricing-intel").call(run_input={
    "period": "daily",
    "fetchPricing": True,
    "maxItems": 20
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
