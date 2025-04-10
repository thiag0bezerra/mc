from typing import List, Optional

from pydantic import BaseModel


class AuthenticateRequest(BaseModel):
    """Request to authenticate with the API."""

    username: str
    password: str


class BanIpRequest(BaseModel):
    """Request to ban an IP address."""

    ip: str
    reason: Optional[str] = None
    expiration: Optional[str] = None
    source: Optional[str] = None


class BanPlayerRequest(BaseModel):
    """Request to ban a player."""

    player: str
    reason: Optional[str] = None
    expiration: Optional[str] = None
    source: Optional[str] = None


class BroadcastRequest(BaseModel):
    """Request to broadcast a message."""

    message: str


class CustomNameRequest(BaseModel):
    """Request to set a custom name for an entity."""

    customName: str


class DropItemsRequest(BaseModel):
    """Request to drop items in the world."""

    item: str
    amount: int
    x: int
    y: int
    z: int


class FoodLevelRequest(BaseModel):
    """Request to set a player's food level."""

    foodLevel: int


class GetBlockRequest(BaseModel):
    """Request to get block information."""

    x: int
    y: int
    z: int


class GetBlocksRequest(BaseModel):
    """Request to get information about multiple blocks."""

    blocks: List[GetBlockRequest]


class GiveRequest(BaseModel):
    """Request to give items to a player."""

    item: str
    amount: int


class HealthRequest(BaseModel):
    """Request to set an entity's health."""

    health: float


class KickRequest(BaseModel):
    """Request to kick a player from the server."""

    reason: Optional[str] = None


class MaxHealthRequest(BaseModel):
    """Request to set an entity's maximum health."""

    maxHealth: float


class SetBlockRequest(BaseModel):
    """Request to set a block in the world."""

    block: str
    x: int
    y: int
    z: int


class SetBlocksRequest(BaseModel):
    """Request to set multiple blocks in the world."""

    blocks: List[SetBlockRequest]


class SetDifficultyRequest(BaseModel):
    """Request to set world difficulty."""

    difficulty: str


class SetSpawnPointRequest(BaseModel):
    """Request to set world spawn point."""

    x: int
    y: int
    z: int


class SetTimeRequest(BaseModel):
    """Request to set world time."""

    time: int


class SetWeatherRequest(BaseModel):
    """Request to set world weather."""

    weather: str
    duration: int


class SlotRequest(BaseModel):
    """Request to set a player's inventory slot."""

    item: str
    amount: int


class SpawnMobRequest(BaseModel):
    """Request to spawn a mob in the world."""

    name: str
    world: str
    x: int
    y: int
    z: int


class TeleportRequest(BaseModel):
    """Request to teleport a player."""

    world: str
    x: float
    y: float
    z: float


class UnwhitelistPlayerRequest(BaseModel):
    """Request to remove a player from the whitelist."""

    name: str


class WhitelistPlayerRequest(BaseModel):
    """Request to add a player to the whitelist."""

    name: str
