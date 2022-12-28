from .models import Servicios,Payment_user,Expired_payments
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiciosSerializer,PaymentUserSerializer,ExpiredPaymentsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class ServiciosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer
    #permission_classes = [IsAuthenticated]
    throttle_scope = 'servicios'

class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentUserSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['paymentDate','expirationDate']
    throttle_scope = 'payment'

class ExpiredPaymentsCreateApiView(generics.ListCreateAPIView):
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredPaymentsSerializer
    throttle_scope = 'payment'

    def get(self,request):
        todos=Expired_payments.objects.all()
        serializer=ExpiredPaymentsSerializer (todos,many=True)
        return Response({
            "ok":True,
            "message":serializer.data
        })
    
    def post(self,request):
        serializer=ExpiredPaymentsSerializer (data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "ok":True,
                "message":"ExpiredPayments_created"
            },status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message":serializer.errors
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)