"""Tests for Schemas Validating Responses Data."""

from src.models.request_model import Request, Grimorio


def test_request_model_attributes():
    """Test the attributes of the Request model."""
    request_attrs = Request.__table__.columns.keys()
    assert 'id' in request_attrs
    assert 'name' in request_attrs
    assert 'last_name' in request_attrs
    assert 'identification' in request_attrs
    assert 'age' in request_attrs
    assert 'magic_affinity' in request_attrs
    assert 'status' in request_attrs
    assert 'is_deleted' in request_attrs


def test_request_model_initialization():
    """Test initialization of Request model."""
    request = Request(
        name='John',
        last_name='Doe',
        identification='ID123456',
        age=25,
        magic_affinity='FIRE',
        status='Pending',
        is_deleted=False
    )

    assert request.name == 'John'
    assert request.last_name == 'Doe'
    assert request.identification == 'ID123456'
    assert request.age == 25
    assert request.magic_affinity == 'FIRE'
    assert request.status == 'Pending'
    assert request.is_deleted is False


def test_request_model_id_autoincrement():
    """Test if 'id' is set as autoincrement primary key."""
    id_column = Request.__table__.columns['id']
    assert id_column.primary_key
    assert id_column.autoincrement


def test_grimorio_model_attributes():
    """Test the attributes of the Grimorio model."""
    grimorio_attrs = Grimorio.__table__.columns.keys()
    assert 'id' in grimorio_attrs
    assert 'type_trebol' in grimorio_attrs
    assert 'request_id' in grimorio_attrs


def test_grimorio_model_initialization():
    """Test initialization of Grimorio model."""
    grimorio = Grimorio(
        type_trebol='Tres Hojas',
        request_id=1
    )

    assert grimorio.type_trebol == 'Tres Hojas'
    assert grimorio.request_id == 1


def test_grimorio_model_id_autoincrement():
    """Test if 'id' is set as autoincrement primary key."""
    id_column = Grimorio.__table__.columns['id']
    assert id_column.primary_key
    assert id_column.autoincrement
