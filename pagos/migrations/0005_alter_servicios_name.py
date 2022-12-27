# Generated by Django 4.1.4 on 2022-12-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0004_alter_expired_payments_penalty_fee_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='name',
            field=models.CharField(choices=[('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Start+'), ('PM', 'Paramount+')], default='NF', max_length=2),
        ),
    ]
