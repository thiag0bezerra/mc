from src.webcraft_api.models.responses import AdminsDto, IsAdminDto
from src.webcraft_api.services.base import BaseService


class AdminService(BaseService):
    """Service for admin-related API endpoints."""

    async def get_admins(self) -> AdminsDto:
        """
        Get a list of all server admins.

        Returns:
            AdminsDto: Object containing list of admins

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/admins")
        return AdminsDto(**response)

    async def is_player_admin(self, player: str) -> IsAdminDto:
        """
        Check if a specific player is a server admin.

        Args:
            player: The player name

        Returns:
            IsAdminDto: Response indicating if the player is an admin

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/admins/{player}")
        return IsAdminDto(**response)
