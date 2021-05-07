from app.models import *
from tests.base_test import BaseTestCase
from datetime import datetime


def new_user(name='Duc Bang', email='abc@gmail.com', username='admin123', password='123456'):
    return User.create(name=name, email=email, username=username, password=password)


def new_book(name="Sự Im Lặng Của Bầy Cừu", content=None, description="Bìa mềm", image="assets/img/book_img/img6.jpg",
             price=115000, quantity=50):
    return Book.create(name=name, quantity=quantity, description=description, image=image, price=price)


class ModelTests(BaseTestCase):
    # TEST User
    def test_new_user(self):
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
        user = new_user()

        user.set_password('1234567')
        self.assertTrue(user.password != '1234567')
        self.assertTrue(user.is_correct_password('1234567'))
        self.assertFalse(user.is_correct_password('123456'))
        self.assertFalse(user.is_correct_password('324832643'))

    def test_user_id(self):
        user = new_user()
        user.id = 10
        self.assertTrue(isinstance(user.get_id(), str))
        self.assertFalse(isinstance(user.get_id(), int))
        self.assertTrue(user.get_id() == '10')

    # TEST Customer
    def test_customer(self):
        c = Customer.create(name='Tran Van A', address='371 Nguyen Kiem', phone='0457492147',
                            email='hrhsrhrs@gmail.com')

        self.assertTrue(c in db.session)
        self.assertTrue(c.__repr__() == '<Name: Tran Van A>')

    # TEST Book
    def test_add_book(self):
        book = new_book()
        self.assertTrue(isinstance(book, Book))

    def test_set_quantity_after_sell(self):
        book = new_book()
        book.set_quantity(10)

        self.assertTrue(book.quantity == 40)

    # TEST Category
    def test_category(self):
        category = Category.create(name="Tiểu thuyết")

        self.assertTrue(isinstance(category, Category))
        self.assertTrue(category in db.session)

    # TEST Author
    def test_author(self):
        author = Author.create(name="Tiểu thuyết")

        self.assertTrue(isinstance(author, Author))
        self.assertTrue(author in db.session)

    # TEST Invoice
    def test_invoice(self):
        Customer.create(name='Tran Van A', address='371 Nguyen Kiem', phone='0457492147', email='hrhsrhrs@gmail.com')
        invoice = Invoice(total=154000, customer_id=1)
        db.session.add(invoice)
        db.session.commit()

        self.assertTrue(invoice in db.session)

    # TEST Detail_Invoice
    def test_detail_invoice(self):
        Customer.create(name='Tran Van A', address='371 Nguyen Kiem', phone='0457492147',
                        email='hrhsrhrs@gmail.com')
        new_book()
        invoice = Invoice(total=154000, customer_id=1)
        db.session.add(invoice)
        db.session.commit()

        detail_invoice = DetailInvoice(book_id=1, invoice_id=1, quantity=2)
        db.session.add(detail_invoice)
        db.session.commit()

        self.assertTrue(detail_invoice in db.session)

    # TEST Inventory
    def test_inventory(self):
        ivt = InventoryReport()
        db.session.add(ivt)
        db.session.commit()

        self.assertTrue(ivt in db.session)
        self.assertTrue(ivt.report_date == datetime.now().date())

    # TEST Detail_Inventory
    def test_detail_inventory(self):
        new_book()
        ivt = InventoryReport()
        db.session.add(ivt)
        db.session.commit()

        divt = DetailInventoryReport(report_id=1, book_id=1, quantity=50)
        db.session.add(divt)
        db.session.commit()

        self.assertTrue(divt in db.session)
