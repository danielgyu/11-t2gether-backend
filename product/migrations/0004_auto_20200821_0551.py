# Generated by Django 3.1 on 2020-08-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200821_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=700),
        ),
    ]
