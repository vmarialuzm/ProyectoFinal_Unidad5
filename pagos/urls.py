from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicios', api.ServiciosViewSet, 'servicios')
router.register(r'payment_user', api.PaymentUserViewSet, 'payment_user')
router.register(r'expired_payments', api.ExpiredPaymentsViewSet, 'expired_payments')

urlpatterns = router.urls