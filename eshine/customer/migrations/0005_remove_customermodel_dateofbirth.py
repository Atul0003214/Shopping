# Generated by Django 4.1.5 on 2023-01-23 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_customermodel_email_customermodel_dateofbirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermodel',
            name='DateOfBirth',
        ),
    ]