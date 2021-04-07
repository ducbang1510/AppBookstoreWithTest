from app import db, create_app, bcrypt
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Date, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from enum import Enum as UserEnum
import hashlib


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


#User_DataTable
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    joined_date = Column(Date, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __init__(self, name, email, username, plaintext_password, avatar=None, active='True', user_role=UserRole.USER):
        self.name = name
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')
        self.active = active
        self.user_role = user_role

    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

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


# if __name__ == '__main__':
#     db.create_all(app=create_app('app.cfg'))