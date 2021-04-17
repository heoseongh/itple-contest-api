from django.db import models

# Create your models here.
class Contest(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=500000)