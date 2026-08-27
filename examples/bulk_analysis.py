from amazon_seller_analyzer import AmazonSellerAnalyzerClient

client = AmazonSellerAnalyzerClient()
payload = {'sellerIds': ['A2L77EE7U53NWQ'], 'marketplace': 'us', 'maxProductsPerSeller': 10}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
