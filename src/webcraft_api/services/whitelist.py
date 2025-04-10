from src.webcraft_api.models.requests import (
    UnwhitelistPlayerRequest,
    WhitelistPlayerRequest,
)
from src.webcraft_api.models.responses import (
    IsWhitelistedDto,
    SuccessResponse,
    WhitelistDto,
    WhitelistedPlayersDto,
)
from src.webcraft_api.services.base import BaseService


class WhitelistService(BaseService):
    """Service for whitelist-related API endpoints."""

    async def get_whitelist_info(self) -> WhitelistDto:
        """
        Get various information about the whitelist.

        Returns:
            WhitelistDto: Whitelist information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/whitelist")
        return WhitelistDto(**response)

    async def get_whitelisted_players(self) -> WhitelistedPlayersDto:
        """
        Get a list of whitelisted players.

        Returns:
            WhitelistedPlayersDto: List of whitelisted players

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/whitelist/players")
        return WhitelistedPlayersDto(**response)

    async def whitelist_player(self, name: str) -> SuccessResponse:
        """
        Add a player to the whitelist.

        Args:
            name: The player name

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = WhitelistPlayerRequest(name=name)
        response = await self.client._post(
            "/api/whitelist/players/add", request.__dict__
        )
        return SuccessResponse(**response)

    async def unwhitelist_player(self, name: str) -> SuccessResponse:
        """
        Remove a player from the whitelist.

        Args:
            name: The player name

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = UnwhitelistPlayerRequest(name=name)
        response = await self.client._post(
            "/api/whitelist/players/remove", request.__dict__
        )
        return SuccessResponse(**response)

    async def is_player_whitelisted(self, player: str) -> IsWhitelistedDto:
        """
        Check if the specified player is on the whitelist.

        Args:
            player: The player name

        Returns:
            IsWhitelistedDto: Response indicating if the player is whitelisted

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/whitelist/players/{player}")
        return IsWhitelistedDto(**response)
