from rest_framework import serializers
from django.utils import timezone
from ecommerce_api.models import Order, OrderProduct, User, Product


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')


class OrderCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('client', 'delivery_address', 'products', 'date_ordered', 'payment_due', 'total_price')

    def to_internal_value(self, data):
        products_data = data.get('products', None)
        data['total_price'] = self.calculate_total_price(products_data)
        data['payment_due'] = timezone.now() + timezone.timedelta(days=5)
        return super().to_internal_value(data)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            OrderProduct.objects.create(order=order, **product_data)
        return order

    def calculate_total_price(self, products_data):
        total = 0

        for product_data in products_data:
            product = Product.objects.get(pk=product_data.get('product'))
            total += product_data['quantity'] * product.price

        return total


class OrderReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('client', 'delivery_address', 'products', 'date_ordered', 'payment_due', 'total_price')
