# Generated by Django 3.0.3 on 2020-08-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_shoppingbag_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingbag',
            name='size',
            field=models.CharField(max_length=128),
        ),
    ]
