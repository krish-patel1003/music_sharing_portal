# Generated by Django 4.2.2 on 2023-06-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='audio_file',
            field=models.FileField(upload_to='music/'),
        ),
    ]
