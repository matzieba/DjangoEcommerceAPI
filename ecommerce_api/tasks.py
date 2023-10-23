from celery import shared_task
from django.core.mail import send_mail

import datetime
from django.utils import timezone

from ecommerce_api.models import Order


@shared_task
def send_payment_reminder():
    orders = Order.objects.filter(payment_due_date__lte=timezone.now() + datetime.timedelta(days=1))

    for order in orders:
        send_mail(
            'Payment Reminder',
            'The due date for your payment is tomorrow.',
            'admin@ecommerce.com',
            [order.client.email],
        )