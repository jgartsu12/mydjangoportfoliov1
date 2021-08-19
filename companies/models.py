from django.db import models
from django.db.models.base import Model

# Create your models here.
class Company(models.Model):
    #image and summary properties
    
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    # name = models.CharField(max_length=50)
    # makes it easier to select the company you want to pick by choosing the summary
    def __str__(self):
        return self.summary 