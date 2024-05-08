from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.URLField(null=True, blank=True)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    genre = models.CharField(max_length=200)
    video_url = models.URLField()


    def __str__(self) -> str:
        return self.title
