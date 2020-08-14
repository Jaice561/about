from django.shortcuts import render
from .models import Photo, Video
# from .models import Photo


# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def photo(request):
    pics = Photo.objects.all()    
    return render(request, 'photo.html', {'pics':pics})

def video(request):
    videos = Video.objects.all()    
    return render(request, 'video.html', {'videos':videos})
