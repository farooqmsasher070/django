from django.db import models

# Create your models here.
class Test(models.Model):
    fistname=models.CharField(max_length=255)