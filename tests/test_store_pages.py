from flask import url_for, jsonify

from tests.base_test import BaseTestCase, create_data
from app.models import *
import json


class StorePagesTest(BaseTestCase):
    # Test thêm mỗi lần 1 sản phẩm vào giỏ
    def test_add_one_product_to_cart(self):
        data = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000
        })
        with self.client:
            response = self.client.post("/api/cart", data=data, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))

            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Thêm giỏ hàng thành công")
            self.assertTrue(data['total_amount'] == 115000)
            self.assertTrue(data['total_quantity'] == 1)

    # Test thêm sản phẩm giống nhau vào giỏ
    def test_add_same_products_to_cart(self):
        data = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000
        })

        with self.client:
            self.client.post("/api/cart", data=data, content_type="application/json")

            response = self.client.post("/api/cart", data=data, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))

            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Thêm giỏ hàng thành công")
            self.assertTrue(data['total_amount'] == 230000)
            self.assertTrue(data['total_quantity'] == 2)

    # Test thêm những sản phẩm khác nhau
    def test_add_different_products_to_cart(self):
        data1 = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000
        })

        data2 = json.dumps({
            'id': str(2),
            'name': 'Án Mạng Mười Một Chữ',
            'image': 'assets/img/book_img/img8.jpg',
            'price': 110000
        })

        with self.client:
            self.client.post("/api/cart", data=data1, content_type="application/json")

            response = self.client.post("/api/cart", data=data2, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))

            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Thêm giỏ hàng thành công")
            self.assertTrue(data['total_amount'] == 225000)
            self.assertTrue(data['total_quantity'] == 2)

    # Test bớt 1 sản phẩm trong giỏ
    def test_remove_product_from_cart(self):
        data1 = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000
        })
        with self.client:
            self.client.post("/api/cart", data=data1, content_type="application/json")
            response = self.client.post("/api/cart", data=data1, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))
            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['total_quantity'] == 2)

            response = self.client.post('/api/remove-item-cart', data=data1, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))
            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Cập nhật giỏ hàng thành công")
            self.assertTrue(data['total_quantity'] == 1)

    # Test xóa 1 sản phẩm khỏi giỏ hàng
    def test_delete_item_from_cart(self):
        data1 = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000
        })
        with self.client:
            self.client.post("/api/cart", data=data1, content_type="application/json")
            response = self.client.post("/api/cart", data=data1, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))
            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['total_quantity'] == 2)

            response = self.client.delete('/api/cart/1', data=data1, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))
            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Xóa thành công")
            self.assertTrue(data['total_quantity'] == 0)
            self.assertTrue(data['total_amount'] == 0)

    # Test thêm và xóa số lượng nhiều trong 1 sản phẩm
    def test_add_or_remove_items_from_cart(self):
        data = json.dumps({
            'id': str(1),
            'name': 'Sự Im Lặng Của Bầy Cừu',
            'image': 'assets/img/book_img/img6.jpg',
            'price': 115000,
            'quantity': 3
        })
        with self.client:
            response = self.client.post('/api/add_remove_cart', data=data, content_type="application/json")

            data = json.loads(response.get_data(as_text=True))
            self.assertTrue(response.status_code == 200)
            self.assertTrue(data['message'] == "Cập nhật giỏ hàng thành công")
            self.assertTrue(data['total_quantity'] == 3)
            self.assertTrue(data['total_amount'] == 345000)

    # Test trang chủ
    def test_index_page(self):
        with self.client:
            response = self.client.get('/')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'Login' in response.data)
            self.assertTrue(b'Username' in response.data)
            self.assertTrue(b'Password' in response.data)

    # Test trang thanh toán
    def test_checkout_page(self):
        with self.client:
            response = self.client.get('/checkout')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'first_name' in response.data)
            self.assertTrue(b'last_name' in response.data)
            self.assertTrue(b'address' in response.data)
            self.assertTrue(b'phone' in response.data)
            self.assertTrue(b'order_comments' in response.data)

    # Test trang thanh toán khi có đăng nhập
    def test_checkout_page_with_login(self):
        create_data()
        with self.client:
            self.client.post("/login", data=dict(username='admin456', password='654321'),
                             follow_redirects=True)

            response = self.client.get('/checkout')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'first_name' not in response.data)
            self.assertTrue(b'last_name' not in response.data)
            self.assertTrue(b'address' in response.data)
            self.assertTrue(b'phone' in response.data)
            self.assertTrue(b'order_comments' in response.data)

    # Test trang danh sách sản phẩm với số trang đúng
    def test_shop_list_page_with_valid_page(self):
        create_data()
        with self.client:
            response = self.client.get('/shop-list/1')

        self.assertTrue(response.status_code == 200)

    # Test trang danh sách sản phẩm với số trang sai
    def test_shop_list_page_with_invalid_page(self):
        create_data()
        with self.client:
            response = self.client.get('/shop-list/2')

        self.assertFalse(response.status_code == 200)

    # Test trang thông tin chi tiết của sách với id sách đúng
    def test_book_detail_page_with_valid_bookID(self):
        create_data()
        with self.client:
            response = self.client.get('/shop-list/book-detail/3')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'add-to-cart' in response.data)
            self.assertTrue(b'quantity' in response.data)

    # Test trang thông tin chi tiết của sách với id sách sai
    def test_book_detail_page_with_invalid_bookID(self):
        create_data()
        with self.client:
            response = self.client.get('/shop-list/book-detail/4')

            self.assertTrue(response.status_code == 200)
            self.assertTrue(b'add-to-cart' not in response.data)

    # Test trang thống kê có login tài khoản admin
    def test_report_page_after_login(self):
        create_data()
        with self.client:
            self.client.post("/login", data=dict(username='admin123', password='123456'),
                             follow_redirects=True)

            response = self.client.get('/report')

            self.assertTrue(response.status_code == 200)

    # Test trang thống kê khi chưa login
    def test_report_page_not_login(self):
        create_data()
        with self.client:
            response = self.client.get('/report')

            self.assertFalse(response.status_code == 200)
