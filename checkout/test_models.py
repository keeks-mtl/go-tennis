from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Category, Product


class TestCheckoutModels(TestCase):

    def test_order_model(self):
        ''' test the order model '''
        order = Order.objects.create(
            full_name="Test User"
        )

        self.assertEqual(str(order), order.order_number)

    def test_orderlineitem_model(self):
        ''' test the orderlineitem model '''

        order = Order.objects.create(
            full_name="Test User"
        )

        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )

        product = Product.objects.create(
            category=self.category,
            sku="1",
            name="test product",
            description="test description",
            price="2.99",
            rating="4",
            image="testimage.jpg",
            has_sizes=False,
        )

        order_line_item = OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            lineitem_total=100,
        )

        self.assertEqual(str(order_line_item),
                         f"SKU 1 on order {order.order_number}")
