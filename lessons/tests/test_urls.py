from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lessons.views import (lessons, book_lessons,
                           add_lesson, edit_lesson, delete_lesson)


class TestUrls(SimpleTestCase):

    def test_lessons_url(self):
        url = reverse("lessons")
        self.assertEquals(resolve(url).func, lessons)

    def test_book_lessons_url(self):
        url = reverse("book_lessons")
        self.assertEquals(resolve(url).func, book_lessons)

    def test_add_lesson_url(self):
        url = reverse("add_lesson")
        self.assertEquals(resolve(url).func, add_lesson)

    def test_edit_lesson_url(self):
        url = reverse("edit_lesson", args=["1"])
        self.assertEquals(resolve(url).func, edit_lesson)

    def test_delete_lesson_url(self):
        url = reverse("delete_lesson", args=["1"])
        self.assertEquals(resolve(url).func, delete_lesson)
