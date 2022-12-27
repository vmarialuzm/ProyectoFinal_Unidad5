from .models import Servicios,Payment_user,Expired_payments
from rest_framework import viewsets
from .serializers import ServiciosSerializer,PaymentUserSerializer,ExpiredPaymentsSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentUserSerializer

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredPaymentsSerializer 