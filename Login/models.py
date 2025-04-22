from django.db import models

# Create your models here.
class user(models.Model):
    user_email=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_country=models.CharField(max_length=40)

    