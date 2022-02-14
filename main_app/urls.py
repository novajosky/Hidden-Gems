from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('maps/', views.maps, name='maps'),
  path('gems/', views.gems_index, name='index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('gems/<int:gem_id>/', views.gems_detail, name='detail'),
  path('gems/create/', views.GemCreate.as_view(), name='gems_create'),
  path('gems/<int:pk>/update/', views.GemUpdate.as_view(), name='gems_update'),
  path('gems/<int:pk>/delete/', views.GemDelete.as_view(), name='gems_delete'),
]