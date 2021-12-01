from django.db import models


class City(models.Model):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)

    class Meta:
        db_table = 'cities'
        ordering = ['id']
