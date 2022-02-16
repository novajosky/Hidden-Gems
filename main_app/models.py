
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0],
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.name } ({ self.id })"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gem_id': self.id})

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Review(models.Model):
    content = models.TextField(max_length=300)
    rating = models.IntegerField(
        choices=RATINGS,
        default=RATINGS[4][0]
    )
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for gem_id: {self.gem_id} @{self.url}"