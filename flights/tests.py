import os

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Airport, Flight


class FlightViewsTests(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username="johndoe")[0])
        Airport.objects.create(
            id="8dd03407-f20c-49aa-bbc2-0d9dc760f4b1",
            ICAO="LFRQ",
            IATA="UIP",
            name="Pluguffan",
            state="Brittany",
            country_code="LF",
            country_name="France",
            city="Quimper/Pluguffan",
            lat=47.973415,
            lon=-4.170914,
            alt=293.0,
            display_name="LFRQ (Pluguffan)",
        )

    def test_nominal_upload_case(self):
        data = b""
        with open("fixtures/onair/0b786dbf-68ad-48a7-a7c6-a652a533872b.dat", "rb") as f:
            data = f.read()
        dat_file = SimpleUploadedFile(
            "fixtures/0b786dbf-68ad-48a7-a7c6-a652a533872b.dat",
            data,
            content_type="text/plain",
        )
        self.client.post(
            reverse("flights:create"),
            {
                "name": "Test flight",
                "description": "My first flight",
                "data_file": dat_file,
            },
        )
        # The flight should have the proper id
        flight = Flight.objects.get(embed_id="0b786dbf-68ad-48a7-a7c6-a652a533872b")
        self.assertIsNotNone(flight)
        self.assertEquals(flight.name, "Test flight")
        self.assertEquals(flight.description, "My first flight")
        self.assertEquals(flight.waypoints.count(), 258)
        self.assertEquals(Airport.objects.count(), 3)

    def test_all_fixtures(self):
        files = os.listdir("fixtures/onair")
        for idx, f in enumerate(files):
            with open("fixtures/onair/{}".format(f), "rb") as flight:
                print("fixtures/onair/{}".format(f))
                data = flight.read()
                dat_file = SimpleUploadedFile(
                    "fixtures/onair/{}".format(f),
                    data,
                    content_type="text/plain",
                )
                self.client.post(
                    reverse("flights:create"),
                    {
                        "name": "Test flight {}".format(idx),
                        "description": "My flight",
                        "data_file": dat_file,
                    },
                )
        self.assertEquals(len(Flight.objects.all()), len(files))
