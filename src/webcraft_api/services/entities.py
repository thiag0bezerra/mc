from src.webcraft_api.models.requests import (
    CustomNameRequest,
    HealthRequest,
    MaxHealthRequest,
    SpawnMobRequest,
)
from src.webcraft_api.models.responses import (
    CustomNameDto,
    EntityDto,
    HealthDto,
    MaxHealthDto,
    SpawnableEntitiesDto,
)
from src.webcraft_api.services.base import BaseService


class EntitiesService(BaseService):
    """Service for entity-related API endpoints."""

    async def get_spawnable_mobs(self) -> SpawnableEntitiesDto:
        """
        Get a list of all spawnable mobs.

        Returns:
            SpawnableEntitiesDto: List of spawnable entities

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/entities/mobs/spawnable")
        return SpawnableEntitiesDto(**response)

    async def spawn_mob(self, request: SpawnMobRequest) -> EntityDto:
        """
        Spawn a mob at the given coordinates and world.

        Args:
            request: The spawn mob request

        Returns:
            EntityDto: The spawned entity info

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post("/api/entities/mobs/spawn", request.__dict__)
        return EntityDto(**response)

    async def get_entity(self, entity_id: str) -> EntityDto:
        """
        Get information about a specific entity.

        Args:
            entity_id: The entity ID

        Returns:
            EntityDto: Entity information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/entities/{entity_id}")
        return EntityDto(**response)

    async def heal_entity(self, entity_id: str) -> EntityDto:
        """
        Heal an entity.

        Args:
            entity_id: The entity ID

        Returns:
            EntityDto: Updated entity information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/entities/{entity_id}/heal")
        return EntityDto(**response)

    async def kill_entity(self, entity_id: str) -> EntityDto:
        """
        Kill an entity.

        Args:
            entity_id: The entity ID

        Returns:
            EntityDto: Updated entity information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._post(f"/api/entities/{entity_id}/kill")
        return EntityDto(**response)

    async def get_entity_custom_name(self, entity_id: str) -> CustomNameDto:
        """
        Get the entity custom name.

        Args:
            entity_id: The entity ID

        Returns:
            CustomNameDto: Entity custom name

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/entities/{entity_id}/customname")
        return CustomNameDto(**response)

    async def set_entity_custom_name(
        self, entity_id: str, custom_name: str
    ) -> EntityDto:
        """
        Set the entity custom name.

        Args:
            entity_id: The entity ID
            custom_name: The custom name to set

        Returns:
            EntityDto: Updated entity information

        Raises:
            APIException: If the request fails
        """
        request = CustomNameRequest(customName=custom_name)
        response = await self.client._patch(
            f"/api/entities/{entity_id}/customname", request.__dict__
        )
        return EntityDto(**response)

    async def get_entity_health(self, entity_id: str) -> HealthDto:
        """
        Get the entity health.

        Args:
            entity_id: The entity ID

        Returns:
            HealthDto: Entity health

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/entities/{entity_id}/health")
        return HealthDto(**response)

    async def set_entity_health(self, entity_id: str, health: float) -> EntityDto:
        """
        Set the entity health.

        Args:
            entity_id: The entity ID
            health: The health value to set

        Returns:
            EntityDto: Updated entity information

        Raises:
            APIException: If the request fails
        """
        request = HealthRequest(health=health)
        response = await self.client._patch(
            f"/api/entities/{entity_id}/health", request.__dict__
        )
        return EntityDto(**response)

    async def get_entity_max_health(self, entity_id: str) -> MaxHealthDto:
        """
        Get the entity max health.

        Args:
            entity_id: The entity ID

        Returns:
            MaxHealthDto: Entity max health

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/entities/{entity_id}/maxhealth")
        return MaxHealthDto(**response)

    async def set_entity_max_health(
        self, entity_id: str, max_health: float
    ) -> EntityDto:
        """
        Set the entity max health.

        Args:
            entity_id: The entity ID
            max_health: The max health value to set

        Returns:
            EntityDto: Updated entity information

        Raises:
            APIException: If the request fails
        """
        request = MaxHealthRequest(maxHealth=max_health)
        response = await self.client._patch(
            f"/api/entities/{entity_id}/maxhealth", request.__dict__
        )
        return EntityDto(**response)
