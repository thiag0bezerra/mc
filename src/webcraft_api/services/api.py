from src.webcraft_api.models.responses import ApiDto
from src.webcraft_api.services.base import BaseService


class ApiService(BaseService):
    """Service for API information endpoints."""

    async def get_api_info(self) -> ApiDto:
        """
        Get various information about the API itself.

        Returns:
            ApiDto: Information about the API

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/api")
        return ApiDto(**response)
