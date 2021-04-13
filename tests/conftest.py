import pytest
from app import create_app, db
from app.models import *


@pytest.fixture(scope='module')
def new_user():
    user = User(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test_app.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456')
    user2 = User(name='Tran Bang', email='abdc@gmail.com', username='admin456', password='654321')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.session.remove()
    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(username='admin123', password='123456'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)

# Run pytest
# python -m pytest -v to run all tests
# python -m pytest -v filepath to run 1 file test
