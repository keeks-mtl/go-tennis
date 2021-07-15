from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile


class TestUserUrls(SimpleTestCase):

    def test_profile_url(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func, profile)
