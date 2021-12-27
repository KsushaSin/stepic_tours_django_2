from django.db import models
from django.db.models import Model


class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    length = models.FloatField()
    lat = models.FloatField(null=True)
    lon = models.FloatField()
    class Meta:
        app_label = 'tours'

    def __str__(self):
        return f'{self.pk} {self.code} {self.name} {self.length}'
