from django.test import TestCase, Client
from coaches.models import Coach, Comment
from django.contrib.auth.models import User


class TestCoachModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

    def test_coach_model(self):
        coach = Coach.objects.create(
            first_name="test",
            last_name="Tester",
            email="test@test.com",
            phone_number="1234567",
            description="test description",
            image="image.jpg",
        )
        self.assertEqual(str(coach), "test")

    def test_comment_model(self):
        self.client.login(
            username="testuser", password="testpassword")
        coach = Coach.objects.create(
            first_name="test",
            last_name="Tester",
            email="test@test.com",
            phone_number="1234567",
            description="test description",
            image="image.jpg"
        )
        comment = Comment.objects.create(
            coach=coach,
            author=self.user,
            comment="Test Comment",
            stars="5",
        )
        self.assertEqual(str(comment), "Comment about test by testuser")
