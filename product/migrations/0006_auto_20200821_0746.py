# Generated by Django 3.1 on 2020-08-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200821_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='image',
            field=models.URLField(max_length=700, null=True),
        ),
    ]
