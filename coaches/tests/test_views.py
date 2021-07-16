from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from coaches.models import Coach, Comment


class TestCoachViews(TestCase):
    "test the coach views for all users"

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.coach = Coach.objects.create(
            first_name="test",
            last_name="Tester",
            email="test@test.com",
            phone_number="1234567",
            description="test description",
            image="image.jpg"
        )
        self.comment = Comment.objects.create(
            coach=self.coach,
            author=self.user,
            comment="Test Comment",
            stars="4",
        )
        self.coaches = reverse("view_coaches")
        self.coach = reverse("view_coach",
                             kwargs={"coach_id": self.coach.id})

    def test_view_coaches(self):
        ''' Test the coaches view '''

        response = self.client.get(self.coaches)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "coaches/coaches.html")
        self.assertTemplateUsed(response, "base.html")

    def test_view_coach_view(self):
        ''' Test the coach view '''
        response = self.client.get(self.coach)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "coaches/coach.html")
        self.assertTemplateUsed(response, "base.html")
