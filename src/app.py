"""Draft FastAPI app with Mangum adapter."""

import os
import sys
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from mangum import Mangum

# Configure the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.config import Settings  # noqa
from core.database import init_db  # noqa
from api.v1.routes import router as v1_router  # noqa
from schemas.responses_schema import ErrorResponse  # noqa


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Load and Instance the Wrapper Settings
settings = Settings()

# Initialize the database
init_db()

# Init the FastAPI application
app = FastAPI()

# Register the API routers (for versions)
app.include_router(v1_router, prefix="/v1")


# Handle Exceptions with custom Response
@app.exception_handler(HTTPException)
async def exception_handler(request, exc):
    """Handle Exceptions with custom Response."""
    logging.error(exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            success=False,
            message=exc.detail,
        ).model_dump()
    )


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"  # pragma: no cover # noqa
    uvicorn.run(
        uvicorn_app, host="0.0.0.0", port=8000, reload=True
    )  # pragma: no cover
