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

            invoice = Invoice(customer_id=customer_id, total=total, note=note)
            db.session.add(invoice)
            db.session.commit()
            # else:
            #     invoice = Invoice(customer_id=1, total=total, paid=total)

            for b in list(cart.values()):
                if b["quantity"] > 0:
                    detail = DetailInvoice(invoice_id=invoice.id,
                                           book_id=int(b["id"]),
                                           quantity=b["quantity"],
                                           price=float(b["price"]))
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


def report_revenue(month, year=None):
    tong = 0
    if year:
        invoices = Invoice.query.filter(extract('month', Invoice.date_of_invoice) == int(month),
                                        extract('year', Invoice.date_of_invoice) == int(year)).all()
    else:
        invoices = Invoice.query.filter(extract('month', Invoice.date_of_invoice) == int(month)).all()

    for i in invoices:
        tong = tong + i.total

    return tong
