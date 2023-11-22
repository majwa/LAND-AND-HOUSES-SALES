# land/models.py

# plot/models.py

# land/models.py

from django.db import models

class Land(models.Model):
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    photos = models.ImageField(upload_to='land_photos/',default='default.jpg' )
    map_location = models.CharField(max_length=255,default='' )
    created_at = models.DateTimeField(default=None )

    def __str__(self):
        return self.location
