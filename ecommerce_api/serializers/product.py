from rest_framework import serializers

from ecommerce_api.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image', 'thumbnail']

    def create(self, validated_data):
        category = validated_data.pop('category')
        category = ProductCategory.objects.get(pk=category.id)
        return Product.objects.create(category=category, **validated_data)
