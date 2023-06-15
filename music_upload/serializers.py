from rest_framework import serializers
from music_upload.models import Music


class MusicUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = (
            "id", "song_name", "artist", "audio_file", "upload_type", "allowed_users", "uploaded_on", "user")
        read_only_fields = ("id", "uploaded_on", "user")
        