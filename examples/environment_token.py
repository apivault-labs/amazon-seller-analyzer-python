import os
from amazon_seller_analyzer import AmazonSellerAnalyzerClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = AmazonSellerAnalyzerClient()
print(client.run_one({'sellerIds': ['A2L77EE7U53NWQ'], 'marketplace': 'us', 'maxProductsPerSeller': 10}))
