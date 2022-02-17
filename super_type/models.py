from unicodedata import name
from django.db import models

class Super_type(models.Model):
    name = models.CharField(max_length=255)
    power = models.IntegerField()

# Create your models here.
