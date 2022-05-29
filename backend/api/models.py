from django.db import models
from matplotlib import image

# Create your models here.
class Usr(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Announcements(models.Model):
    header = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.DateField()
    image = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False)
    alt = models.CharField(max_length=100)

class Queries(models.Model):
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=100)
