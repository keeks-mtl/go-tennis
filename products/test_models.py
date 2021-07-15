from django.test import TestCase
from products.models import Category, Product


class TestProductModels(TestCase):

    def test_category_model(self):
        category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        self.assertEqual(str(category), "test_category")

    def test_product_model(self):
        category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        product = Product.objects.create(
            sku="1",
            name="test product",
            description="test description",
            price="2.99",
            rating="4",
            image="testimage.jpg",
            category=category,
            has_sizes=False,
        )
        self.assertEqual(str(product), "test product")
