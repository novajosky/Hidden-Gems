from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('maps/', views.maps, name='maps'),
  path('gems/', views.gems_index, name='index'),
]