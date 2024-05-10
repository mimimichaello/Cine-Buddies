from django.db import models
from django.conf import settings

from films.models import Film



class Room(models.Model):
    name = models.CharField(max_length=100)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_rooms')
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribed_rooms')
    voice_enabled = models.BooleanField(default=True)
    playback_time = models.FloatField(default=0.0)
    live_video_url = models.URLField(blank=True, null=True)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def create_room(cls, name, film, owner, subscriber, voice_enabled=True):
        room = cls(name=name, film=film, owner=owner, subscriber=subscriber, voice_enabled=voice_enabled)
        room.save()
        return room


