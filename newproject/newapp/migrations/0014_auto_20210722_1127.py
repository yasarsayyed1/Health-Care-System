# Generated by Django 3.2.5 on 2021-07-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0013_auto_20210722_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='drformmodel',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='drformmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('famale', 'female')], default='2', max_length=30),
        ),
    ]
