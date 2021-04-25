from flask import Blueprint, render_template, redirect, url_for, flash, request, session, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from app import create_app, db, login_manager, models, get_data, utils
from app.models import *
from . import store_pages_blueprint

import os, os.path

from werkzeug.utils import secure_filename
from flask import send_from_directory


@store_pages_blueprint.route('/')
def index():
    categories = get_data.get_category()
    books = get_data.filter_book()
    booklm = get_data.filter_book(10)
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
    books = get_data.filter_book()
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
    books = get_data.filter_book()
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

    if len(books) == 0:
        flash('Không có kết quả nào về {}'.format(kw))

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


# Thêm sản phẩm vào giỏ hàng
@store_pages_blueprint.route('/api/cart', methods=['post'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    data = request.json
    book_id = str(data.get('id'))
    book_name = data.get('name')
    image = data.get('image')
    price = data.get('price')

    cart = session['cart']

    if book_id in cart:  # co san pham trong gio
        quan = cart[book_id]['quantity']
        cart[book_id]['quantity'] = int(quan) + 1
        subp = cart[book_id]['subTotal']
        cart[book_id]['subTotal'] = float(subp) + price
    else:  # chua co san pham trong gio
        cart[book_id] = {
            "id": book_id,
            "name": book_name,
            "image": image,
            "price": price,
            "quantity": 1,
            "subTotal": price
        }

    session['cart'] = cart

    total_quan, total_amount = utils.cart_stats(session['cart'])

    return jsonify({
        "message": "Thêm giỏ hàng thành công",
        'total_amount': total_amount,
        'total_quantity': total_quan
    })


# Bớt một sản phẩm khỏi giỏ hàng
@store_pages_blueprint.route('/api/remove-item-cart', methods=['post'])
def remove_from_cart():
    data = request.json
    book_id = str(data.get('id'))
    book_name = data.get('name')
    image = data.get('image')
    price = data.get('price')

    cart = session['cart']
    if book_id in cart:  # co san pham trong gio
        quan = cart[book_id]['quantity']
        cart[book_id]['quantity'] = int(quan) - 1
        subp = cart[book_id]['subTotal']
        cart[book_id]['subTotal'] = float(subp) - price
    else:  # chua co san pham trong gio
        cart[book_id] = {
            "id": book_id,
            "name": book_name,
            "image": image,
            "price": price,
            "quantity": 1,
            "subTotal": price
        }

    session['cart'] = cart

    total_quan, total_amount = utils.cart_stats(session['cart'])

    return jsonify({
        "message": "Cập nhật giỏ hàng thành công",
        'total_amount': total_amount,
        'total_quantity': total_quan
    })


# Xóa giỏ hàng
@store_pages_blueprint.route("/api/cart/<int:b_id>", methods=["delete"])
def delete_item(b_id):
    data = request.json
    book_id = str(data.get('id'))

    cart = session.get('cart')
    for idx, b in enumerate(cart.values()):
        if b['id'] == b_id:
            del cart[idx]
            break

    cart = session['cart']

    if book_id in cart:
        cart[book_id]['quantity'] = 0
        cart[book_id]['subTotal'] = 0

    session['cart'] = cart

    total_quan, total_amount = utils.cart_stats(session['cart'])
    return jsonify({
        "message": "Xoa thanh cong",
        "data": {"book_id": b_id},
        'total_amount': total_amount,
        'total_quantity': total_quan
    })


# Trang giỏ hàng
@store_pages_blueprint.route("/shop-cart")
def shop_cart():
    categories = get_data.get_category()

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }
    return render_template('store_pages/shop_cart.html', categories=categories, cart_info=cart_info)


# Trang thanh toán
@store_pages_blueprint.route("/checkout", methods=['get', 'post'])
def checkout():
    categories = get_data.get_category()

    if request.method == 'POST':

        if utils.add_invoice(session.get('cart')):
            del session['cart']

            return jsonify({"message": "Đặt hàng thành công"})

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/checkout.html', categories=categories, cart_info=cart_info)


# trung
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Nhập sách
@store_pages_blueprint.route('/admin/tempbookview', methods=['GET', 'POST'])
def create_book():
    # lấy dữ liệu từ form
    if request.method == "POST":
        name = request.form.get('name')
        content = request.form.get('content')
        description = request.form.get('description')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        category = request.form.get('category')
        author = request.form.get('author')
        image = request.form.get('image')

        print(author)
        print(category)

        # upload_and_save_picture_not_finish
        # file_path = os.getcwd() + r'\app\static\assets\img\book_img'
        # image = request.files['image']
        #
        # if image and allowed_file(image.filename):
        #     file_name = secure_filename(image.filename)
        #     image.save(os.path.join(file_path), file_name)

    # Kiểm tra điều kiện
    kq_check_exitst = get_data.check_book_is_exists(name)
    kq_check_quantity = get_data.check_book_quantity(name)
    kq_create = None
    kq_update = None
    kq = None

    if not kq_check_exitst:
        kq_create = get_data.create_book_with_quantity(name, content, description, image, price,
                                                       quantity, author, category)
    elif kq_check_quantity:
        kq_update = get_data.update_book_with_quantity(name, quantity)
    else:
        kq = False

    print(kq_create)
    print(kq_update)
    print(kq)

    return redirect('/admin/tempbookview')
