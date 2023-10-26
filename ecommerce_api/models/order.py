

from django.db import models

from django.utils import timezone

from ecommerce_api import settings


class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    delivery_address = models.CharField(max_length=300)
    products = models.ManyToManyField('ecommerce_api.Product', through='ecommerce_api.OrderProduct')
    date_ordered = models.DateField(default=timezone.now)
    payment_due = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


class OrderProduct(models.Model):
    product = models.ForeignKey('ecommerce_api.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


