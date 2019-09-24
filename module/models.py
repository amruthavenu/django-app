from django.db import models

# Create your models here.
class Table(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')