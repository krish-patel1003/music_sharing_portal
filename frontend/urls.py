from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('music_upload/', views.music_upload, name='music_upload'),
    path('music_list/', views.music_list, name='music_list'),
    path('music_update/<int:id>/', views.music_update, name='music_detail'),
]