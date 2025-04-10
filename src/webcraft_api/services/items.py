from src.webcraft_api.models.responses import BlockNamesDto, ItemNamesDto
from src.webcraft_api.services.base import BaseService


class ItemsService(BaseService):
    """Service for item/block-related API endpoints."""

    async def get_all_blocks(self) -> BlockNamesDto:
        """
        Get a list of all minecraft blocks.

        Returns:
            BlockNamesDto: List of block names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/blocks")
        return BlockNamesDto(**response)

    async def get_all_items(self) -> ItemNamesDto:
        """
        Get a list of all minecraft items.

        Returns:
            ItemNamesDto: List of item names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/items")
        return ItemNamesDto(**response)
