from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Category, Product


class TestBagViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse("home")
        self.view_bag = reverse("view_bag")
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            category=self.category,
            sku="1",
            name="test product",
            description="test description",
            price="2.99",
            rating="4",
            image="testimage.jpg",
            has_sizes=False,
        )

    def test_view_bag_view_GET(self):
        ''' test the view bag page  '''

        response = self.client.get(self.view_bag)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")
        self.assertTemplateUsed(response, "base.html")
