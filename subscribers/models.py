from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    subscribed_at = models.DateTimeField(
        default=timezone.now, verbose_name="Subscribed At"
    )
    email = models.EmailField(max_length=150, unique=True
    )

    def __str__(self):
        return self.email
