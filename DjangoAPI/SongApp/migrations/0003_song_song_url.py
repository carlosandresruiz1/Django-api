# Generated by Django 5.1 on 2024-09-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SongApp', '0002_artistrolsong_rol_delete_artistrol_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.CharField(default='hola', max_length=200),
            preserve_default=False,
        ),
    ]
