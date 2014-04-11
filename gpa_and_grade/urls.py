from django.conf.urls import patterns, url, include
from django.contrib import admin
from gpacalc.views import MainView
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gpa/', include('gpacalc.urls',namespace='gpa')),
    url(r'^grade/', include('gradecalc.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/', include('user_profile.urls', namespace='profile')),
    # url(r'^results/', Results.as_view(), name="results"),
    url(r'^$', MainView.as_view(), name="main_page"),
)