from django.shortcuts import render
from frontend.forms import MusicUploadForm
from music_upload.models import Music

# Create your views here.


def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def music_upload(request):
    form = MusicUploadForm()
    return render(request, 'music_upload/music_upload.html', {"form": form})

def music_list(request):
    return render(request, 'music_upload/music_list.html')

def music_update(request, id):
    music = Music.objects.get(id=id)
    form = MusicUploadForm(request.POST or None, request.FILES or None, instance=music)
    return render(request, 'music_upload/music_update.html', {"form": form, "music": music})