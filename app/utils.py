# Tính tổng giỏ hàng
def cart_stats(cart):
    if cart is None:
        return 0, 0

    books = cart.values()

    quantity = sum([b['quantity'] for b in books])
    total = sum([b['price'] * b['quantity'] for b in books])

    return quantity, total