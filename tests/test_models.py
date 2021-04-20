from app.models import *
from tests.base_test import BaseTestCase


def new_user(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456'):
    return User.create(name=name, email=email, username=username, password=password)


def new_book(name="Sự Im Lặng Của Bầy Cừu", content=None, description="Bìa mềm", image="assets/img/book_img/img6.jpg",
             price=115000, quantity=50):
    return Book.create(name=name, quantity=quantity, description=description, image=image, price=price)


class ModelTests(BaseTestCase):
    def test_new_user(self):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, authenticated, and role fields are defined correctly
        """
        user = new_user()

        self.assertTrue(isinstance(user, User))
        self.assertTrue(user in db.session)
        self.assertTrue(user.password != '123456')
        self.assertTrue(user.user_role == UserRole.USER)
        self.assertTrue(user.__repr__() == '<User: admin123>')
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_anonymous)

    def test_setting_password(self):
        """
        GIVEN an existing User
        WHEN the password for the user is set
        THEN check the password is stored correctly and not as plaintext
        """
        user = new_user()

        user.set_password('1234567')
        self.assertTrue(user.password != '1234567')
        self.assertTrue(user.is_correct_password('1234567'))
        self.assertFalse(user.is_correct_password('123456'))
        self.assertFalse(user.is_correct_password('324832643'))

    def test_user_id(self):
        """
        GIVEN an existing User
        WHEN the ID of the user is defined to a value
        THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
        """
        user = new_user()
        user.id = 10
        self.assertTrue(isinstance(user.get_id(), str))
        self.assertFalse(isinstance(user.get_id(), int))
        self.assertTrue(user.get_id() == '10')

    def test_add_book(self):
        book = new_book()
        self.assertTrue(isinstance(book, Book))

    # def test_add_book_invalid(self):
    #     new_book()
    #     book = new_book(quantity=45)
    #
    #     self.assertTrue(book.quantity == 95)

    def test_new_category(self):
        category = Category.create(name="Tiểu thuyết")

        self.assertTrue(isinstance(category, Category))
        self.assertTrue(category in db.session)

    def test_new_author(self):
        author = Author.create(name="Tiểu thuyết")

        self.assertTrue(isinstance(author, Author))
        self.assertTrue(author in db.session)
