from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    """Custom user model that extends the default Django user model."""

    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_mentor = models.BooleanField(default=False)  # True if the user is a mentor, False if not
    is_mentee = models.BooleanField(default=True)  # True if the user is a mentee, False if not
    skills = models.ManyToManyField('Skill', blank=True, related_name="users")  # Many-to-many relationship with the Skill model

    def __str__(self):
        return self.email

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
=======
    # def get_absolute_url(self):
    #     return reverse("user_detail", kwargs={"pk": self.pk})
>>>>>>> be24a7ba44bfb11e81ee67bec5a9810ae4b33357


class Skill(models.Model):
    name = models.CharField(max_length=100)

