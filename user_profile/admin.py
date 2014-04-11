
from django.contrib.gis import admin
from models import User_Profile

admin.site.register(User_Profile, admin.GeoModelAdmin)