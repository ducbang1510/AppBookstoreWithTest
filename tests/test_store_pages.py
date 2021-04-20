from flask import url_for, jsonify

from tests.base_test import BaseTestCase, create_data
from app.models import *
from app import utils
import json


class StorePagesTest(BaseTestCase):
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
