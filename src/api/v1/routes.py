"""Routes for API v1."""""

from fastapi import APIRouter

from .endpoints import (
    hello_world, request
)


router = APIRouter()

router.include_router(
    hello_world.router, prefix="", tags=["hello_world"]
)

router.include_router(
    request.router, prefix="", tags=["request"]
)
