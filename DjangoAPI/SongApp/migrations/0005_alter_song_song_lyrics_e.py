# Generated by Django 5.1 on 2024-09-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SongApp', '0004_song_song_lyrics_e'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_lyrics_e',
            field=models.CharField(max_length=500),
        ),
    ]
