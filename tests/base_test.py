from flask import session
from flask_testing import TestCase
from app import create_app, db
from app.models import *
from datetime import datetime


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
    Book.create(name='Naruto Tập 43', quantity=50, description="Bìa mềm", image="assets/img/book_img/img12.jpg",
                price=22000)
    Book.create(name='Án Mạng Mười Một Chữ', quantity=310, description="Bìa mềm",
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

    User.create(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456', user_role=UserRole.ADMIN)
    User.create(name='Tran Bang', email='abdc@gmail.com', username='admin456', password='654321')

    Customer.create(name='Tran Van A', address='371 Nguyen Kiem', phone='0457492147', email='hrhsrhrs@gmail.com')
    Customer.create(name='Phan Van Trung', address='432 Nguyen Van Cong', phone='0123456789', email='trung123@gmail.com')

    i1 = Invoice(total=154000, customer_id=1)
    i2 = Invoice(total=440000, customer_id=1)
    db.session.add(i1)
    db.session.add(i2)
    db.session.commit()

    di1 = DetailInvoice(invoice_id=1, book_id=1, quantity=2, price=44000)
    di2 = DetailInvoice(invoice_id=1, book_id=2, quantity=1, price=110000)
    di3 = DetailInvoice(invoice_id=2, book_id=3, quantity=4, price=440000)
    db.session.add(di1)
    db.session.add(di2)
    db.session.add(di3)
    db.session.commit()

    ivt = InventoryReport()
    db.session.add(ivt)
    db.session.commit()

    divt = DetailInventoryReport(report_id=1, book_id=1, quantity=50)
    db.session.add(divt)
    db.session.commit()


# init cart for testing
def init_cart():
    session['cart'] = {}
    cart = session['cart']
    cart[1] = {
        "id": 1,
        "name": 'Naruto Tập 43',
        "price": 22000,
        "quantity": 3,
        "subTotal": 22000 * 3
    }
    cart[2] = {
        "id": 2,
        "name": 'Án Mạng Mười Một Chữ',
        "price": 110000,
        "quantity": 1,
        "subTotal": 110000
    }
    session['cart'] = cart
    return session['cart']