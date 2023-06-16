from django.forms import ModelForm
from music_upload.models import Music


class MusicUploadForm(ModelForm):
    class Meta:
        model = Music
        fields = ("song_name", "artist", "audio_file", "upload_type", "allowed_users", )