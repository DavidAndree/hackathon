from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    """Custom user model that extends the default Django user model."""

    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse("user_detail", kwargs={"pk": self.pk})


class Skill(models.Model):
    name = models.CharField(max_length=100)
