import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from flights.models import Flight


class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pictures")
    name = models.CharField(max_length=100, null=False, blank=False)
    data_file = models.ImageField(upload_to="uploads/pictures/")
    description = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(default=timezone.now)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, related_name="pictures", null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("pictures:detail", args=[self.id])
