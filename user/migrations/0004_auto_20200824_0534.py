# Generated by Django 3.0.3 on 2020-08-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200824_0037'),
        ('user', '0003_auto_20200824_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='shopping_bag',
            field=models.ManyToManyField(related_name='shopping', through='user.ShoppingBag', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='wish_list',
            field=models.ManyToManyField(related_name='wish', through='user.Wishlist', to='product.Product'),
        ),
    ]