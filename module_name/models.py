from django.db import models

# Create your models here.

class Module_name(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    watch_name = models.CharField(max_length=255)
    watch_price = models.CharField(max_length=255 ,blank = True)
    watch_detail = models.CharField(max_length=2000 ,blank = True)
    watch_image=models.FileField(upload_to="static/images",default="default.jpg")
     
    

    




    class Meta:
        db_table="module_name"