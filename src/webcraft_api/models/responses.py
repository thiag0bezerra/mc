from typing import List, Optional

from pydantic import BaseModel

from .common import Position


class ErrorResponse(BaseModel):
    """Error response from the API."""

    status: int
    code: str
    message: str


class SuccessResponse(BaseModel):
    """Success response from the API."""

    status: int
    code: str
    message: str


class AdminDto(BaseModel):
    """Represents an admin player in Minecraft."""

    name: str
    uuid: str


class AdminsDto(BaseModel):
    """List of admin players."""

    admins: List[AdminDto]


class IsAdminDto(BaseModel):
    """Response indicating if a player is an admin."""

    admin: bool


class ApiDto(BaseModel):
    """Information about the API."""

    name: str
    version: str
    authors: List[str]
    description: str
    documentation: str
    website: str


class BannedIpDto(BaseModel):
    """Information about a banned IP address."""

    ip: str
    reason: str
    source: str
    expires: int  # Unix timestamp


class BannedIpsDto(BaseModel):
    """List of banned IP addresses."""

    bannedIps: List[BannedIpDto]


class BannedPlayerDto(BaseModel):
    """Information about a banned player."""

    name: str
    reason: str
    source: str
    expires: int  # Unix timestamp


class BannedPlayersDto(BaseModel):
    """List of banned players."""

    bannedPlayers: List[BannedPlayerDto]


class IsBannedDto(BaseModel):
    """Response indicating if a player or IP is banned."""

    banned: bool


class BlockDto(BaseModel):
    """Information about a block in the world."""

    name: str
    position: Position


class BlocksDto(BaseModel):
    """List of blocks."""

    blocks: List[BlockDto]


class BlockNamesDto(BaseModel):
    """List of available block names."""

    blocks: List[str]


class CustomNameDto(BaseModel):
    """Custom name for an entity."""

    customName: Optional[str] = None


class DifficultyDto(BaseModel):
    """World difficulty setting."""

    difficulty: str


class EntityDto(BaseModel):
    """Information about an entity."""

    id: int
    uniqueId: str
    entityType: str
    x: float
    y: float
    z: float
    world: str
    customName: Optional[str] = None
    isDead: bool = False
    health: float = 0.0
    maxHealth: float = 0.0


class FoodLevelDto(BaseModel):
    """Food level of a player."""

    foodLevel: int


class HealthDto(BaseModel):
    """Health of an entity or player."""

    health: float


class IsWhitelistedDto(BaseModel):
    """Response indicating if a player is whitelisted."""

    whitelisted: bool


class ItemNamesDto(BaseModel):
    """List of available item names."""

    items: List[str]


class LocationDto(BaseModel):
    """Location in a world."""

    # this one deviates from the OpenAPI spec, but the server does not return 'world' in the response
    world: Optional[str] = None
    x: float
    y: float
    z: float


class MaxHealthDto(BaseModel):
    """Maximum health of an entity or player."""

    maxHealth: float


class PingDto(BaseModel):
    """Response to a ping request."""

    response: str


class PlayerCountDto(BaseModel):
    """Count of online and offline players."""

    online: int
    offline: int


class PlayerDto(BaseModel):
    """Detailed information about a player."""

    name: str
    uuid: str
    firstLogin: int
    lastLogin: int
    banned: bool
    op: bool
    whitelisted: bool
    ip: str
    entityID: int
    ping: int
    allowedFlight: bool
    online: bool
    exhaustion: float
    exp: float
    foodLevel: int
    health: float
    level: int
    world: str


class PlayerNamesDto(BaseModel):
    """List of player names."""

    players: List[str]


class PlayerSpawnPointDto(BaseModel):
    """Spawn point of a player."""

    defined: bool
    x: float
    y: float
    z: float


class PluginDto(BaseModel):
    """Information about a server plugin."""

    name: str
    enabled: bool
    version: str
    description: str
    website: str
    authors: List[str]
    contributors: List[str]


class PluginNamesDto(BaseModel):
    """List of plugin names."""

    plugins: List[str]


class SeedDto(BaseModel):
    """World seed."""

    seed: str


class ServerDto(BaseModel):
    """Information about the Minecraft server."""

    maxPlayers: int
    name: str
    version: str
    bukkitVersion: str
    address: str
    port: int
    motd: str


class SlotDto(BaseModel):
    """Information about an inventory slot."""

    slot: str
    item: str
    amount: int


class PlayerInventoryDto(BaseModel):
    """Player's inventory contents."""

    slots: List[SlotDto]


class SpawnPointDto(BaseModel):
    """World spawn point coordinates."""

    x: float
    y: float
    z: float


class SpawnableEntitiesDto(BaseModel):
    """List of entity types that can be spawned."""

    entities: List[str]


class TimeDto(BaseModel):
    """World time information."""

    time: int
    humanReadableTime: str


class WeatherDto(BaseModel):
    """World weather information."""

    weather: str
    duration: int


class WhitelistDto(BaseModel):
    """Whitelist settings."""

    enabled: bool
    enforced: bool


class WhitelistedPlayerDto(BaseModel):
    """Information about a whitelisted player."""

    name: str
    uuid: str


class WhitelistedPlayersDto(BaseModel):
    """List of whitelisted players."""

    whitelistedPlayers: List[WhitelistedPlayerDto]


class WorldDto(BaseModel):
    """Information about a Minecraft world."""

    name: str
    time: float
    difficulty: str
    hardcore: bool
    pvp: bool
    spawnAnimals: bool
    spawnMonsters: bool
    seed: str


class WorldNamesDto(BaseModel):
    """List of world names."""

    worlds: List[str]
