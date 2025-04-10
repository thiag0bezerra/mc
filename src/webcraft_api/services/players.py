from typing import Optional

from src.webcraft_api.models.enums import SlotType
from src.webcraft_api.models.requests import (
    FoodLevelRequest,
    GiveRequest,
    HealthRequest,
    KickRequest,
    MaxHealthRequest,
    SlotRequest,
    TeleportRequest,
)
from src.webcraft_api.models.responses import (
    FoodLevelDto,
    HealthDto,
    LocationDto,
    MaxHealthDto,
    PlayerCountDto,
    PlayerDto,
    PlayerInventoryDto,
    PlayerNamesDto,
    PlayerSpawnPointDto,
    SlotDto,
    SuccessResponse,
)
from src.webcraft_api.services.base import BaseService


class PlayersService(BaseService):
    """Service for player-related API endpoints."""

    async def get_count(self) -> PlayerCountDto:
        """
        Get Online/Offline players count.

        Returns:
            PlayerCountDto: Player count information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/players")
        return PlayerCountDto(**response)

    async def get_online_players(self) -> PlayerNamesDto:
        """
        Get a list of all players currently online.

        Returns:
            PlayerNamesDto: List of online player names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/players/online")
        return PlayerNamesDto(**response)

    async def get_offline_players(self) -> PlayerNamesDto:
        """
        Get a list of all players currently offline.

        Returns:
            PlayerNamesDto: List of offline player names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/players/offline")
        return PlayerNamesDto(**response)

    async def get_player_info(self, player: str) -> PlayerDto:
        """
        Get information about a specific player.

        Args:
            player: The player name or UUID

        Returns:
            PlayerDto: Player information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}")
        return PlayerDto(**response)

    async def feed_player(self, player: str) -> SuccessResponse:
        """
        Feed a player by setting their food level to the maximum value.

        Args:
            player: The player name or UUID

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/players/{player}/feed")
        return SuccessResponse(**response)

    async def give_items(
        self, player: str, item: str, amount: int = 1
    ) -> SuccessResponse:
        """
        Give items/blocks to a player.

        Args:
            player: The player name or UUID
            item: The item to give
            amount: The amount to give

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = GiveRequest(item=item, amount=amount)
        response = await self.client._post(
            f"/api/players/{player}/give", request.__dict__
        )
        return SuccessResponse(**response)

    async def heal_player(self, player: str) -> SuccessResponse:
        """
        Heal a player by setting their health to the maximum value.

        Args:
            player: The player name or UUID

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/players/{player}/heal")
        return SuccessResponse(**response)

    async def kick_player(
        self, player: str, reason: Optional[str] = None
    ) -> SuccessResponse:
        """
        Kick a player from the server.

        Args:
            player: The player name or UUID
            reason: The reason for kicking

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = KickRequest(reason=reason)
        response = await self.client._post(
            f"/api/players/{player}/kick", request.__dict__
        )
        return SuccessResponse(**response)

    async def kill_player(self, player: str) -> SuccessResponse:
        """
        Kill a player.

        Args:
            player: The player name or UUID

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/players/{player}/kill")
        return SuccessResponse(**response)

    async def starve_player(self, player: str) -> SuccessResponse:
        """
        Starve a player by setting their food level to zero.

        Args:
            player: The player name or UUID

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/players/{player}/starve")
        return SuccessResponse(**response)

    async def teleport_player(
        self, player: str, world: str, x: float, y: float, z: float
    ) -> SuccessResponse:
        """
        Teleport a player to a specific location.

        Args:
            player: The player name or UUID
            world: The world name
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = TeleportRequest(world=world, x=x, y=y, z=z)
        response = await self.client._post(
            f"/api/players/{player}/teleport", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_food_level(self, player: str) -> FoodLevelDto:
        """
        Get the player's food level.

        Args:
            player: The player name or UUID

        Returns:
            FoodLevelDto: Player food level

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/foodlevel")
        return FoodLevelDto(**response)

    async def set_food_level(self, player: str, food_level: int) -> SuccessResponse:
        """
        Set the player's food level.

        Args:
            player: The player name or UUID
            food_level: The food level to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = FoodLevelRequest(foodLevel=food_level)
        response = await self.client._patch(
            f"/api/players/{player}/foodlevel", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_health(self, player: str) -> HealthDto:
        """
        Get the player's health.

        Args:
            player: The player name or UUID

        Returns:
            HealthDto: Player health

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/health")
        return HealthDto(**response)

    async def set_health(self, player: str, health: float) -> SuccessResponse:
        """
        Set the player's health.

        Args:
            player: The player name or UUID
            health: The health value to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = HealthRequest(health=health)
        response = await self.client._patch(
            f"/api/players/{player}/health", request.__dict__
        )
        return SuccessResponse(**response)

    async def clear_inventory(self, player: str) -> SuccessResponse:
        """
        Clear the player inventory.

        Args:
            player: The player name or UUID

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/players/{player}/inventory/clear")
        return SuccessResponse(**response)

    async def get_inventory(self, player: str) -> PlayerInventoryDto:
        """
        Get the player's inventory.

        Args:
            player: The player name or UUID

        Returns:
            PlayerInventoryDto: Player inventory information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/inventory/get")
        return PlayerInventoryDto(**response)

    async def get_inventory_slot(self, player: str, slot: SlotType) -> SlotDto:
        """
        Get the player's inventory slot.

        Args:
            player: The player name or UUID
            slot: The slot type

        Returns:
            SlotDto: Slot information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(
            f"/api/players/{player}/inventory/slots/{slot}"
        )
        return SlotDto(**response)

    async def set_inventory_slot(
        self, player: str, slot: SlotType, item: str, amount: int
    ) -> SuccessResponse:
        """
        Set the player's inventory slot.

        Args:
            player: The player name or UUID
            slot: The slot type
            item: The item to place in the slot
            amount: The amount of the item

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = SlotRequest(item=item, amount=amount)
        response = await self.client._patch(
            f"/api/players/{player}/inventory/slots/{slot}", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_location(self, player: str) -> LocationDto:
        """
        Get the player's location.

        Args:
            player: The player name or UUID

        Returns:
            LocationDto: Player location information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/location")
        return LocationDto(**response)

    async def get_max_health(self, player: str) -> MaxHealthDto:
        """
        Get the player's max health.

        Args:
            player: The player name or UUID

        Returns:
            MaxHealthDto: Player max health

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/maxhealth")
        return MaxHealthDto(**response)

    async def set_max_health(self, player: str, max_health: float) -> SuccessResponse:
        """
        Set the player's max health.

        Args:
            player: The player name or UUID
            max_health: The max health value to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = MaxHealthRequest(maxHealth=max_health)
        response = await self.client._patch(
            f"/api/players/{player}/maxhealth", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_spawn_point(self, player: str) -> PlayerSpawnPointDto:
        """
        Get the player's spawn point.

        Args:
            player: The player name or UUID

        Returns:
            PlayerSpawnPointDto: Player spawn point information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/players/{player}/spawnpoint")
        return PlayerSpawnPointDto(**response)
