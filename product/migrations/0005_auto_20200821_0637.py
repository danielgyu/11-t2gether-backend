# Generated by Django 3.1 on 2020-08-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200821_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='information',
            name='ingredient',
            field=models.TextField(),
        ),
    ]
