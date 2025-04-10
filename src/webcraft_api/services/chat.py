from src.webcraft_api.models.requests import BroadcastRequest
from src.webcraft_api.models.responses import SuccessResponse
from src.webcraft_api.services.base import BaseService


class ChatService(BaseService):
    """Service for chat-related API endpoints."""

    async def broadcast_all(self, message: str) -> SuccessResponse:
        """
        Broadcast a message to all players and admins on the server.

        Args:
            message: The message to broadcast

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = BroadcastRequest(message=message)
        response = await self.client._post("/api/chat/broadcast/all", request.__dict__)
        return SuccessResponse(**response)

    async def broadcast_ops(self, message: str) -> SuccessResponse:
        """
        Broadcast a message to all admins on the server.

        Args:
            message: The message to broadcast

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = BroadcastRequest(message=message)
        response = await self.client._post("/api/chat/broadcast/ops", request.__dict__)
        return SuccessResponse(**response)

    async def broadcast_players(self, message: str) -> SuccessResponse:
        """
        Broadcast a message to all players (non admins players) on the server.

        Args:
            message: The message to broadcast

        Returns:
            SuccessResponse: Success response

        Raises:
            APIException: If the request fails
        """
        request = BroadcastRequest(message=message)
        response = await self.client._post(
            "/api/chat/broadcast/players", request.__dict__
        )
        return SuccessResponse(**response)
