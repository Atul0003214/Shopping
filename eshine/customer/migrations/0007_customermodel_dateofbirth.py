# Generated by Django 4.1.5 on 2023-01-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customermodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='DateOfBirth',
            field=models.DateField(default="2023-01-23"),
            preserve_default=False,
        ),
    ]