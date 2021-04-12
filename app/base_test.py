from flask_testing import TestCase
from app import create_app, db


class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""

    def create_app(self):
        app = create_app('test_app.cfg')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()