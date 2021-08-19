from django.db import models
from django.db.models.base import Model

# Create your models here.
class Company(models.Model):
#   image and summary properites

    image = models.ImageField(upload_to='images/')
   
    summary = models.CharField(max_length=200)