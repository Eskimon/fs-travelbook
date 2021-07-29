import json
import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    embed_id = models.CharField(max_length=36)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="flights")
    name = models.CharField(max_length=100, null=False, blank=False)
    data_file = models.FileField(upload_to="uploads/flights/")
    description = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(default=timezone.now)
    departure = models.ForeignKey("Airport", on_delete=models.SET_NULL, related_name="departures", null=True)
    arrival = models.ForeignKey("Airport", on_delete=models.SET_NULL, related_name="arrivals", null=True)
    start = models.DateTimeField(null=True)
    takeoff = models.DateTimeField(null=True)
    landing = models.DateTimeField(null=True)

    class Meta:
        ordering = ["name"]
        constraints = [models.UniqueConstraint(fields=["owner", "embed_id"], name="unique flight_owner")]

    def get_absolute_url(self):
        return reverse("flights:detail", args=[self.id])

    def save(self, reparse=False, *args, **kwargs):
        if reparse:
            # Delete all waypoint if any
            self.waypoints.all().delete()
            # Parse the data file
            with self.data_file.open() as f:
                data = json.load(f)
                test = Flight.objects.filter(embed_id=data["Flight"]["Id"])
                if test.exists():
                    return test.first()
                self.embed_id = data["Flight"]["Id"]
                # Some general data about the flight
                self.start = data["Flight"]["StartTime"]
                self.takeoff = data["Flight"]["AirborneTime"]
                self.landing = data["Flight"]["LandedTime"]
                # Try to get/create the depart/arrival airport
                self.departure = Airport.objects.get_or_create(
                    onair_id=data["Flight"]["DepartureAirportId"],
                    defaults={
                        "onair_id": data["Flight"]["DepartureAirport"]["Id"],
                        "ICAO": data["Flight"]["DepartureAirport"]["ICAO"],
                        "IATA": data["Flight"]["DepartureAirport"]["IATA"],
                        "name": data["Flight"]["DepartureAirport"]["Name"],
                        "state": data["Flight"]["DepartureAirport"]["State"],
                        "country_code": data["Flight"]["DepartureAirport"]["CountryCode"],
                        "country_name": data["Flight"]["DepartureAirport"]["CountryName"],
                        "city": data["Flight"]["DepartureAirport"]["City"],
                        "display_name": data["Flight"]["DepartureAirport"]["DisplayName"],
                        "lat": data["Flight"]["DepartureAirport"]["Latitude"],
                        "lon": data["Flight"]["DepartureAirport"]["Longitude"],
                        "alt": data["Flight"]["DepartureAirport"]["Elevation"],
                    },
                )[0]
                self.arrival = Airport.objects.get_or_create(
                    onair_id=data["Flight"]["ArrivalActualAirportId"],
                    defaults={
                        "onair_id": data["Flight"]["ArrivalActualAirport"]["Id"],
                        "ICAO": data["Flight"]["ArrivalActualAirport"]["ICAO"],
                        "IATA": data["Flight"]["ArrivalActualAirport"]["IATA"],
                        "name": data["Flight"]["ArrivalActualAirport"]["Name"],
                        "state": data["Flight"]["ArrivalActualAirport"]["State"],
                        "country_code": data["Flight"]["ArrivalActualAirport"]["CountryCode"],
                        "country_name": data["Flight"]["ArrivalActualAirport"]["CountryName"],
                        "city": data["Flight"]["ArrivalActualAirport"]["City"],
                        "display_name": data["Flight"]["ArrivalActualAirport"]["DisplayName"],
                        "lat": data["Flight"]["ArrivalActualAirport"]["Latitude"],
                        "lon": data["Flight"]["ArrivalActualAirport"]["Longitude"],
                        "alt": data["Flight"]["ArrivalActualAirport"]["Elevation"],
                    },
                )[0]
                super(Flight, self).save(*args, **kwargs)
                # Add all the waypoints
                for idx, wp in enumerate(data["StatPoints"]):
                    Waypoint(
                        flight=self,
                        index=idx,
                        lat=wp["Aircraft"]["Latitude"],
                        lon=wp["Aircraft"]["Longitude"],
                        alt=wp["Aircraft"]["Altitude"],
                    ).save()
                # super(Flight, self).save(*args, **kwargs)
                return self
        else:
            super(Flight, self).save(*args, **kwargs)
            return self


class Waypoint(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="waypoints")
    index = models.PositiveIntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    alt = models.DecimalField(max_digits=7, decimal_places=2)
    # Storing speed and whatnot?
    # speed = Positive Integer
    # compas = Positive Integer
    # Drawing a virtual horizon somewhere?
    # Pitch ? = Integer
    # Bank ? = Integer

    class Meta:
        ordering = ["flight", "index"]


class Airport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    onair_id = models.CharField(max_length=36, unique=True, null=True, blank=True)
    ICAO = models.CharField(max_length=4)  # Validator only capital letter
    IATA = models.CharField(max_length=3)  # Validator only capital letter
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    alt = models.DecimalField(max_digits=6, decimal_places=2)
