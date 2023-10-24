from rest_framework import serializers

from ecommerce_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'type', 'first_name', 'last_name', 'email']