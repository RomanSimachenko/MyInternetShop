# Generated by Django 4.0.1 on 2022-01-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_cart_product_cartproduct_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'verbose_name': 'Cart product', 'verbose_name_plural': 'Cart products'},
        ),
    ]
