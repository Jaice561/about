from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def video(request):
  return render(request, 'video.html')

def photo(request):
  return render(request, 'photo.html')
