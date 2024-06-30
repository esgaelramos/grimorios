"""Tests for Main Module for the FastAPI-Financial application."""

from fastapi.testclient import TestClient
from src.app import app

# Create a test client for our FastAPI application
client = TestClient(app)


def test_hello_world():
    """Test for the hello world endpoint of the API."""
    expected_response = "Hello Grimorios!"

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == expected_response

