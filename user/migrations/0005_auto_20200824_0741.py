# Generated by Django 3.0.3 on 2020-08-24 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200824_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingbag',
            old_name='procut_id',
            new_name='product_id',
        ),
    ]
