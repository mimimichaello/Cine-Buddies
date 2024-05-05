from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """
    Модель пользовательского Профиля
    """

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')

    def __str__(self) -> str:
        return self.username
