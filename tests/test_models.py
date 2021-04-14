from app.models import *
from tests.base_test import BaseTestCase
import unittest


def new_user(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456'):
    return User.create(name=name, email=email, username=username, password=password)


class ModelTests(BaseTestCase):

    def test_new_user(self):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, authenticated, and role fields are defined correctly
        """
        user = new_user()
        self.assertTrue(isinstance(user, User))

        assert user.password != '123456'
        assert user.user_role == UserRole.USER
        assert user.__repr__() == '<User: admin123>'
        assert user.is_authenticated
        assert user.is_active
        assert not user.is_anonymous

    def test_setting_password(self):
        """
        GIVEN an existing User
        WHEN the password for the user is set
        THEN check the password is stored correctly and not as plaintext
        """
        user = new_user()

        user.set_password('1234567')
        assert user.password != '1234567'
        assert user.is_correct_password('1234567')
        assert not user.is_correct_password('123456')
        assert not user.is_correct_password('FlaskIsAwesome')

    def test_user_id(self):
        """
        GIVEN an existing User
        WHEN the ID of the user is defined to a value
        THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
        """
        user = new_user()
        user.id = 10
        assert isinstance(user.get_id(), str)
        assert not isinstance(user.get_id(), int)
        assert user.get_id() == '10'


if __name__ == '__main__':
    unittest.main(verbosity=2)
