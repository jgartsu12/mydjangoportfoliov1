from django.db import models
from django.db.models.base import Model

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    content = models.TextField()

    STATUS = [
        (0, 'Draft'),
        (1, 'Publish')
    ]

    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
