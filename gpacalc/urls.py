from django.conf.urls import patterns, url
from gpacalc import views

urlpatterns = patterns('',
    url(r'^addclasses/', views.ClassView.as_view(), name="addclasses"),
    url(r'^allclasses/', views.AllClasses.as_view(), name="allclasses"),
    url(r'^$', views.GpaView.as_view()),

)


