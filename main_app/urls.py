from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('maps/', views.maps, name='maps'),
  path('gems/', views.gems_index, name='index'),
  path('accounts/signup/', views.signup, name='signup'),
  path('gems/<int:gem_id>/', views.gems_detail, name='detail'),
  path('gems/create/', views.GemCreate.as_view(), name='gems_create'),
  path('gems/<int:pk>/update/', views.GemUpdate.as_view(), name='gems_update'),
  path('gems/<int:pk>/delete/', views.GemDelete.as_view(), name='gems_delete'),
  path('gems/<int:gem_id>/add_photo/', views.add_photo, name='add_photo'),
  path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
  path('gems/<int:gem_id>/add_review/', views.add_review, name='add_review'),
  path('review/<int:pk>/delete/', views.ReviewDelete.as_view(), name='delete_review'),
]