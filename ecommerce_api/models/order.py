

from django.db import models

from django.utils import timezone

from ecommerce_api import settings


class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    delivery_address_street = models.CharField(max_length=100, blank=True, null=True)
    delivery_address_city = models.CharField(max_length=50, blank=True, null=True)
    delivery_address_country = models.CharField(max_length=50, blank=True, null=True)
    delivery_address_house_number = models.CharField(max_length=50, blank=True, null=True)
    delivery_address_postal_code = models.CharField(max_length=25, blank=True, null=True)
    products = models.ManyToManyField('ecommerce_api.Product', through='ecommerce_api.OrderProduct')
    date_ordered = models.DateTimeField(default=timezone.now)
    payment_due = models.DateTimeField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


class OrderProduct(models.Model):
    product = models.ForeignKey('ecommerce_api.Product', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


