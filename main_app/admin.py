from django.contrib import admin
from .models import Gem, Review, Photo

# Register your models here.

admin.site.register(Gem)
admin.site.register(Review)
admin.site.register(Photo)
