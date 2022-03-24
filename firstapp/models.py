from django.db import models


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
