from flask import url_for, render_template
from tests.base_test import BaseTestCase, create_data
from app import get_data
from app.models import *


class GetDataTests(BaseTestCase):
    def test_search_with_keyword(self):
        create_data()
        kw = "Án Mạng"
        results = get_data.filter_book(kw=kw)

        for r in results:
            self.assertTrue(kw.lower() in r.name.lower())

        self.assertTrue(len(results) == 2)

    def test_search_with_unknown_kw(self):
        create_data()
        kw = "kjdasbngjdzbnsjg"
        results = get_data.filter_book(kw=kw)

        for r in results:
            self.assertFalse(kw.lower() in r.name.lower())

        self.assertTrue(len(results) == 0)

    def test_search_with_price(self):
        create_data()
        results = get_data.filter_book(min_price=20000, max_price=100000)
        for r in results:
            self.assertTrue(r.name == 'Naruto Tập 43')

        self.assertTrue(len(results) == 1)

    def test_search_with_wrong_price(self):
        create_data()
        results = get_data.filter_book(min_price=100000, max_price=20000)

        self.assertTrue(len(results) == 0)

    def test_get_book_with_details(self):
        create_data()
        results = get_data.get_book_with_details()

        self.assertTrue(results[0].author == 'Masashi Kishimoto')
        self.assertTrue(results[1].author == 'Higashino Keigo')
        self.assertTrue(results[2].author == 'Agatha Christie')

        self.assertTrue(results[0].cate == 'Manga - Comic')
        self.assertTrue(results[1].cate == 'Truyện trinh thám')
        self.assertTrue(results[2].cate == 'Truyện trinh thám')

        self.assertTrue(len(results) == 3)

    def test_get_author_of_book_with_validID(self):
        create_data()
        results = get_data.get_author_of_book(book_id=1)

        for r in results:
            self.assertTrue(r.name == "Masashi Kishimoto")

        self.assertTrue(len(results) == 1)

    def test_get_author_of_book_with_unknownID(self):
        create_data()
        results = get_data.get_author_of_book(book_id=7)

        self.assertTrue(len(results) == 0)

    # Test get_author
    def test_get_authors(self):
        create_data()
        results = get_data.get_authors()

        self.assertTrue(len(results) == 3)

    # Test get_book_by_id
    def test_get_book_by_id(self):
        create_data()
        result = get_data.get_book_by_id(book_id=2)

        self.assertTrue(result.name == 'Án Mạng Mười Một Chữ')

    def test_get_book_by_invalid_id(self):
        create_data()
        result = get_data.get_book_by_id(book_id=5)

        self.assertTrue(result is None)

    # Test get_customer
    def test_get_customer_with_valid_info(self):
        create_data()
        c = Customer(name='Tran Van A', address='371 Nguyen Kiem', phone='0457492147', email='hrhsrhrs@gmail.com')
        result = get_data.get_customer(c)

        self.assertFalse(result is None)
        self.assertTrue(result.name == 'Tran Van A')
        self.assertTrue(result.address == '371 Nguyen Kiem')
        self.assertTrue(result.phone == '0457492147')
        self.assertTrue(result.email == 'hrhsrhrs@gmail.com')

    def test_get_customer_with_invalid_info(self):
        create_data()
        c = Customer(name='Nguyen Van A', address='371 Nguyen Kiem', phone='0457492147', email='hrhsrhrs@gmail.com')
        result = get_data.get_customer(c)

        self.assertTrue(result is None)

    # Test get_data_report
    def test_get_data_report(self):
        create_data()
        r = get_data.get_data_report()

        self.assertTrue(len(r) == 2)
        self.assertTrue(r[0].book_name == 'Naruto Tập 43')
        self.assertTrue(r[0].quantity == 50)
        self.assertTrue(r[0].report_date == datetime.now().date())

        self.assertTrue(r[1].book_name == 'Án Mạng Mười Một Chữ')
        self.assertTrue(r[1].quantity == 310)
        self.assertTrue(r[1].report_date == datetime.now().date())

    # Test check_book_is_exists
    def test_check_book_is_exists_with_valid_name(self):
        create_data()
        r = get_data.check_book_is_exists('Naruto Tập 43')

        self.assertTrue(r)

    def test_check_book_is_exists_with_invalid_name(self):
        create_data()
        r = get_data.check_book_is_exists('Ở một góc nhân gian')

        self.assertFalse(r)

    # Test check_book_quantity
    def test_check_book_quantity_with_quantity_less_than_300(self):
        create_data()
        r = get_data.check_book_quantity('Naruto Tập 43')

        self.assertTrue(r)

    def test_check_book_quantity_with_quantity_greater_than_300(self):
        create_data()
        r = get_data.check_book_quantity('Án Mạng Mười Một Chữ')

        self.assertFalse(r)

    # Test get_author_id
    def test_get_author_id_with_valid_name(self):
        create_data()
        r = get_data.get_author_id('Agatha Christie')

        self.assertTrue(r == 1)

    def test_get_author_id_with_invalid_name(self):
        create_data()
        r = get_data.get_author_id('kjbfdsbflsfgh')

        self.assertTrue(r is None)

    # Test get_category_id
    def test_get_category_id_with_valid_name(self):
        create_data()
        r = get_data.get_category_id('Manga - Comic')

        self.assertTrue(r == 1)

    def test_get_author_id_with_invalid_name(self):
        create_data()
        r = get_data.get_category_id('Tiểu thuyết')

        self.assertTrue(r is None)

    # Test get_book_id
    def test_get_book_id_with_valid_name(self):
        create_data()
        r = get_data.get_book_id('Án Mạng Trên Chuyến Tàu Tốc Hành Phương Đông')

        self.assertTrue(r == 3)

    def test_get_book_id_with_invalid_name(self):
        create_data()
        r = get_data.get_book_id('Naruto tap 1')

        self.assertTrue(r is None)

    # Test get_row_of_books_db
    def test_get_row_of_books_db(self):
        create_data()
        r = get_data.get_row_of_books_db()

        self.assertTrue(r == 3)
