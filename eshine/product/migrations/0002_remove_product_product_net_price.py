# Generated by Django 4.1.5 on 2023-01-24 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_net_price',
        ),
    ]
