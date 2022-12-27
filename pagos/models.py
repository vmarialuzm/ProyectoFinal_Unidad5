from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Servicios(models.Model):
    id = models.AutoField(primary_key=True)

    class Nombres(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    name = models.CharField(
        max_length=2,
        choices=Nombres.choices,
        default=Nombres.NETFLIX,
    )
    description = models.TextField()
    logo = models.URLField(max_length=200)

    class Meta:
        db_table="servicios"

class Payment_user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    service_id = models.ForeignKey(Servicios,on_delete=models.CASCADE,related_name='servicios')
    amount = models.FloatField(default=0.0)
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField(null=False)

    class Meta:
        db_table="payment_user"

class Expired_payments(models.Model):
    id = models.AutoField(primary_key=True)
    payment_user_id = models.ForeignKey(Payment_user,on_delete=models.CASCADE,related_name='payment_user')
    penalty_fee_amount = models.FloatField(default=0.0)

    class Meta:
        db_table="expired_payments"

