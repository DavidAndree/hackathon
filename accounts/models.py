from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    '''Custom user model that extends the default Django user model.'''
    age = models.PositiveIntegerField(null=True, blank=True)
    