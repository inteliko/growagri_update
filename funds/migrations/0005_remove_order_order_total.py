# Generated by Django 5.0.4 on 2024-04-25 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0004_order_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_total',
        ),
    ]
