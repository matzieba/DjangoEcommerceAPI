from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import Group
from django.dispatch import receiver

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'client'),
        ('seller', 'seller'),
    )

    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def assign_group(self):
        group, created = Group.objects.get_or_create(name=self.type)
        self.save()
        self.groups.add(group)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_group_to_user(sender, instance, created, **kwargs):
    if created:
        instance.assign_group()
