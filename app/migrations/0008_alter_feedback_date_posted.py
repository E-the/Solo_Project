# Generated by Django 4.0.5 on 2022-07-19 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 16, 9, 1, 639010)),
        ),
    ]
