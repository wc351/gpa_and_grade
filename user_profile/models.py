from django.contrib.gis.db import models


class User_Profile(models.Model):
    username = models.CharField(max_length=50)
    year_level = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    school = models.CharField(max_length=75)
    geom = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.username