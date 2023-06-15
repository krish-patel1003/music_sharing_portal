from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('music_upload/', views.music_upload, name='music_upload'),
    path('music_list/', views.music_list, name='music_list'),
]