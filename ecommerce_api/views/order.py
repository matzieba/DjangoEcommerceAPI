
from typing import Optional

from django.db.models import Count
from rest_framework import viewsets
from django.core.mail import send_mail
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from ecommerce_api.models import Order, OrderProduct
from ecommerce_api.permissions import IsSeller, IsClient
from ecommerce_api.serializers.order import OrderReadSerializer, OrderCreateSerializer, OrderStatsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated & IsClient]

    def get_serializer_class(self):
        if self.request.method in ["GET", "LIST"]:
            return OrderReadSerializer
        else:
            return OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)

        self.send_confirmation_email(order, request.user.email)

        read_serializer = OrderReadSerializer(order)

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def send_confirmation_email(self, order: Order, to_email: str) -> Optional[None]:
        subject = f'Order:{order.pk} Confirmation'
        message = 'Your order has been placed successfully.'
        from_email = 'from@example.com'
        send_mail(subject, message, from_email, [to_email], fail_silently=False)


class OrderStatsViewSet(ListModelMixin, GenericViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated & IsSeller]
    serializer_class = OrderStatsSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        date_from = serializer.validated_data["date_from"]
        date_to = serializer.validated_data["date_to"]
        num_products = serializer.validated_data["num_products"]

        data = (OrderProduct.objects
                .filter(order__date_ordered__range=[date_from, date_to])
                .values("product__name")
                .annotate(total=Count("product"))
                .order_by("-total")[:num_products])

        output = [{"product": d["product__name"], "orders": d["total"]} for d in data]

        return Response(output)