from unicodedata import name
from django.db import models

class SuperType(models.Model):
    hero = models.CharField(max_length=255)
    villain = models.CharField(max_length=255)

# Create your models here.
