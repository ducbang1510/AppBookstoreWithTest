from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, login_required, logout_user
from app import create_app, db, login_manager, models, get_data, utils
from app.models import *
from . import store_pages_blueprint


@store_pages_blueprint.route('/')
def index():
    categories = get_data.get_category()
    books = get_data.get_books()
    booklm = get_data.get_books(10)
    book_list = get_data.get_book_with_details()
    authors = get_data.get_authors(8)

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }
    return render_template('store_pages/index.html',
                           categories=categories,
                           books=books,
                           booklm=booklm,
                           book_list=book_list,
                           authors=authors,
                           cart_info=cart_info)


# Thông tin sách
@store_pages_blueprint.route("/shop-list/book-detail/<int:book_id>")
def book_detail(book_id):
    categories = get_data.get_category()
    book = get_data.get_book_by_id(book_id)
    books = get_data.get_books()
    book_list = get_data.get_book_with_details()
    authors = get_data.get_author_of_book(book_id)
    images = get_data.get_image('300x452', book_id=book_id)
    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/book_detail.html',
                           book=book,
                           books=books,
                           book_list=book_list,
                           categories=categories,
                           authors=authors, images=images, cart_info=cart_info)


# Tất cả sản phẩm
@store_pages_blueprint.route("/shop-list/<int:page_num>")
def shop_list(page_num):
    categories = get_data.get_category()
    author_list = get_data.get_authors()
    books = get_data.get_books()
    book_list = get_data.get_book_with_details()
    book_pagi = Book.query.paginate(per_page=12, page=page_num, error_out=True)
    all_pages = book_pagi.iter_pages()
    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/shop_list.html', book_pagi=book_pagi, book_list=book_list, books=books,
                           categories=categories,
                           author_list=author_list,
                           cart_info=cart_info,
                           page_num=page_num,
                           all_pages=all_pages)


# Lọc theo thể loại và tác giả
@store_pages_blueprint.route("/shop-list")
def shop_filter():
    categories = get_data.get_category()
    author_list = get_data.get_authors()
    book_list = get_data.get_book_with_details()

    kw = request.args.get("kw")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    cate_id = request.args.get("category_id")
    author_id = request.args.get("author_id")
    books = get_data.filter_book(cate_id=cate_id, author_id=author_id, min_price=min_price, max_price=max_price, kw=kw)

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/shop_list.html', books=books, book_list=book_list, kw=kw,
                           min_price=min_price,
                           cate_id=cate_id,
                           author_id=author_id,
                           categories=categories,
                           author_list=author_list,
                           cart_info=cart_info)