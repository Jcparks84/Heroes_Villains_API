from unicodedata import name
from django.db import models

class SuperType(models.Model):
    type = models.CharField(max_length=255, null=True)

    

# Create your models here.
