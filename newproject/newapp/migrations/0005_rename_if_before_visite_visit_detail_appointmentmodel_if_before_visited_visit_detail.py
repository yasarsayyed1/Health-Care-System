# Generated by Django 3.2.5 on 2021-07-18 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20210718_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentmodel',
            old_name='if_before_visite_visit_detail',
            new_name='if_before_visited_visit_detail',
        ),
    ]
