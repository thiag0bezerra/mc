from typing import Optional


class APIException(Exception):
    """Exception raised for API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        """
        Initialize the exception.

        Args:
            message: The error message
            status_code: The HTTP status code
        """
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
