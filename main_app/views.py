from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Gem

# Define the home view
def home(request):
    return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

@login_required
def maps(request):
  return render(request, 'maps.html')

def gems_index(request):
  return render(request, 'gems/index.html')

def gems_detail(request, gem_id):
  gem = Gem.objects.get(id = gem_id)
  return render (request, 'gems/detail.html', {
    'gem': gem,
  })

class GemCreate(CreateView):
  model = Gem
  fields = ['name', 'location', 'coordinates', 'description',  'picture', 'category']
  success_url = '/gems/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GemUpdate(UpdateView):
  pass
class GemDelete(DeleteView):
  pass




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