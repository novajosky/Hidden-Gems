from django.forms import ModelForm
from .models import Review, Photo

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['url', 'gem']