from django.test import TestCase, Client
from lessons.models import ClassType, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User


class TestLessonModels(TestCase):

    def test_class_type_model(self):
        class_type = ClassType.objects.create(
            name="test_classtype",
            friendly_name="Test Class Type",
        )
        self.assertEqual(str(class_type), "test_classtype")

    def test_lesson_model(self):
        class_type = ClassType.objects.create(
            name="test_classtype",
            friendly_name="Test Class Type",
        )
        coach = Coach.objects.create(
            first_name="test",
            last_name="Tester",
            email="test@test.com",
            phone_number="1234567",
            description="test description",
            image="image.jpg",
        )
        lesson = Lesson.objects.create(
            class_type=class_type,
            coach=coach,
            description="test description",
            price="35.00",
            date="2021-12-12",
            time="02:21 PM",
            spots="4",
        )
        self.assertEqual(str(lesson), "Lesson on 2021-12-12 by test")
