# Generated by Django 4.0.5 on 2022-07-19 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_feedback_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 19, 47, 25, 496716)),
        ),
    ]
