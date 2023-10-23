from django.core import mail
from django.utils import timezone, dateparse
from freezegun import freeze_time

@freeze_time("2023-10-23 07:19:33")
def test_order_creation(db, client, user_client, product):
    client.force_authenticate(user=user_client)

    product_quantity = 2

    order_data = {
        "client": user_client.pk,
        "delivery_address": "123 Street, City",
        "products": [
            {"product": product.id, "quantity": product_quantity}
        ]
    }

    response = client.post("/ecommerce/orders/", data=order_data, format='json')

    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.body == 'Your order has been placed successfully.'

    expected_time = timezone.now() + timezone.timedelta(days=5)
    response_time = dateparse.parse_datetime(response.data['payment_due'])
    assert response_time == expected_time

    expected_total_price = product.price * product_quantity
    assert response.data['total_price'] == str(expected_total_price)


