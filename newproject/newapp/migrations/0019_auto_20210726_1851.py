# Generated by Django 3.2.5 on 2021-07-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0018_rename_orders_ordersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='ordersmodel',
            name='phone_number',
            field=models.CharField(blank=True, default='-', max_length=12),
        ),
    ]
