"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from app.models import *


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    user = User('Duc Bang', 'abc@gmail.com', 'admin123', '123456')
    assert user.name == 'Duc Bang'
    assert user.email == 'abc@gmail.com'
    assert user.username == 'admin123'
    assert user.password != '123456'
    assert user.user_role == UserRole.USER
    assert user.__repr__() == '<User: admin123>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.name == 'Duc Bang'
    assert new_user.email == 'abc@gmail.com'
    assert new_user.username == 'admin123'
    assert new_user.password != '123456'
    assert new_user.user_role == UserRole.USER


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('1234567')
    assert new_user.password != '1234567'
    assert new_user.is_correct_password('1234567')
    assert not new_user.is_correct_password('123456')
    assert not new_user.is_correct_password('FlaskIsAwesome')


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 10
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '10'
