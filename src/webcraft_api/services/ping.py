from src.webcraft_api.models.responses import PingDto
from src.webcraft_api.services.base import BaseService


class PingService(BaseService):
    """Service for ping-related API endpoints."""

    async def ping(self) -> PingDto:
        """
        Send a Ping request to the server to check if it is alive.

        Returns:
            PingDto: Ping response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/ping")
        return PingDto(**response)
