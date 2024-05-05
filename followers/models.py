from django.conf import settings
from django.db import models


class Follower(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscribers")
    subscribed_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions")

    class Meta:
        unique_together = ("subscriber", "subscribed_to")


    def __str__(self):
        return f"{self.subscriber} subscribed to {self.subscribed_to}"
