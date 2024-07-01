"""Services for CRUD operations on Request Model."""

import random

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.request_model import Request, Grimorio
from schemas.request_schema import RequestCreate, RequestUpdate


class RequestService:
    """Services for CRUD operations on Request Model."""

    def __init__(self, db: Session):
        """Init Constructor for RequestService."""
        self.db = db

    def create_request(self, request: RequestCreate):
        """Validate and Create a Request."""
        self._validate_request_data(request)

        new_request = Request(**request.model_dump())
        self.db.add(new_request)
        self.db.commit()
        self.db.refresh(new_request)
        return new_request

    def update_request(self, request_id: int, request: RequestUpdate):
        """Validate and Update a Request."""
        db_request = self._get_request_by_id(request_id)

        # Update the Request with the new data
        for key, value in request.model_dump().items():
            setattr(db_request, key, value)

        self.db.commit()
        self.db.refresh(db_request)
        return db_request

    def update_request_status(self, request_id: int, status: str):
        """Update the status of a Request."""
        db_request = self._get_request_by_id(request_id)
        db_request.status = status
        self.db.commit()
        return db_request

    def get_all_requests(self):
        """Get all Requests."""
        return self.db.query(Request).filter(Request.is_deleted == False).all()  # noqa

    def get_request(self, request_id: int):
        """Get a specific Request by ID."""
        return self._get_request_by_id(request_id)

    def delete_request(self, request_id: int):
        """Logically delete a Request."""
        db_request = self._get_request_by_id(request_id)
        db_request.is_deleted = True
        self.db.commit()

    def assign_grimorio(self, request_id: int):
        """Assign a Grimorio to a Request."""
        tipo_trebol = self._random_grimorio_type()

        new_grimorio = Grimorio(type_trebol=tipo_trebol, request_id=request_id)
        self.db.add(new_grimorio)
        self.db.commit()
        self.db.refresh(new_grimorio)
        return new_grimorio

    def get_all_grimorios(self):
        """Get all Grimorios."""
        return self.db.query(Grimorio).all()

    def _validate_request_data(self, request: RequestCreate):
        """Validate the Request data."""
        if not (request.name.isalpha() and request.last_name.isalpha()):
            raise HTTPException(
                status_code=400,
                detail="Nombre y Apellido deben contener solo letras."
            )

        if not (
            0 < len(request.identification) <= 10
            and request.identification.isalnum()
        ):
            raise HTTPException(
                status_code=400,
                detail="Identificación inválida."
            )

        if not (0 <= request.age <= 99):
            raise HTTPException(status_code=400, detail="Edad inválida.")

    def _get_request_by_id(self, request_id: int):
        """Get a Request by ID."""
        db_request = self.db.query(Request)\
            .filter(Request.id == request_id, Request.is_deleted == False).first()  # noqa
        if not db_request:
            raise HTTPException(status_code=404, detail="Solicitud not found.")
        return db_request

    def _random_grimorio_type(self):
        """Get a random Grimorio type."""
        tipos_trebol = [
            "Una Hoja", "Dos Hojas", "Tres Hojas",
            "Cuatro Hojas", "Cinco Hojas"
        ]
        ponderaciones = [0.5, 0.3, 0.15, 0.04, 0.01]
        return random.choices(tipos_trebol, weights=ponderaciones, k=1)[0]
