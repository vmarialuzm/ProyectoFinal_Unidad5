from rest_framework import serializers
from .models import Servicios,Payment_user,Expired_payments

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'
        read_only_fields = '__all__',

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = '__all__',

class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'
        read_only_fields = '__all__',