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
    user = User('Duc Bang', 'abc@gmail.com', 'bang123', '654321')
    assert user.name == 'Duc Bang'
    assert user.email == 'abc@gmail.com'
    assert user.username == 'bang123'
    assert user.password != '654321'
    assert user.user_role == UserRole.USER
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
