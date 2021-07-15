from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from profiles.models import UserProfile
from checkout.models import Order
from profiles.forms import UserProfileForm


class TestUserViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.profile = reverse("profile")
        self.login = reverse("account_login")
        self.form = UserProfileForm

    def test_profile_login_required(self):
        ''' Test the user needs to be logged in to see the userprofile page '''

        response = self.client.get(self.profile)
        self.assertNotEqual(response.status_code, 200)

    def test_profile_page_logged_in(self):
        ''' Test the user profile page when logged in '''

        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.profile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertTemplateUsed(response, "base.html")