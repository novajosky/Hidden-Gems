import os
from re import template
import boto3
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Gem, Review, Photo
from .forms import ReviewForm


# Define the home view
def home(request):
    return render(request, 'base.html')

@login_required
def maps(request):
  gems = Gem.objects.all()
  mapbox_access_token = os.environ['MAP_KEY']
  return render(request, 'gems/maps.html', 
    { 'MAP_KEY' : mapbox_access_token, 'gems': gems })

def gems_index(request):
  gems = Gem.objects.all
  return render(request, 'gems/index.html', {'gems': gems})

@login_required
def gems_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  review_form = ReviewForm()
  return render(request, 'gems/detail.html', {
    'gem': gem, 'review_form': review_form, 'MAP_KEY': os.environ['MAP_KEY']
  })

class GemCreate(LoginRequiredMixin, CreateView):
  model = Gem
  fields = ['name', 'location', 'latitude', 'longitude', 'description', 'category']
  success_url = '/gems/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GemUpdate(LoginRequiredMixin, UpdateView):
  model = Gem
  fields = ['location', 'latitude', 'longitude', 'description', 'category']

class GemDelete(LoginRequiredMixin, DeleteView):
  model = Gem
  success_url = '/gems/'

  def user_valid(self):
    self.object = self.get_object()
    return self.object.user == self.request.user

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def add_review(request, gem_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.gem_id = gem_id
    new_review.save()
  return redirect('detail', gem_id=gem_id)

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  template = "/main_app/_confirm_delete.html"
  success_url = '/gems/'

def add_photo(request, gem_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, gem_id=gem_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', gem_id=gem_id)

class PhotoDelete(LoginRequiredMixin, DeleteView):
  model = Photo
  # template = "/main_app/photo_confirm_delete.html"
  success_url = '/gems/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def some_function(request):
  secret_key = os.environ['SECRET_KEY']