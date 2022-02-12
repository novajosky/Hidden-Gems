from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def maps(request):
  return render(request, 'maps.html')

def gems_index(request):
  return render(request, 'gems/index.html')