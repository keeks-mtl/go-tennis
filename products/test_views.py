from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Category, Product


class TestProductViews(TestCase):
    "test the stock views for all users"

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
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
        self.products = reverse("products")
        self.product_detail = reverse("product_detail",
                                   kwargs={"product_id": self.product.id})

    def test_products_view(self):
        ''' Test the products view '''

        response = self.client.get(self.products)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertTemplateUsed(response, "base.html")

    def test_products_views_with_sort(self):
        ''' Test the products view with a direction parameter '''

        response = self.client.get(self.products,
                                   {"sort": "name",
                                    "direction": "desc"})
        context = response.context
        self.assertTrue(context['current_sorting'])
        self.assertEqual(context['current_sorting'], "name_desc")

    def test_view_product_detail_view(self):
        ''' Test the product_detail view '''
        response = self.client.get(self.product_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertTemplateUsed(response, "base.html")