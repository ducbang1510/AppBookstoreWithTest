from flask import Blueprint, render_template, redirect, url_for, flash, request, session, jsonify
from flask_login import login_user, current_user, login_required, logout_user
from flask_admin import BaseView
from app import create_app, db, login_manager, models, get_data, utils, admin, admin_view
from app.models import *
from . import store_pages_blueprint
from .forms import CustomerForm
from app.users.forms import LoginForm, RegisterForm


@store_pages_blueprint.route('/', methods=['GET', 'POST'])
def index():
    categories = get_data.get_category()
    books = get_data.filter_book()
    booklm = get_data.filter_book(10)
    book_list = get_data.get_book_with_details()
    authors = get_data.get_authors(8)
    form = LoginForm()
    form1 = RegisterForm()

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
                           cart_info=cart_info,
                           form1=form1, form=form)


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
    form = LoginForm()
    form1 = RegisterForm()
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/book_detail.html',
                           book=book,
                           books=books,
                           book_list=book_list,
                           categories=categories,
                           authors=authors, images=images, cart_info=cart_info,
                           form=form, form1=form1)


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
    form = LoginForm()
    form1 = RegisterForm()
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/shop_list.html', book_pagi=book_pagi, book_list=book_list, books=books,
                           categories=categories,
                           author_list=author_list,
                           cart_info=cart_info,
                           page_num=page_num,
                           all_pages=all_pages,
                           form1=form1, form=form)


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
    form = LoginForm()
    form1 = RegisterForm()

    if len(books) == 0:
        if kw:
            flash('Không có kết quả nào về {}'.format(kw))
        else:
            flash('Không có kết quả nào')

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
                           cart_info=cart_info,
                           form=form, form1=form1)


# Trang giỏ hàng
@store_pages_blueprint.route("/shop-cart")
def shop_cart():
    categories = get_data.get_category()
    form = LoginForm()
    form1 = RegisterForm()

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }
    return render_template('store_pages/shop_cart.html', categories=categories, cart_info=cart_info
                           , form=form, form1=form1)


# Trang thanh toán
@store_pages_blueprint.route("/checkout", methods=['get', 'post'])
def checkout():
    categories = get_data.get_category()

    form = LoginForm()
    form1 = RegisterForm()
    form2 = CustomerForm()
    cart = session.get('cart')

    if request.method == 'POST':
        if cart:
            if current_user.is_authenticated and current_user.user_role == UserRole.USER:
                new_customer = Customer(name=current_user.name,
                                        address=form2.address.data,
                                        phone=form2.phone.data,
                                        email=current_user.email)
            elif form2.email.data:
                new_customer = Customer(name=form2.first_name.data + ' ' + form2.last_name.data,
                                        address=form2.address.data,
                                        phone=form2.phone.data,
                                        email=form2.email.data)
            else:
                flash('Hãy sử dụng tài khoản khách hàng để thanh toán')
                return redirect(url_for('store_pages.checkout'))

            if utils.add_customer(new_customer):
                c = Customer.query.filter_by(id=new_customer.id).first()
            else:
                c = get_data.get_customer(new_customer)

            if utils.add_invoice(session.get('cart'), c.id, form2.order_comments.data):
                del session['cart']

                flash("Đặt hàng thành công")
                return redirect(url_for('store_pages.index'))
        else:
            flash("Không có sản phẩm nào trong giỏ")
            return redirect(url_for('store_pages.checkout'))

    quan, price = utils.cart_stats(session.get('cart'))
    cart_info = {
        'total_quantity': quan,
        'total_amount': price
    }

    return render_template('store_pages/checkout.html', categories=categories, cart_info=cart_info,
                           form=form, form1=form1, form2=form2)


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


# Bớt sản phẩm khỏi giỏ hàng
@store_pages_blueprint.route('/api/remove-item-cart', methods=['post'])
def remove_from_cart():
    data = request.json
    book_id = str(data.get('id'))
    price = data.get('price')

    cart = session['cart']
    if book_id in cart:  # co san pham trong gio
        quan = cart[book_id]['quantity']
        cart[book_id]['quantity'] = int(quan) - 1
        subp = cart[book_id]['subTotal']
        cart[book_id]['subTotal'] = float(subp) - price

    session['cart'] = cart

    total_quan, total_amount = utils.cart_stats(session['cart'])

    return jsonify({
        "message": "Cập nhật giỏ hàng thành công",
        'total_amount': total_amount,
        'total_quantity': total_quan
    })


@store_pages_blueprint.route('/api/add_remove_cart', methods=['post'])
def add_or_remove_items_from_cart():
    if 'cart' not in session:
        session['cart'] = {}

    data = request.json
    book_id = str(data.get('id'))
    book_name = data.get('name')
    image = data.get('image')
    price = data.get('price')
    quantity = data.get('quantity')

    cart = session['cart']

    if book_id in cart:  # co san pham trong gio
        cart[book_id]['quantity'] = int(quantity)
        cart[book_id]['subTotal'] = int(quantity) * price
    else:  # chua co san pham trong gio
        cart[book_id] = {
            "id": book_id,
            "name": book_name,
            "image": image,
            "price": price,
            "quantity": int(quantity),
            "subTotal": price
        }

    session['cart'] = cart

    total_quan, total_amount = utils.cart_stats(session['cart'])

    return jsonify({
        'message': "Cập nhật giỏ hàng thành công",
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
        "message": "Xóa thành công",
        "data": {"book_id": b_id},
        'total_amount': total_amount,
        'total_quantity': total_quan
    })


class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = admin


@store_pages_blueprint.route('/report', methods=['POST', 'GET'])
def report():
    data = []
    reports = get_data.get_data_report()
    if current_user.is_authenticated and current_user.user_role == UserRole.ADMIN:
        if request.method == 'POST':
            year = request.form.get("year")
            for i in range(1, 13):
                data.append(utils.report_revenue(i, year=year))
            m = int(max(data))
            a = list(str(m))
            for i in range(0, len(a)):
                if i == 0:
                    a[i] = str(int(a[i]) + 1)
                else:
                    a[i] = '0'
            c = int(''.join(a))
            return MyView().render('admin/thongke.html', data=data, c=c, reports=reports, year=year)

        return MyView().render('admin/thongke.html', data=data, c=0, reports=reports)
    else:
        flash('Hãy đăng nhập với tài khoản quyền admin')
        return redirect('/admin')


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
        kq_create = utils.create_book_with_quantity(name, content, description, image, price,
                                                       quantity, author, category)
    elif kq_check_quantity:
        kq_update = utils.update_book_with_quantity(name, quantity)
    else:
        kq = False

    print(kq_create)
    print(kq_update)
    print(kq)

    return redirect('/admin/tempbookview')