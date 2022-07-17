from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.

class Ordertable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    order_image=models.FileField(upload_to="static/images",default="default.jpg")
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    product_brand = models.CharField(max_length=255 ,blank = True)  
    order_name = models.CharField(max_length=255)
    order_price = models.FloatField( blank=True)
    order_address = models.CharField(max_length=2000 ,blank = True)
    order_quantity = models.CharField(max_length=255 ,blank = True)
    order_phonenumber = models.CharField(max_length=255 ,blank = True)  
    order_pincode = models.CharField(max_length=255 ,blank = True)  
    order_email = models.CharField(max_length=255 ,blank = True)  
    order_payment = models.CharField(max_length=255 ,blank = True)  
    order_total = models.CharField(max_length=255 ,blank = True)  
    order_date = models.CharField(max_length=255 ,blank = True)  

     
    

    




    class Meta:
        db_table="ordertable"
