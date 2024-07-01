"""Module `database` for setup the connection."""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from .config import Settings


# Instance the Wrapper Settings
settings = Settings()


def create_engine_with_fallback(database_url: str):
    """Create the database engine or fallback to SQLite."""
    connect_args = {}
    if "sqlite" in database_url:
        connect_args["check_same_thread"] = False
    try:
        logging.info(f"Connecting to the database {database_url}")
        return create_engine(
            database_url, connect_args=connect_args,
            poolclass=StaticPool if "sqlite" in database_url else None
        )
    except Exception as e:  # pragma: no cover
        logging.warning(f"Database connection FAIL: {e}. Using db in-memory.")
        connect_args["check_same_thread"] = False
        return create_engine(
            'sqlite:///:memory:',
            poolclass=StaticPool,
            connect_args=connect_args
        )

# Use SQLite in-memory if TEST environment variable is set
database_url = settings.DATABASE_URL  # noqa
if os.getenv("TEST"):
    database_url = 'sqlite:///:memory:'

# Create the database engine or fallback to SQLite
engine = create_engine_with_fallback(database_url)  # noqa
default_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def get_session():
    """Provide a transactional scope around a series of operations."""
    db_session = default_session()
    try:
        yield db_session
    finally:
        db_session.close()


# Instance the Base for use in the Models
Base = declarative_base()


def init_db():
    """Initialize the database and create all tables."""
    Base.metadata.create_all(bind=engine)
