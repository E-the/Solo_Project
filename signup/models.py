from django.db import models

# Create your models here.
class Signup(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255 ,blank = True)
    password=models.CharField(max_length=255)
     
    

    



    class Meta:
        db_table="signup"