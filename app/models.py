from django.db import models
from datetime import datetime

# Create your models here.

class App(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    watch = models.CharField(max_length=255)
    price = models.CharField(max_length=255 ,blank = True)
    details = models.CharField(max_length=255 ,blank = True)
    user_image=models.FileField(upload_to="static/images",default="default.jpg")
     
class Feedback(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    feedback = models.CharField(max_length=250)
    date_posted = models.DateTimeField(default=datetime.now())    

    




    db_table="item"