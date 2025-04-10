from typing import Any, Dict, Optional

import aiohttp

from src.webcraft_api.exceptions import APIException
from src.webcraft_api.models.requests import AuthenticateRequest
from src.webcraft_api.services.admin import AdminService
from src.webcraft_api.services.api import ApiService
from src.webcraft_api.services.banlist import BanlistService
from src.webcraft_api.services.chat import ChatService
from src.webcraft_api.services.entities import EntitiesService
from src.webcraft_api.services.items import ItemsService
from src.webcraft_api.services.ping import PingService
from src.webcraft_api.services.players import PlayersService
from src.webcraft_api.services.plugins import PluginsService
from src.webcraft_api.services.server import ServerService
from src.webcraft_api.services.whitelist import WhitelistService
from src.webcraft_api.services.worlds import WorldsService


class WebCraftAPI:
    """
    WebCraftAPI Client

    A comprehensive async client for interacting with the WebCraftAPI
    for Minecraft servers.
    """

    def __init__(self, base_url: str, session: Optional[aiohttp.ClientSession] = None):
        """
        Initialize the WebCraftAPI client.

        Args:
            base_url: The base URL of the WebCraftAPI server
            session: Optional existing aiohttp ClientSession
        """
        self.base_url = base_url.rstrip("/")
        self.token: Optional[str] = None
        self._session: Optional[aiohttp.ClientSession] = session
        self._is_session_owner = session is None

        # Initialize services
        self.admin = AdminService(self)
        self.api = ApiService(self)
        self.banlist = BanlistService(self)
        self.chat = ChatService(self)
        self.entities = EntitiesService(self)
        self.items = ItemsService(self)
        self.ping = PingService(self)
        self.players = PlayersService(self)
        self.plugins = PluginsService(self)
        self.server = ServerService(self)
        self.whitelist = WhitelistService(self)
        self.worlds = WorldsService(self)

    async def __aenter__(self):
        """Context manager entry point."""
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        if self._is_session_owner:
            await self.close()

    async def open(self):
        """Initialize the HTTP session if it does not already exist."""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={"Content-Type": "application/json"}
            )
            self._is_session_owner = True
            if self.token:
                self._update_auth_header()

    async def close(self):
        """Close the HTTP session if owned by this instance."""
        if self._is_session_owner and self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    async def authenticate(self, username: str, password: str) -> str:
        """
        Authenticate with the API and get a JWT token.

        Args:
            username: The username for authentication
            password: The password for authentication

        Returns:
            str: The JWT token

        Raises:
            APIException: If authentication fails
        """
        await self.open()

        auth_request = AuthenticateRequest(username=username, password=password)

        if not self._session:
            raise RuntimeError("Session not initialized")

        async with self._session.post(
            f"{self.base_url}/api/authenticate", json=auth_request.__dict__
        ) as response:
            if response.status == 200:
                text = await response.text()
                self.token = text.strip('"')
                self._update_auth_header()
                return self.token
            else:
                try:
                    error = await response.json()
                    message = error.get("message", "Unknown error")
                except Exception:
                    message = f"Authentication failed with status {response.status}"
                raise APIException(message, response.status)

    def _update_auth_header(self):
        """Update the session headers with the authentication token."""
        if self._session and self.token:
            self._session.headers.update({"Authorization": f"Bearer {self.token}"})

    async def _check_session(self):
        """Ensure session is open and initialized."""
        await self.open()
        if not self._session:
            raise RuntimeError("Session not initialized")

    async def _get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a GET request to the API.

        Args:
            endpoint: The API endpoint
            params: Query parameters

        Returns:
            dict: The response data

        Raises:
            APIException: If the request fails
        """
        await self._check_session()
        async with self._session.get(  # type: ignore
            f"{self.base_url}{endpoint}", params=params
        ) as response:
            if response.status >= 400:
                try:
                    error = await response.json()
                    message = error.get(
                        "message", f"API request failed with status {response.status}"
                    )
                except Exception:
                    message = f"API request failed with status {response.status}"
                raise APIException(message, response.status)

            return await response.json()

    async def _post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a POST request to the API.

        Args:
            endpoint: The API endpoint
            data: Request data

        Returns:
            dict: The response data

        Raises:
            APIException: If the request fails
        """
        await self._check_session()
        async with self._session.post(  # type: ignore
            f"{self.base_url}{endpoint}", json=data
        ) as response:
            if response.status >= 400:
                try:
                    error = await response.json()
                    message = error.get(
                        "message", f"API request failed with status {response.status}"
                    )
                except Exception:
                    message = f"API request failed with status {response.status}"
                raise APIException(message, response.status)

            if response.status == 200:
                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    return await response.json()
                else:
                    # Handle text responses by wrapping them
                    text = await response.text()
                    return {"response": text}

            return {}

    async def _patch(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a PATCH request to the API.

        Args:
            endpoint: The API endpoint
            data: Request data

        Returns:
            dict: The response data

        Raises:
            APIException: If the request fails
        """
        await self._check_session()

        async with self._session.patch(  # type: ignore
            f"{self.base_url}{endpoint}", json=data
        ) as response:
            if response.status >= 400:
                try:
                    error = await response.json()
                    message = error.get(
                        "message", f"API request failed with status {response.status}"
                    )
                except Exception:
                    message = f"API request failed with status {response.status}"
                raise APIException(message, response.status)

            return await response.json()
