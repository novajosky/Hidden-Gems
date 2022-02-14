# from sre_parse import CATEGORIES
from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.

CATEGORIES = (
    ('B', 'Business'),
    ('T', 'Trail'),
    ('R', 'Ruins'),
    ('L', 'Landmark'), 
)

class Gem(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    picture = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default = CATEGORIES[1][1],
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return reverse('detail', kwargs={'gem_id': self.id})
