"""Tests for Schemas Validating Responses Data."""

import pytest
from pydantic import ValidationError
from src.schemas.request_schema import (
    RequestCreate, RequestUpdate, RequestResponse, Grimorio, MagicType
)


def test_request_create_validation():
    """Test the RequestCreate Schema."""
    data = {
        "name": "John",
        "last_name": "Doe",
        "identification": "ID123456",
        "age": 25,
        "magic_affinity": "Light"
    }
    request_create = RequestCreate(**data)
    assert request_create.name == data["name"]
    assert request_create.last_name == data["last_name"]
    assert request_create.identification == data["identification"]
    assert request_create.age == data["age"]
    assert request_create.magic_affinity == MagicType.LIGHT


def test_request_create_validation_error():
    """Test the RequestCreate Schema Validation Error."""
    data = {
        "name": "John",
        "last_name": "Doe",
        "identification": "ID123456",
        "age": 150,  # Invalid age
        "magic_affinity": "Fire"
    }
    with pytest.raises(ValidationError):
        RequestCreate(**data)


def test_request_update_validation():
    """Test the RequestUpdate Schema."""
    data = {
        "name": "Jane",
        "last_name": "Smith",
        "identification": "ID654321",
        "age": 30,
        "magic_affinity": "Water"
    }
    request_update = RequestUpdate(**data)
    assert request_update.name == data["name"]
    assert request_update.last_name == data["last_name"]
    assert request_update.identification == data["identification"]
    assert request_update.age == data["age"]
    assert request_update.magic_affinity == MagicType.WATER


def test_request_response_validation():
    """Test the RequestResponse Schema."""
    data = {
        "id": 1,
        "name": "John",
        "last_name": "Doe",
        "identification": "ID123456",
        "age": 25,
        "magic_affinity": "Fire",
        "status": "Approved"
    }
    request_response = RequestResponse(**data)
    assert request_response.id == data["id"]
    assert request_response.name == data["name"]
    assert request_response.last_name == data["last_name"]
    assert request_response.identification == data["identification"]
    assert request_response.age == data["age"]
    assert request_response.magic_affinity == MagicType.FIRE
    assert request_response.status == data["status"]


def test_grimorio_validation():
    """Test the Grimorio Schema."""
    data = {
        "id": 1,
        "type_trebol": "Tres Hojas",
        "request_id": 1
    }
    grimorio = Grimorio(**data)
    assert grimorio.id == data["id"]
    assert grimorio.type_trebol == data["type_trebol"]
    assert grimorio.request_id == data["request_id"]
