
from django.contrib.gis import admin
from models import Grade

admin.site.register(Grade, admin.GeoModelAdmin)