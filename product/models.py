from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    watch_name = models.CharField(max_length=255)
    watch_price = models.FloatField( blank=True)
    watch_detail = models.CharField(max_length=2000 ,blank = True)
    watch_stock = models.CharField(max_length=255 ,blank = True)
    watch_tec = models.CharField(max_length=255 ,blank = True)  
    product_catog = models.CharField(max_length=255 ,blank = True)  
    watch_image=models.FileField(upload_to="static/images",default="default.jpg")
    watch_image2=models.FileField(upload_to="static/images",default="default.jpg")
    watch_image3=models.FileField(upload_to="static/images",default="default.jpg")
     
    

    




    class Meta:
        db_table="product"