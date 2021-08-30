from django.db import models
from django.db.models.base import Model

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    
    # categories for the projects for filtering projects
    ENTERPRISE='ENTERPRISE'
    ECOMMERCE='ECOMMERCE'
    AWS_CLOUD_SOLUTIONS='AWS CLOUD SOLUTIONS'
    SCHEDULING='SCHEDULING'

    CATEGORY_CHOICES = [
        (ENTERPRISE, 'ENTERPRISE'),
        (ECOMMERCE, 'ECOMMERCE'),
        (AWS_CLOUD_SOLUTIONS, 'AWS CLOUD SOLUTIONS'),
        (SCHEDULING, 'SCHEDULING'),
    ]

    category = models.CharField(
        max_length=150,
        choices=CATEGORY_CHOICES,
        default=AWS_CLOUD_SOLUTIONS,
    )
    
    # url link to project 
    url = models.URLField(max_length=200)
   
    def __str__(self):
        return self.name