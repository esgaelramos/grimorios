"""Routes for API v1."""""

from fastapi import APIRouter

from .endpoints import (
    hello_world
)


router = APIRouter()

router.include_router(
    hello_world.router, prefix="", tags=["hello_world"]
)
