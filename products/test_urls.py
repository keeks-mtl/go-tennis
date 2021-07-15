from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (products, product_detail,
                            add_product, edit_product, delete_product)


class TestUrls(SimpleTestCase):

    def test_products_url(self):
        url = reverse("products")
        self.assertEquals(resolve(url).func, products)

    def test_product_detail_url(self):
        url = reverse("product_detail", args=["1"])
        self.assertEquals(resolve(url).func, product_detail)

    def test_add_product_url(self):
        url = reverse("add_product")
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url(self):
        url = reverse("edit_product", args=["1"])
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url(self):
        url = reverse("delete_product", args=["1"])
        self.assertEquals(resolve(url).func, delete_product)
