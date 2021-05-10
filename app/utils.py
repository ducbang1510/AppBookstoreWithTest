from app.models import *
from sqlalchemy import extract
from app import get_data


# Tính tổng giỏ hàng
def cart_stats(cart):
    if cart is None:
        return 0, 0

    books = cart.values()

    quantity = sum([b['quantity'] for b in books])
    total = sum([b['price'] * b['quantity'] for b in books])

    return quantity, total


# Lưu hóa đơn
def add_invoice(cart, customer_id, note=None):
    total = 0
    if cart:
        try:
            for b in list(cart.values()):
                total = total + float(b["subTotal"])

            invoice = Invoice(total=total, customer_id=customer_id, note=note)
            db.session.add(invoice)
            db.session.commit()

            for b in list(cart.values()):
                if b["quantity"] > 0:
                    detail = DetailInvoice(invoice_id=invoice.id,
                                           book_id=int(b["id"]),
                                           quantity=b["quantity"],
                                           price=float(b["price"]))

                    book = get_data.get_book_by_id(int(b["id"]))
                    book.set_quantity(int(b["quantity"]))

                    db.session.add(detail)

            db.session.commit()

            return True
        except:
            pass

    return False


def add_customer(customer):
    c = get_data.get_customer(customer)
    if c:
        return False
    else:
        db.session.add(customer)
        db.session.commit()

    return True


def report_revenue(month, year=None, day=None):
    tong = 0
    if day:
        invoices = Invoice.query.filter(extract('day', Invoice.date_of_invoice) == int(day),
                                        extract('month', Invoice.date_of_invoice) == int(month),
                                        extract('year', Invoice.date_of_invoice) == int(year)).all()
    else:
        invoices = Invoice.query.filter(extract('month', Invoice.date_of_invoice) == int(month),
                                        extract('year', Invoice.date_of_invoice) == int(year)).all()

    for i in invoices:
        tong = tong + i.total

    return tong


def create_book_with_quantity(name, content, description, image, price,
                              quantity, author, category):
    if quantity >= 50:
        book = Book(name=name, content=content, description=description, image=image,
                    price=price, quantity=quantity)

        category_id = get_data.get_category_id(category_name=category)
        author_id = get_data.get_author_id(author_name=author)

        try:
            db.session.add(book)
            db.session.commit()

            book_id = get_data.get_book_id(book_name=name)
            book_cate = BookCate(book_id=book_id, category_id=category_id)
            book_author = BookAuthor(book_id=book_id, author_id=author_id)
            book_image = Bookimage(image=image, book_id=book_id)

            db.session.add(book_cate)
            db.session.add(book_author)
            db.session.add(book_image)

            db.session.commit()
            return True

        except Exception as ex:
            print(ex)
            return False
    return False


def update_book_with_quantity(book_name, quantity):
    b = Book.query.filter(Book.name.contains(book_name)).first()
    if b.quantity <= 300 and quantity >= 50:
        b.quantity += int(quantity)
    else:
        pass

    try:
        db.session.add(b)
        db.session.commit()

        return True
    except Exception as ex:
        print(ex)
        return False