from src.webcraft_api.models.requests import (
    BanIpRequest,
    BanPlayerRequest,
)
from src.webcraft_api.models.responses import (
    BannedIpsDto,
    BannedPlayersDto,
    IsBannedDto,
    SuccessResponse,
)
from src.webcraft_api.services.base import BaseService


class BanlistService(BaseService):
    """Service for ban list related API endpoints."""

    async def get_banned_ips(self) -> BannedIpsDto:
        """
        Get a list of all banned IP addresses.

        Returns:
            BannedIpsDto: List of banned IPs

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/banlist/ips")
        return BannedIpsDto(**response)

    async def ban_ip(self, request: BanIpRequest) -> SuccessResponse:
        """
        Ban an IP address from the server.

        Args:
            request: The ban IP request

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post("/api/banlist/ips/ban", request.__dict__)
        return SuccessResponse(**response)

    async def is_ip_banned(self, ip: str) -> IsBannedDto:
        """
        Check if the specified IP address is banned.

        Args:
            ip: The IP address

        Returns:
            IsBannedDto: Response indicating if the IP is banned

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/banlist/ips/{ip}")
        return IsBannedDto(**response)

    async def unban_ip(self, ip: str) -> SuccessResponse:
        """
        Pardon/unban an IP Address from the server.

        Args:
            ip: The IP address

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/banlist/ips/{ip}/pardon")
        return SuccessResponse(**response)

    async def get_banned_players(self) -> BannedPlayersDto:
        """
        Get a list of all banned players.

        Returns:
            BannedPlayersDto: List of banned players

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/banlist/players")
        return BannedPlayersDto(**response)

    async def ban_player(self, request: BanPlayerRequest) -> SuccessResponse:
        """
        Ban a player from the server.

        Args:
            request: The ban player request

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post("/api/banlist/players/ban", request.__dict__)
        return SuccessResponse(**response)

    async def is_player_banned(self, player: str) -> IsBannedDto:
        """
        Check if the specified player is banned.

        Args:
            player: The player name

        Returns:
            IsBannedDto: Response indicating if the player is banned

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/banlist/players/{player}")
        return IsBannedDto(**response)

    async def unban_player(self, player: str) -> SuccessResponse:
        """
        Pardon/unban a player from the server.

        Args:
            player: The player name

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/banlist/players/{player}/pardon")
        return SuccessResponse(**response)
