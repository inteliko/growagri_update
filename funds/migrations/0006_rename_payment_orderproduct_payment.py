# Generated by Django 5.0.4 on 2024-05-10 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_remove_order_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='Payment',
            new_name='payment',
        ),
    ]