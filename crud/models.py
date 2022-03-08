from django.db import models

# Create your models here.

class infos(models.Model):
    pid = models.AutoField
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
