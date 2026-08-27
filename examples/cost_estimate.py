from amazon_seller_analyzer import AmazonSellerAnalyzerClient

for count in (10, 100, 1000):
    print(count, AmazonSellerAnalyzerClient.estimate_cost(count), "USD estimated result charges")
