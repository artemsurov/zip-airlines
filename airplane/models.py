from django.db import models


class AirPlane(models.Model):
    passenger_capacity = models.PositiveSmallIntegerField()
