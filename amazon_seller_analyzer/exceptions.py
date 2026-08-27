"""Public exception hierarchy for the Amazon Seller Analyzer SDK."""

class AmazonSellerAnalyzerError(Exception):
    """Base SDK error."""

class AuthenticationError(AmazonSellerAnalyzerError):
    """The Apify token is missing or rejected."""

class ActorRunError(AmazonSellerAnalyzerError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(AmazonSellerAnalyzerError):
    """The client stopped waiting before the Actor completed."""
