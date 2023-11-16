from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import Group
from django.dispatch import receiver

class User(AbstractUser):

    def assign_group(self):
        if self.is_staff:
            group_name = 'Staff'
        else:
            group_name = 'Clients'
        group, created = Group.objects.get_or_create(name=group_name)
        self.groups.add(group)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_group_to_user(sender, instance: User, created: bool, **kwargs):
    if created:
        instance.assign_group()
