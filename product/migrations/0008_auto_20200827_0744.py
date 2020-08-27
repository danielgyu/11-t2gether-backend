# Generated by Django 3.1 on 2020-08-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200821_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.URLField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='size',
            name='image',
            field=models.URLField(max_length=3000, null=True),
        ),
    ]
