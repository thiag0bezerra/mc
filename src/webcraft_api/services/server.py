from src.webcraft_api.models.responses import ServerDto
from src.webcraft_api.services.base import BaseService


class ServerService(BaseService):
    """Service for server-related API endpoints."""

    async def get_server_info(self) -> ServerDto:
        """
        Get various information about the server itself.

        Returns:
            ServerDto: Server information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/server")
        return ServerDto(**response)
