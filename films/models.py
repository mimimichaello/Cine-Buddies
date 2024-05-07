from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_img_url = models.URLField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    genre = models.CharField(max_length=200)
    external_id = models.CharField(max_length=50, unique=True)


    def __str__(self) -> str:
        return self.title
