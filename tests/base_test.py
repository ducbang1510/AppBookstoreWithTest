from flask_testing import TestCase
from app import create_app, db
from app.models import *


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app('test_app.cfg')
        app.app_context().push()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


# init_data for testing
def create_data():
    Book.create(name='Naruto Tập 43', quantity=0, description="Bìa mềm", image="assets/img/book_img/img12.jpg",
                price=22000)
    Book.create(name='Án Mạng Mười Một Chữ', quantity=0, description="Bìa mềm",
                image="assets/img/book_img/img8.jpg",
                price=110000)
    Book.create(name='Án Mạng Trên Chuyến Tàu Tốc Hành Phương Đông', quantity=0, description="Bìa mềm",
                image="assets/img/book_img/img2.jpg",
                price=110000)

    Category.create(name='Manga - Comic')
    Category.create(name='Truyện trinh thám')
    Category.create(name='Sách tham khảo')

    Author.create(name="Agatha Christie", image='assets/img/140x140/img7.jpg')
    Author.create(name="Higashino Keigo", image='assets/img/140x140/img2.jpg')
    Author.create(name="Masashi Kishimoto", image='assets/img/140x140/img4.jpg')

    BookCate.create(category_id=1, book_id=1)
    BookCate.create(category_id=2, book_id=2)
    BookCate.create(category_id=2, book_id=3)

    BookAuthor.create(book_id=1, author_id=3)
    BookAuthor.create(book_id=2, author_id=2)
    BookAuthor.create(book_id=3, author_id=1)

    User.create(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456')
    User.create(name='Tran Bang', email='abdc@gmail.com', username='admin456', password='654321')
