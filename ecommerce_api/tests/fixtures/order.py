import pytest
from model_bakery import baker
from django.utils import timezone

from ecommerce_api.models import Order, OrderProduct


@pytest.fixture()
def orders(product1, product2, user_client):
    order_products = []
    for i in range(5):
        order = baker.make(
            Order,
            client=user_client,
            delivery_address='123 Street, City',
            date_ordered=timezone.now(),
            payment_due=timezone.now() + timezone.timedelta(days=5),
            total_price=product1.price
        )
        order_product = baker.make(
            OrderProduct,
            product=product1,
            order=order,
            quantity=1
        )
        order_products.append(order_product)
    for i in range(3):
        order = baker.make(
            Order,
            client=user_client,
            delivery_address='123 Street, City',
            date_ordered=timezone.now(),
            payment_due=timezone.now() + timezone.timedelta(days=5),
            total_price=product2.price
        )
        order_product = baker.make(
            OrderProduct,
            product=product2,
            order=order,
            quantity=1
        )
        order_products.append(order_product)
    return order_products

@pytest.fixture()
def order_stats_data():
    return {
        'date_from': '2023-01-01',
        'date_to': '2023-12-31',
        'num_products': 5
    }

@pytest.fixture()
def order_stats_data_1():
    return {
        'date_from': '2023-01-01',
        'date_to': '2023-12-31',
        'num_products': 1
    }