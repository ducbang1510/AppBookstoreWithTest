from app.get_data import get_book_id
from app.models import *

from tests.base_test import BaseTestCase


def create_book_with_quantity(name=None, content=None, description=None, image=None, price=None,
                              quantity=None, author=None, category=None):
    book = Book(name=name, content=content, description=description, image=image,
                price=price, quantity=quantity)

    # category_id = get_category_id(category_name=category)
    # author_id = get_author_id(author_name=author)

    category_id = 1
    author_id = 1

    try:
        db.session.add(book)
        db.session.commit()

        book_id = get_book_id(book_name=name)
        book_cate = BookCate(book_id=book_id, category_id=category_id)
        book_author = BookAuthor(book_id=book_id, author_id=author_id)

        db.session.add(book_cate)
        db.session.add(book_author)

        db.session.commit()
        return True

    except Exception as ex:
        print(ex)
        return False


def get_row_of_books_db():
    books = Book.query

    row = books.count()
    return row


class TestCreateBook(BaseTestCase):
    def test_create_book(self):
        Author.create(name="Higashino Keigo")
        Category.create(name='Truyện trinh thám')

        row_before = get_row_of_books_db()

        create_book_with_quantity(name='Naruto Tập 1', content='nội dung', description='mô tả', image=''
                                  , price=50000, quantity=50, author='Thomas Harris', category='Tiểu thuyết')

        row_after = get_row_of_books_db()

        self.assertTrue(row_after > row_before)
