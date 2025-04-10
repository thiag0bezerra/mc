class BaseService:
    """Base class for API service implementations."""

    def __init__(self, client: "WebCraftAPI"):
        """
        Initialize the service.

        Args:
            client: The WebCraftAPI client instance
        """
        self.client = client
