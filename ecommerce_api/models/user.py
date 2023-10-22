from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('seller', 'Seller'),
    )

    role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)