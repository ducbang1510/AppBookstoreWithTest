from flask import session
from tests.base_test import BaseTestCase, init_cart, create_data
from app import utils, get_data
from app.models import *


class UtilsTest(BaseTestCase):
    # Test cart_stats
    def test_cart_stats(self):
        total_quan, total_amount = utils.cart_stats(init_cart())

        self.assertTrue(total_quan == 4)
        self.assertTrue(total_amount == 176000)

    # Test add_invoice
    def test_add_invoice(self):
        create_data()
        kt = utils.add_invoice(init_cart(), 1)

        self.assertTrue(kt)

    def test_add_invoice_with_unknown_CustomerID(self):
        create_data()
        kt = utils.add_invoice(init_cart(), 3)

        self.assertFalse(kt)

    # Test add_customer
    def test_add_customer(self):
        create_data()
        new_customer = Customer(name='Tran Van C',
                                address='37 Quang Trung',
                                phone='0838855548',
                                email='fashrs@gmail.com')
        kt = utils.add_customer(new_customer)

        self.assertTrue(kt)
        self.assertTrue(new_customer in db.session)

    def test_add_duplicate_customer(self):
        create_data()
        new_customer = Customer(name='Tran Van A',
                                address='371 Nguyen Kiem',
                                phone='0457492147',
                                email='hrhsrhrs@gmail.com')
        kt = utils.add_customer(new_customer)

        self.assertFalse(kt)
        self.assertFalse(new_customer in db.session)

    # Test report
    def test_report_revenue_with_valid_date(self):
        create_data()
        total = utils.report_revenue(5, 2021)

        self.assertTrue(total == 594000)

    def test_report_revenue_with_invalid_date(self):
        create_data()
        total = utils.report_revenue(1, 2022)

        self.assertTrue(total == 0)

    # Test create_book_with_quantity
    def test_create_book_with_quantity(self):
        create_data()
        row_before = get_data.get_row_of_books_db()

        utils.create_book_with_quantity(name='Naruto Tập 1', content='nội dung', description='mô tả', image=''
                                        , price=50000, quantity=50, author='Masashi Kishimoto',
                                        category='Manga - Comic')

        row_after = get_data.get_row_of_books_db()

        self.assertTrue(row_after > row_before)

    # Test update_book_with_quantity
    def test_update_book_with_valid_quantity(self):
        create_data()
        utils.update_book_with_quantity(book_name='Naruto Tập 43', quantity=50)

        book = get_data.get_book_by_id(1)
        self.assertTrue(book.quantity == 100)

    def test_update_book_with_invalid_quantity(self):
        create_data()
        utils.update_book_with_quantity(book_name='Án Mạng Mười Một Chữ', quantity=50)

        book = get_data.get_book_by_id(2)
        self.assertTrue(book.quantity == 310)
        self.assertFalse(book.quantity == 360)