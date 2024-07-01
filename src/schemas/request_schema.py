"""Schemas for Validating and Standard Requests."""

from enum import Enum

from pydantic import BaseModel, Field


class MagicType(str, Enum):
    """Enum for the Magic Type of the User."""

    DARK = "Dark"
    LIGHT = "Light"
    FIRE = "Fire"
    WATER = "Water"
    WIND = "Wind"
    EARTH = "Earth"


class RequestCreate(BaseModel):
    """Schema for Creating a Request."""

    name: str = Field(..., max_length=20)
    last_name: str = Field(..., max_length=20)
    identification: str = Field(..., max_length=10)
    age: int = Field(..., ge=0, le=99)
    magic_affinity: MagicType


class RequestUpdate(BaseModel):
    """Schema for Updating a Request."""

    name: str = Field(..., max_length=20)
    last_name: str = Field(..., max_length=20)
    identification: str = Field(..., max_length=10)
    age: int = Field(..., ge=0, le=99)
    magic_affinity: MagicType


class RequestResponse(BaseModel):
    """Schema for Returning a Request."""

    id: int
    name: str
    last_name: str
    identification: str
    age: int
    magic_affinity: MagicType
    status: str = Field(default="Pending")


class Grimorio(BaseModel):
    """Schema for Returning a Grimorio."""

    id: int
    type_trebol: str
    request_id: int
