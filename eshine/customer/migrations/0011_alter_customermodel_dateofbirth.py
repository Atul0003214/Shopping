# Generated by Django 4.1.5 on 2023-02-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_customermodel_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='DateOfBirth',
            field=models.DateField(verbose_name='DateOfBirth YYYY-MM-DD'),
        ),
    ]