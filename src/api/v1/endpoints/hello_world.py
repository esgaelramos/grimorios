"""EndPoints for Hello World."""""

from fastapi import APIRouter, HTTPException
from schemas.responses_schema import SuccessResponse
from schemas.responses_schema import ErrorResponse


router = APIRouter()


@router.get("/hello-world", response_model=SuccessResponse)
async def hello_world():
    """Hello World EndPoint."""
    return {
        "success": True,
        "data": {"from Grimorios": "to the World"}
    }


@router.get("/custom-error", response_model=ErrorResponse)
async def custom_error():
    """Raise Custom Error EndPoint."""
    raise HTTPException(status_code=500, detail="Custom Unexpected Error")
