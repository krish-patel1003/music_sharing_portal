from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import User
# Create your models here.


class Music(models.Model):
    '''
        Music upload Model
    '''
    PRIVATE = "PRI"
    PUBLIC = "PUB"
    PROTECTED = "PRO"

    UPLOAD_TYPE_CHOICES = [
        (PRIVATE, "Private"),
        (PUBLIC, "Public"),
        (PROTECTED, "Protected"),
    ]

    song_name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(
        upload_to='music/', null=False, blank=False, validators=[FileExtensionValidator( ['mp3'] ) ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music')
    upload_type = models.CharField(
        max_length=3,
        choices=UPLOAD_TYPE_CHOICES,
        default=PUBLIC,
    )
    uploaded_on = models.DateTimeField(auto_now_add=True)
    allowed_users = models.ManyToManyField(User, related_name='allowed_users', null=True, blank=True)


    def __str__(self):
        return self.song_name