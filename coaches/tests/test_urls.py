from django.test import SimpleTestCase
from django.urls import reverse, resolve
from coaches.views import (view_coaches, view_coach,
                           add_coach, edit_coach, delete_coach)


class TestUrls(SimpleTestCase):

    def test_view_coaches_url(self):
        url = reverse("view_coaches")
        self.assertEquals(resolve(url).func, view_coaches)

    def test_view_coach_url(self):
        url = reverse("view_coach", args=["1"])
        self.assertEquals(resolve(url).func, view_coach)

    def test_add_coach_url(self):
        url = reverse("add_coach")
        self.assertEquals(resolve(url).func, add_coach)

    def test_edit_coach_url(self):
        url = reverse("edit_coach", args=["1"])
        self.assertEquals(resolve(url).func, edit_coach)

    def test_delete_coach_url(self):
        url = reverse("delete_coach", args=["1"])
        self.assertEquals(resolve(url).func, delete_coach)
