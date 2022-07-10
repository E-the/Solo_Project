from django.db import models

# Create your models here.

class App(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    watch = models.CharField(max_length=255)
    price = models.CharField(max_length=255 ,blank = True)
    details = models.CharField(max_length=255 ,blank = True)
    user_image=models.FileField(upload_to="static/images",default="default.jpg")
     
    

    




    db_table="item"