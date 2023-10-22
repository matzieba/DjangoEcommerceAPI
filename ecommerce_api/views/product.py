from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from ecommerce_api.models import Product, ProductCategory
from ecommerce_api.permissions import IsClient, IsSeller
from ecommerce_api.serializers.product import ProductCategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated & IsClient]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'description', 'category__name', 'price']
    ordering_fields = ['name', 'category__name', 'price']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny, ]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSeller, ]
        else:
            self.permission_classes = [IsAuthenticated & IsClient]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset
