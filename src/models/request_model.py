"""Models for the User Table in the DataBase."""

from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class Request(Base):
    """Model for the User Table in the DataBase."""

    __tablename__ = "requests"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    last_name = Column(String(20))
    identification = Column(String(10))
    age = Column(Integer)
    magic_affinity = Column(String(20))
    status = Column(String(20), default="Pending")
    is_deleted = Column(Boolean, default=False)


class Grimorio(Base):
    """Model for the Grimorio Table in the DataBase."""

    __tablename__ = "grimorios"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    type_trebol = Column(String(20))
    request_id = Column(Integer)
