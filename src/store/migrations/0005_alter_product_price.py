# Generated by Django 4.2.13 on 2024-05-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_shippingadress_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
