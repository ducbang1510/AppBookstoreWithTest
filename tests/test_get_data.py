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
# Test get_book_by_id
# Test get_image
# Test get_customer
# Test get_data_report
