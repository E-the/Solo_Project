# Generated by Django 4.0.5 on 2022-06-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='password',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
