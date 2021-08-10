import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class MyUser(models.Model):

    ICONS_CHOICES = (
        (0, "None"),
        (1, "Icons"),
        (2, "Circle"),
    )

    MAP_CHOICES = (
        (0, "OSM"),
        (1, "Topo"),
        (2, "Sat"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    icons = models.PositiveIntegerField(default=1, choices=ICONS_CHOICES)
    maps = models.PositiveIntegerField(default=0, choices=ICONS_CHOICES)

    def get_absolute_url(self):
        return reverse("myuser:update", args=[self.id])


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.get_or_create(user=instance)
