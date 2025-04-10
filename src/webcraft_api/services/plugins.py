from src.webcraft_api.models.responses import PluginDto, PluginNamesDto
from src.webcraft_api.services.base import BaseService


class PluginsService(BaseService):
    """Service for plugin-related API endpoints."""

    async def get_all_plugins(self) -> PluginNamesDto:
        """
        Get a list of all the plugins on the server.

        Returns:
            PluginNamesDto: List of plugin names

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get("/api/plugins")
        return PluginNamesDto(**response)

    async def get_plugin_info(self, plugin: str) -> PluginDto:
        """
        Get information about a specific plugin.

        Args:
            plugin: The plugin name

        Returns:
            PluginDto: Plugin information

        Raises:
            APIException: If the request fails
        """
        response = await self.client._get(f"/api/plugins/{plugin}")
        return PluginDto(**response)
