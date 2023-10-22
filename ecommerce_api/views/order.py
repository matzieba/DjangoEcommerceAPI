from rest_framework import viewsets
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

from ecommerce_api.models import Order
from ecommerce_api.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated & IsSeller]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        send_mail('Order Confirmation', 'Your order has been placed successfully.', 'from@example.com',
                  ['to@example.com'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()