# Generated by Django 4.0.5 on 2022-07-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_watch_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='watch_image2',
            field=models.FileField(default='default.jpg', upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='watch_image3',
            field=models.FileField(default='default.jpg', upload_to='static/images'),
        ),
    ]
