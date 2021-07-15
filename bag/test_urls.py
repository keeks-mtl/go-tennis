from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag.views import (view_bag, add_to_bag, edit_bag,
                       remove_product, book_lesson, remove_lesson)


class TestBagUrls(SimpleTestCase):

    def test_view_bag_url(self):
        url = reverse("view_bag")
        self.assertEquals(resolve(url).func, view_bag)

    def test_add_to_bag_url(self):
        url = reverse("add_to_bag", args=["1"])
        self.assertEquals(resolve(url).func, add_to_bag)

    def test_edit_bag_url(self):
        url = reverse("edit_bag", args=["1"])
        self.assertEquals(resolve(url).func, edit_bag)

    def test_remove_product_url(self):
        url = reverse("remove_product", args=["1"])
        self.assertEquals(resolve(url).func, remove_product)

    def test_book_lesson_url(self):
        url = reverse("book_lesson", args=["1"])
        self.assertEquals(resolve(url).func, book_lesson)

    def test_remove_lesson_url(self):
        url = reverse("remove_lesson", args=["1"])
        self.assertEquals(resolve(url).func, remove_lesson)