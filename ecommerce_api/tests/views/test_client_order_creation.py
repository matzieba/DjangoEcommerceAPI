from django.core import mail

def test_order_confirmation_email_sent(db, client, user_client, product):
    client.force_authenticate(user=user_client)

    order_data = {
        "client": user_client.pk,
        "delivery_address": "123 Street, City",
        "products": [
            {"product": product.id, "quantity": 2}
        ]
    }

    response = client.post("/ecommerce/orders/", data=order_data, format='json')

    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.subject == f"Order :{response.order.pk} Confirmation"
    assert email.body == 'Your order has been placed successfully.'