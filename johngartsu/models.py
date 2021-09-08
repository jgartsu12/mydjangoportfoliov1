from django.db import models
from django.db.models.base import Model
# Create your models here.


class JohnGartsu(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name