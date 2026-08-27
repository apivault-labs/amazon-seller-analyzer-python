from amazon_seller_analyzer import AmazonSellerAnalyzerClient

client = AmazonSellerAnalyzerClient()
rows = client.run({'sellerIds': ['A2L77EE7U53NWQ'], 'marketplace': 'us', 'maxProductsPerSeller': 10})
print(rows[0] if rows else "No results")
