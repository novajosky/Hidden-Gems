from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.

class Gem(models.Model):
    name = models.CharField(max_length=100)
    location = models.IntegerField()
    description = models.TextField(max_length=300)
    picture = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)