from django.urls import path
from music_upload.views import MusicUploadView, MusicListView, MusicDetailView

urlpatterns = [
    path("upload/", MusicUploadView.as_view(), name="music_upload"),
    path("list/", MusicListView.as_view(), name="music_list"),
    path("detail/<int:pk>/", MusicDetailView.as_view(), name="music_detail"),
]