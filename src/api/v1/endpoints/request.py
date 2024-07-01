"""EndPoints for Request."""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_session
from services.request_service import RequestService
from schemas.request_schema import (
    RequestCreate, RequestUpdate, RequestResponse, Grimorio
)

router = APIRouter()


def get_request_service(db: Session = Depends(get_session)):
    """Get Request Service."""
    return RequestService(db)


@router.post("/solicitud", response_model=RequestResponse)
def create_new_request(
    request: RequestCreate,
    service: RequestService = Depends(get_request_service)
):
    """Create a New Request."""
    return service.create_request(request)


@router.put("/solicitud/{id}", response_model=RequestResponse)
def update_existing_request(
    id: int, request: RequestUpdate,
    service: RequestService = Depends(get_request_service)
):
    """Update Existing Request."""
    return service.update_request(id, request)


@router.patch("/solicitud/{id}/estatus")
def update_status(
    id: int, status: str,
    service: RequestService = Depends(get_request_service)
):
    """Update Request Status."""
    return service.update_request_status(id, status)


@router.get("/solicitudes", response_model=List[RequestResponse])
def get_requests(
    service: RequestService = Depends(get_request_service)
):
    """Get All Requests."""
    return service.get_all_requests()


@router.delete("/solicitud/{id}")
def remove_request(
    id: int,
    service: RequestService = Depends(get_request_service)
):
    """Remove Request."""
    service.delete_request(id)
    return {"msg": "Solicitud eliminada"}


@router.get("/asignaciones", response_model=List[Grimorio])
def get_grimorios(
    service: RequestService = Depends(get_request_service)
):
    """Get All Grimorios."""
    return service.get_all_grimorios()
