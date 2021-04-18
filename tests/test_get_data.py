from flask import url_for, render_template
from tests.base_test import BaseTestCase
from app import get_data
from app.models import *


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

    Author.create(name="Agatha Christie")
    Author.create(name="Higashino Keigo")
    Author.create(name="Masashi Kishimoto")

    BookCate.create(category_id=1, book_id=1)
    BookCate.create(category_id=2, book_id=2)
    BookCate.create(category_id=2, book_id=3)

    BookAuthor.create(book_id=1, author_id=3)
    BookAuthor.create(book_id=2, author_id=2)
    BookAuthor.create(book_id=3, author_id=1)


class GetDataTests(BaseTestCase):
    def test_search_with_keyword(self):
        kw = "Án Mạng"
        results = get_data.filter_book(kw=kw)

        for r in results:
            assert kw.lower() in r.name.lower()

        assert len(results) == 2

    def test_search_with_unknown_kw(self):
        kw = "kjdasbngjdzbnsjg"
        results = get_data.filter_book(kw=kw)

        for r in results:
            assert kw.lower() not in r.name.lower()

        assert len(results) == 0

    def test_get_book_with_details(self):
        results = get_data.get_book_with_details()

        assert results[0].author == 'Masashi Kishimoto'
        assert results[1].author == 'Higashino Keigo'
        assert results[2].author == 'Agatha Christie'

        assert results[0].cate == 'Manga - Comic'
        assert results[1].cate == 'Truyện trinh thám'
        assert results[2].cate == 'Truyện trinh thám'

        assert len(results) == 3