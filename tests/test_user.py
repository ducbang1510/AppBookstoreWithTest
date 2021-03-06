from flask import url_for
from flask_login import current_user

from tests.base_test import BaseTestCase, create_data
from app.models import *


class UserViewsTests(BaseTestCase):
    def test_login_page(self):
        with self.client:
            response = self.client.get('/login')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'Login' in response.data)
            self.assertTrue(b'Username' in response.data)
            self.assertTrue(b'Password' in response.data)

    def test_valid_login(self):
        create_data()
        with self.client:
            response = self.client.post("/login", data=dict(username='admin123', password='123456'),
                                        follow_redirects=True)

            self.assertTrue(response.status_code == 200)
            self.assertTrue(current_user.username == "admin123")
            self.assertTrue(current_user.is_authenticated)
            self.assertTrue(current_user.is_active)
            self.assertFalse(current_user.is_anonymous)

    def test_valid_login_can_logout(self):
        create_data()
        with self.client:
            response = self.client.post("/login", data=dict(username='admin123', password='123456'),
                                        follow_redirects=True)

            assert response.status_code == 200
            self.assertTrue(current_user.username == "admin123")

            response = self.client.get("/logout", follow_redirects=True)

            assert response.status_code == 200
            self.assertTrue(current_user.is_anonymous)

    def test_login_already_logged_in(self):
        create_data()
        with self.client:
            self.client.post("/login", data=dict(username='admin123', password='123456'),
                             follow_redirects=True)

            self.client.post("/login", data=dict(username='admin456', password='654321'),
                             follow_redirects=True)

            self.assertTrue(current_user.username == "admin123")
            self.assertFalse(current_user.username == "admin456")

    def test_invalid_login(self):
        create_data()
        with self.client:
            self.client.post("/login", data=dict(username='admin123', password='12345671'),
                             follow_redirects=True)

            self.assertTrue(current_user.is_anonymous)

    def test_valid_registration(self):
        create_data()
        with self.client:
            response = self.client.post("/register",
                                        data=dict(name_dk='Anh Khoa',
                                                  email_dk='Khoa123@gmail.com',
                                                  username_dk='khoa123',
                                                  password_dk='khoa123',
                                                  confirm='khoa123'),
                                        follow_redirects=True)

            self.assertTrue(response.status_code == 200)
            self.assertTrue(current_user.username == "khoa123")
            self.assertTrue(current_user.is_authenticated)
            self.assertTrue(current_user.is_active)
            self.assertFalse(current_user.is_anonymous)

    def test_invalid_registration(self):
        create_data()
        with self.client:
            response = self.client.post("/register",
                                        data=dict(name='Anh Khoa',
                                                  email='Khoa123@gmail.com',
                                                  username='khoa123',
                                                  password='khoa123',
                                                  confirm='khoa12342313'),  # Does NOT match!
                                        follow_redirects=True)

            assert response.status_code == 200
            self.assertFalse(current_user.is_authenticated)
            self.assertFalse(current_user.is_active)
            self.assertTrue(current_user.is_anonymous)

    def test_duplicate_registration(self):
        create_data()
        with self.client:
            response = self.client.post("/register",
                                        data=dict(name='Tran Duc Bang',
                                                  email='bang123@gmail.com',
                                                  username='admin456',  # Duplicate username
                                                  password='123456',
                                                  confirm='123456'),
                                        follow_redirects=True)

            assert b'Logout' not in response.data
            assert b'Login' in response.data
            assert b'Register' in response.data
            assert response.status_code == 200
            self.assertFalse(current_user.is_authenticated)
            self.assertFalse(current_user.is_active)
            self.assertTrue(current_user.is_anonymous)


# Run unittest
# python -m unittest -v to run all tests
# python -m unittest filepath to run file test
