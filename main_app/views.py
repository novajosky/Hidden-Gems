from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Gem, Review
from .forms import ReviewForm
import os

# Define the home view
def home(request):
    return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

@login_required
def maps(request):
  mapbox_access_token = 'pk.eyJ1IjoibWlrZW5vdmEiLCJhIjoiY2t6ajF0ZHd2MDVrMjJvbXE2OG0xbDg3NCJ9.q_wwOsFi-0Pbyhx5ESJfTg'
  return render(request, 'gems/maps.html', 
    { 'mapbox_access_token' : mapbox_access_token })

def gems_index(request):
  gems = Gem.objects.filter(user=request.user)
  return render(request, 'gems/index.html', {'gems': gems})

def gems_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  review_form = ReviewForm()
  return render(request, 'gems/detail.html', {
    'gem': gem, 'review_form': review_form
  })

class GemCreate(CreateView):
  model = Gem
  fields = ['name', 'location', 'latitude', 'longitude', 'description',  'picture', 'category']
  success_url = '/gems/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GemUpdate(UpdateView):
  model = Gem
  fields = ['location', 'latitude', 'longitude', 'description', 'picture', 'category']

class GemDelete(DeleteView):
  model = Gem
  success_url = '/gems/'

def add_review(request, gem_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.gem_id = gem_id
    new_review.save()
  return redirect('detail', gem_id=gem_id)

class ReviewUpdate(UpdateView):
  model = Review
  fields = ['content', 'rating']

class ReviewDelete(DeleteView):
  model = Review
  success_url = '/gems/'




####### Need to need to add to class base views
## refer to cat collector
# class CatCreate(LoginRequiredMixin, CreateView):


####### Need to need to add to see users added hidden gems
# gems = Gem.objects.filter(user=request.user)

####### Need to need to add to the create function
  # def form_valid(self, form):
  #   # Assign the logged in user (self.request.user)
  #   form.instance.user = self.request.user  # form.instance is the cat
  #   # Let the CreateView do its job as usual
  #   return super().form_valid(form)

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