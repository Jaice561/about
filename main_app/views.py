from django.shortcuts import render
from .models import Photo


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

def image(request):
    image_file = request.FILES['image_file'].file.read()
    Photo.objects.create(image=image_file)
