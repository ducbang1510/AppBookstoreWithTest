def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(username='admin123', password='1234567'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(username='admin123',
                                          password='123456'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for logging in, admin123!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    # assert b'Login' not in response.data
    # assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    # assert b'Login' in response.data
    # assert b'Register' in response.data


def test_login_already_logged_in(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(username='admin123', password='1234567'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!  Redirecting to your User Profile page...' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    # assert b'Login' not in response.data
    # assert b'Register' not in response.data


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(name='Anh Khoa',
                                          email='Khoa123@gmail.com',
                                          username='khoa123',
                                          password='khoa123',
                                          confirm='khoa123'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, khoa123!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    # assert b'Login' not in response.data
    # assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_invalid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(name='Van Trung',
                                          email='trung123@gmail.com',
                                          username='trung123',
                                          password='trung123',
                                          confirm='trung1234'),  # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, trung123!' not in response.data
    assert b'[This field is required.]' not in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_duplicate_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    # Register the new account
    test_client.post('/register',
                     data=dict(name='Van Trung',
                               email='trung123@gmail.com',
                               username='trung123',
                               password='trung123',
                               confirm='trung123'),
                     follow_redirects=True)
    # Try registering with the same email address
    response = test_client.post('/register',
                                data=dict(name='Phan Van Trung',
                                          email='trung1234@gmail.com',
                                          username='trung123',
                                          password='trung1234',
                                          confirm='trung1234'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already registered!  Redirecting to your User Profile page...' in response.data
    assert b'Thanks for registering, trung123!' not in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    # assert b'Login' not in response.data
    # assert b'Register' not in response.data
