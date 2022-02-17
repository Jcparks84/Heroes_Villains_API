from django.db import models
from super_type.models import Super_type

# Create your models here.

class Heroes_Villains(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Super_type, on_delete=models.CASCADE)

