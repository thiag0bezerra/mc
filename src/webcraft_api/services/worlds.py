from typing import List, Union

from src.webcraft_api.models.enums import DifficultyType, WeatherType
from src.webcraft_api.models.requests import (
    DropItemsRequest,
    GetBlockRequest,
    GetBlocksRequest,
    SetBlockRequest,
    SetBlocksRequest,
    SetDifficultyRequest,
    SetSpawnPointRequest,
    SetTimeRequest,
    SetWeatherRequest,
)
from src.webcraft_api.models.responses import (
    BlockDto,
    BlocksDto,
    DifficultyDto,
    SeedDto,
    SpawnPointDto,
    SuccessResponse,
    TimeDto,
    WeatherDto,
    WorldDto,
    WorldNamesDto,
)
from src.webcraft_api.services.base import BaseService


class WorldsService(BaseService):
    """Service for world-related API endpoints."""

    async def get_all_worlds(self) -> WorldNamesDto:
        """
        Get a list of all worlds present on the server.

        Returns:
            WorldNamesDto: List of world names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/worlds")
        return WorldNamesDto(**response)

    async def get_world_info(self, world_name: str) -> WorldDto:
        """
        Get information about a specific world.

        Args:
            world_name: The world name

        Returns:
            WorldDto: World information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world_name}")
        return WorldDto(**response)

    async def save_world(self, world: str) -> SuccessResponse:
        """
        Save the world.

        Args:
            world: The world name

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/worlds/{world}/save")
        return SuccessResponse(**response)

    async def get_blocks(self, world: str, blocks: List[GetBlockRequest]) -> BlocksDto:
        """
        Get blocks at specific locations.

        Args:
            world: The world name
            blocks: List of block positions to query

        Returns:
            BlocksDto: Block information

        Raises:
            APIException: If the request fails
        """
        request = GetBlocksRequest(blocks=blocks)
        response = await self.client._post(
            f"/api/worlds/{world}/blocks", request.__dict__
        )
        return BlocksDto(**response)

    async def set_blocks(
        self, world: str, blocks: List[SetBlockRequest]
    ) -> SuccessResponse:
        """
        Set blocks in specific locations.

        Args:
            world: The world name
            blocks: List of blocks to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = SetBlocksRequest(blocks=blocks)
        response = await self.client._patch(
            f"/api/worlds/{world}/blocks", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_block(self, world: str, x: int, y: int, z: int) -> BlockDto:
        """
        Get block at a specific location.

        Args:
            world: The world name
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            BlockDto: Block information

        Raises:
            APIException: If the request fails
        """
        request = GetBlockRequest(x=x, y=y, z=z)
        response = await self.client._post(
            f"/api/worlds/{world}/blocks/block", request.__dict__
        )
        return BlockDto(**response)

    async def set_block(
        self, world: str, block: str, x: int, y: int, z: int
    ) -> SuccessResponse:
        """
        Set block at a specific location.

        Args:
            world: The world name
            block: The block name
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = SetBlockRequest(block=block, x=x, y=y, z=z)
        response = await self.client._patch(
            f"/api/worlds/{world}/blocks/block", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_difficulty(self, world: str) -> DifficultyDto:
        """
        Get the difficulty of a specific world.

        Args:
            world: The world name

        Returns:
            DifficultyDto: World difficulty information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world}/difficulty")
        return DifficultyDto(**response)

    async def set_difficulty(
        self, world: str, difficulty: Union[DifficultyType, str]
    ) -> SuccessResponse:
        """
        Set the difficulty of a specific world.

        Args:
            world: The world name
            difficulty: The difficulty to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        if isinstance(difficulty, DifficultyType):
            difficulty = difficulty.value

        request = SetDifficultyRequest(difficulty=difficulty)
        response = await self.client._patch(
            f"/api/worlds/{world}/difficulty", request.__dict__
        )
        return SuccessResponse(**response)

    async def drop_items(
        self, world: str, item: str, amount: int, x: int, y: int, z: int
    ) -> SuccessResponse:
        """
        Drop items at a specific location.

        Args:
            world: The world name
            item: The item to drop
            amount: The amount of items to drop
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = DropItemsRequest(item=item, amount=amount, x=x, y=y, z=z)
        response = await self.client._post(
            f"/api/worlds/{world}/items/drop", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_seed(self, world_name: str) -> SeedDto:
        """
        Get the seed of a specific world.

        Args:
            world_name: The world name

        Returns:
            SeedDto: World seed information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world_name}/seed")
        return SeedDto(**response)

    async def get_spawn_point(self, world: str) -> SpawnPointDto:
        """
        Get the spawn point of a specific world.

        Args:
            world: The world name

        Returns:
            SpawnPointDto: World spawn point information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world}/spawnpoint")
        return SpawnPointDto(**response)

    async def set_spawn_point(
        self, world: str, x: int, y: int, z: int
    ) -> SuccessResponse:
        """
        Set the spawn point of a specific world.

        Args:
            world: The world name
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = SetSpawnPointRequest(x=x, y=y, z=z)
        response = await self.client._patch(
            f"/api/worlds/{world}/spawnpoint", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_time(self, world: str) -> TimeDto:
        """
        Get the time of a specific world.

        Args:
            world: The world name

        Returns:
            TimeDto: World time information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world}/time")
        return TimeDto(**response)

    async def set_time(self, world: str, time: int) -> SuccessResponse:
        """
        Set the time of a specific world.

        Args:
            world: The world name
            time: The time to set

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = SetTimeRequest(time=time)
        response = await self.client._patch(
            f"/api/worlds/{world}/time", request.__dict__
        )
        return SuccessResponse(**response)

    async def get_weather(self, world: str) -> WeatherDto:
        """
        Get the weather of a specific world.

        Args:
            world: The world name

        Returns:
            WeatherDto: World weather information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/worlds/{world}/weather")
        return WeatherDto(**response)

    async def set_weather(
        self, world: str, weather: Union[WeatherType, str], duration: int
    ) -> SuccessResponse:
        """
        Set the weather of a specific world.

        Args:
            world: The world name
            weather: The weather to set
            duration: The duration in ticks

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        if isinstance(weather, WeatherType):
            weather = weather.value

        request = SetWeatherRequest(weather=weather, duration=duration)
        response = await self.client._patch(
            f"/api/worlds/{world}/weather", request.__dict__
        )
        return SuccessResponse(**response)
