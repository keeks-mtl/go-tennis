from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from lessons.models import ClassType, Lesson
from coaches.models import Coach


class TestLessonViews(TestCase):
    "test the lesson views for all users"

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.class_type = ClassType.objects.create(
            name="test_class_type",
            friendly_name="Test ClassType"
        )
        self.coach = Coach.objects.create(
            first_name="test",
            last_name="Tester",
            email="test@test.com",
            phone_number="1234567",
            description="test description",
            image="image.jpg",
        )
        self.lesson = Lesson.objects.create(
            class_type=self.class_type,
            coach=self.coach,
            description="test description",
            price="35.00",
            date="2021-12-12",
            time="02:21 PM",
            spots="4",
        )
        self.book_lessons = reverse("book_lessons")

    def test_book_lessons_view(self):
        ''' Test the book lessons view '''

        response = self.client.get(self.book_lessons)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lessons/book.html")
        self.assertTemplateUsed(response, "base.html")