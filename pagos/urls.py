from . import api
from .api import ExpiredPaymentsCreateApiView
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'servicios', api.ServiciosViewSet, 'servicios')
router.register(r'payment_user', api.PaymentUserViewSet, 'payment_user')

urlpatterns=[
    path("expired_payments/",ExpiredPaymentsCreateApiView.as_view(),name='expired_payments')
]

urlpatterns += router.urls