# Generated by Django 4.0.1 on 2022-01-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_product_cartproduct_cart_product_delete_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='cart_product',
            new_name='product',
        ),
    ]