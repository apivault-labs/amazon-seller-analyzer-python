import json
from amazon_seller_analyzer import AmazonSellerAnalyzerClient

rows = AmazonSellerAnalyzerClient().run({'sellerIds': ['A2L77EE7U53NWQ'], 'marketplace': 'us', 'maxProductsPerSeller': 10})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
