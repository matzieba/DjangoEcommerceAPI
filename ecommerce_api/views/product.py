from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ecommerce_api.models import Product, ProductCategory
from ecommerce_api.permissions import IsClient
from ecommerce_api.serializers import ProductCategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated & IsClient]

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset
