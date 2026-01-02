from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add profile picture (optional)
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)

    # Follow system: users this user is following
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True
    )

    def __str__(self):
        return self.username
