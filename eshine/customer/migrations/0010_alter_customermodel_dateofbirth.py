# Generated by Django 4.1.5 on 2023-02-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_customermodel_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='DateOfBirth',
            field=models.DateField(verbose_name='YYYY-MM-DD'),
        ),
    ]
