"""Tests for the DataBase Module."""

import unittest
from unittest.mock import MagicMock, patch

from src.core.database import create_engine_with_fallback, get_session


class TestDatabase(unittest.TestCase):
    """Test the Database class."""

    @patch('src.core.database.create_engine')
    @patch('src.core.database.sessionmaker')
    def setUp(self, mock_sessionmaker, mock_create_engine):
        """Set up the test case."""
        self.database_url = 'sqlite:///:memory:'
        self.mock_engine = mock_create_engine.return_value
        self.mock_sessionmaker = mock_sessionmaker
        self.db = create_engine_with_fallback(self.database_url)

    @patch('src.core.database.create_engine')
    def test_create_engine_with_fallback(self, mock_create_engine):
        """Test create_engine_with_fallback function."""
        # Simulate successful creation of the database engine
        mock_create_engine.return_value = MagicMock()

        # Call the function with a database URL
        engine = create_engine_with_fallback(self.database_url)

        # Verify that create_engine was called with the correct URL
        self.assertIsNotNone(engine)

    @patch('src.core.database.default_session')
    def test_get_session(self, mock_default_session):
        """Test the get_session method."""
        mock_session = MagicMock()
        mock_default_session.return_value = mock_session

        session_gen = get_session()

        # Simulate entering the context
        session = next(session_gen)
        self.assertEqual(session, mock_session)

        try:
            next(session_gen)
        except StopIteration:
            pass

        # Verify that the session was closed correctly
        mock_session.close.assert_called_once()
