from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def music_upload(request):
    return render(request, 'music_upload/music_upload.html')

def music_list(request):
    return render(request, 'music_upload/music_list.html')