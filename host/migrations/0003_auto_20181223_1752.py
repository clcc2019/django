# Generated by Django 2.1.4 on 2018-12-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_auto_20181223_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostname',
            name='ssl',
            field=models.FileField(blank=True, null=True, upload_to='ssl_up'),
        ),
    ]
