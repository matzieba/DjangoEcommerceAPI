"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ecommerce_api.views.product import ProductViewSet
from ecommerce_api.views.user import LoginView, UserMeView

router = DefaultRouter()

from ecommerce_api.views.order import OrderViewSet, OrderStatsViewSet

api_urls = []

router.register(r'orders', OrderViewSet, basename='order')
router.register(r'products', ProductViewSet, basename='product')

api_urls += router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ecommerce/", include(api_urls)),
    path('ecommerce/order-stats/', OrderStatsViewSet.as_view({'get': 'list'})),
    path('login/', LoginView.as_view(), name='api-login'),
    path('userme/', UserMeView.as_view(), name='userme'),
]
