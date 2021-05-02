from app import db, create_app, bcrypt
from app.mixins import CRUDMixin
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Date, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from enum import Enum as UserEnum


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


# User_DataTable
class User(db.Model, CRUDMixin, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(Date, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __init__(self, name, email, username, password, active=True, user_role=UserRole.USER):
        self.name = name
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.active = active
        self.user_role = user_role

    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    def set_password(self, plaintext_password):
        self.password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def __repr__(self):
        return f'<User: {self.username}>'

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)


# Bảng khách hàng
class Customer(db.Model, CRUDMixin):
    __tablename__ = 'customer'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(50), nullable=False)

    # invoices = relationship('Invoice', backref='customer', lazy=True)

    def __init__(self, name, address=None, phone=None, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f'<User: {self.name}>'


# Bảng sách
class Book(db.Model, CRUDMixin):
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    content = Column(LONGTEXT, nullable=True)
    description = Column(String(255))
    image = Column(String(255))
    price = Column(Float, default=0)
    quantity = Column(Integer, nullable=False, default=50)
    categories = relationship('Category', secondary='book_cate', lazy='subquery', backref=backref('books', lazy=True))
    authors = relationship('Author', secondary='book_author', lazy='subquery', backref=backref('books', lazy=True))

    # images = relationship('Bookimage', backref=backref('books', lazy=True))

    def __init__(self, name, quantity, content=None, description=None, image=None, price=None):
        self.name = name
        self.content = content
        self.description = description
        self.image = image
        self.price = price
        self.quantity = quantity

    def set_quantity(self, sell_quantity):
        self.quantity = self.quantity - sell_quantity

    def __str__(self):
        return "Tên sách: %s, số lượng: %s" % (str(self.name), str(self.quantity))


class Bookimage(db.Model):
    __tablename__ = 'book_image'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String(255), nullable=False)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=False)


# Bảng thể loại
class Category(db.Model, CRUDMixin):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Bảng sách-thể loại
class BookCate(db.Model, CRUDMixin):
    __tablename__ = 'book_cate'
    __table_args__ = {'extend_existing': True}

    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)

    def __init__(self, book_id, category_id):
        self.book_id = book_id
        self.category_id = category_id


# Bảng tác giả
class Author(db.Model, CRUDMixin):
    __tablename__ = 'author'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(255))

    def __init__(self, name, image=None):
        self.name = name
        self.image = image

    def __str__(self):
        return self.name


# Bảng sách-tác giả
class BookAuthor(db.Model, CRUDMixin):
    __tablename__ = 'book_author'
    __table_args__ = {'extend_existing': True}

    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)


# Bảng hóa đơn
class Invoice(db.Model, CRUDMixin):
    __tablename__ = 'invoice'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_of_invoice = Column(Date, default=datetime.now())
    total = Column(Float, default=0)
    note = Column(LONGTEXT, nullable=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    def __str__(self):
        return "Mã háo dơn %s, ngày tạo %s" % (str(self.id), str(self.date_of_invoice))


# Bảng chi tiết hóa đơn
class DetailInvoice(db.Model):
    __tablename__ = 'detail_invoice'
    __table_args__ = {'extend_existing': True}

    invoice_id = Column(Integer, ForeignKey('invoice.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)

    books = relationship('Book', backref=backref('detail_invoice', lazy=True))
    invoices = relationship('Invoice', backref=backref('detail_invoice', lazy=True))

    def __str__(self):
        return "%s x %s" % (str(self.books), str(self.quantity))


# Bảng báo cáo tồn
class InventoryReport(db.Model):
    __tablename__ = 'inventory_report'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(Date, default=datetime.now())

    # detail_inventory_reports = relationship('DetailInventoryReport', backref=backref('inventory_report', lazy=True))

    def __str__(self):
        return "Mã báo cáo tồn kho %s, ngày tạo %s" % (str(self.id), str(self.report_date))


# Bảng chi tiết báo cáo tồn
class DetailInventoryReport(db.Model):
    __tablename__ = 'detail_inventory_report'
    __table_args__ = {'extend_existing': True}

    report_id = Column(Integer, ForeignKey('inventory_report.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    quantity = Column(Integer, default=0)
    books = relationship('Book', backref=backref('detail_inventory_report', lazy=True))
    inventory_reports = relationship('InventoryReport', backref=backref('detail_inventory_report', lazy=True))
