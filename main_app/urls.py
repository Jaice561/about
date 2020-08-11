from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('video/', views.video, name='video'),
    path('photo/', views.photo, name='photo'),
]