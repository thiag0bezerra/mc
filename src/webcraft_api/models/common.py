from pydantic import BaseModel


class Position(BaseModel):
    """Represents a position in a Minecraft world."""

    x: float
    y: float
    z: float


class Location(BaseModel):
    """Represents a location in a Minecraft world including world name."""

    world: str
    x: float
    y: float
    z: float
