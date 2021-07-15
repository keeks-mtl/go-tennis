from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.checkout = reverse("checkout")
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testPassword'
        )
        self.item = Product.objects.create(
            sku="1",
            name="test product",
            description="test description",
            price="2.99",
            rating="4",
            has_sizes=False,
        )
        self.add_to_bag = reverse("add_to_bag",
                                   kwargs={"item_id": self.item.id})

    def test_checkout_view_with_empty_bag(self):
        ''' Test the checkout view with an empty bag. '''

        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "There's nothing in your bag at the moment")