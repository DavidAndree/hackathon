from django.db import models

class Subscription(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField()