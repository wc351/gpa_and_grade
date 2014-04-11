from django.conf.urls import patterns, url
from user_profile import views
from djgeojson.views import GeoJSONLayerView
from user_profile.models import User_Profile

urlpatterns = patterns('',

    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=User_Profile, geometry_field='geom', simplify=True), name='data'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^$', views.CreateUserView.as_view(), name="profile"),
)


