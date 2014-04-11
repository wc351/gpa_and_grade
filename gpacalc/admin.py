
from django.contrib.gis import admin
from models import GPA

admin.site.register(GPA, admin.GeoModelAdmin)