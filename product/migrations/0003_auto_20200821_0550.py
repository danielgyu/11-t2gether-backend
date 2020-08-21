# Generated by Django 3.1 on 2020-08-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.URLField(max_length=400),
        ),
    ]