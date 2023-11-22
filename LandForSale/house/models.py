# house/models.py

from django.db import models

class House(models.Model):
    location = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    photos = models.ImageField(upload_to='house_photos/',default='default.jpg' )
    map_location = models.CharField(max_length=255,default='' )
    created_at = models.DateTimeField(default=None )

    def __str__(self):
        return self.location

