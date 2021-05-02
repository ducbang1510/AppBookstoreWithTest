from app import db
from app.models import *


def get_category():
    return Category.query.all()


def get_authors(lm=None):
    authors = Author.query
    if lm:
        authors = authors.limit(lm)
    return authors.all()


def get_author_of_book(book_id):
    authors = Author.query.join(BookAuthor, Author.id == BookAuthor.author_id) \
        .filter(BookAuthor.book_id == book_id)
    return authors.all()


def get_book_by_id(book_id):
    return Book.query.get(book_id)


def get_image(cat, book_id=None):
    image = Bookimage.query.filter(Bookimage.image.contains(cat))
    if book_id:
        image = Bookimage.query.join(Book, Book.id == Bookimage.book_id) \
            .filter(Bookimage.image.contains(cat), Bookimage.book_id == book_id)
    return image.all()


def get_book_with_details():
    books = db.session.query(Book.id, Book.name, Book.description, Book.image, Book.price, Book.quantity,
                             Author.name.label('author'),
                             Category.name.label('cate')) \
        .join(BookAuthor, BookAuthor.book_id == Book.id) \
        .join(Author, Author.id == BookAuthor.author_id) \
        .join(BookCate, BookCate.book_id == Book.id) \
        .join(Category, Category.id == BookCate.category_id)

    return books.all()


def filter_book(cate_id=None, author_id=None, min_price=None, max_price=None, kw=None, lm=None):
    books = Book.query

    if kw:
        books = books.filter(Book.name.contains(kw))

    if cate_id:
        books = books.join(BookCate, Book.id == BookCate.book_id)\
            .filter(BookCate.category_id == cate_id)

    if author_id:
        books = books.join(BookAuthor, Book.id == BookAuthor.book_id)\
            .filter(BookAuthor.author_id == author_id)

    if min_price and max_price:
        books = books.filter(Book.price.__gt__(min_price), Book.price.__lt__(max_price))

    if lm:
        books = books.limit(lm)

    return books.all()


def get_customer(customer):
    c = Customer.query.filter_by(name=customer.name,
                                 address=customer.address,
                                 phone=customer.phone,
                                 email=customer.email).first()

    return c


def get_data_report():
    data = db.session.query(Book.name.label('book_name'),
                            Book.price.label('price'),
                            DetailInventoryReport.quantity.label('quantity'),
                            InventoryReport.report_date.label('report_date')) \
                .join(Book, Book.id == DetailInventoryReport.book_id) \
                .join(InventoryReport, DetailInventoryReport.report_id == InventoryReport.id)
    return data.all()


# check a book is exists in database?
def check_book_is_exists(book_name=None):
    name_book_db = ''
    if book_name is not None:
        books = Book.query.filter(Book.name.contains(book_name)).first()
        if books is not None:
            name_book_db = books.name

    if book_name == name_book_db:
        return True
    else:
        return False


# check quantity
def check_book_quantity(book_name=None):
    quantity_db = None
    if book_name is not None:
        books = Book.query.filter(Book.name.contains(book_name)).first()
        if books is not None:
            quantity_db = books.quantity

    if quantity_db is not None:
        if quantity_db < 300:
            return True
    else:
        return False


def get_author_id(author_name):
    author = Author.query.filter(Author.name.contains(author_name)).first()

    return author.id


def get_category_id(category_name):
    category = Category.query.filter(Category.name.contains(category_name)).first()

    return category.id


def get_book_id(book_name):
    book = Book.query.filter(Book.name.contains(book_name)).first()

    return book.id


def get_row_of_books_db():
    row = Book.query.count()
    return row
