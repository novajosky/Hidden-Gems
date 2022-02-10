from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

class Gem:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

gems = {
    Gem('The Ape Cave', 'Skamania, Washington', 'An awesome cave!'),
    Gem('Sunnyside Beach', 'Steilacoom, Washington', 'At night, you can see all the stars!')
}

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def gems_index(request):
  return render(request, 'gems/index.html', { 'gems': gems })