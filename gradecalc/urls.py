from django.conf.urls import patterns, url
from gradecalc import views

urlpatterns = patterns('',
    url(r'^gradecalc/', views.GradeCalcView.as_view(), name="gradecalc"),
    url(r'^viewgrades/', views.ViewGrades.as_view(), name="viewgrades"),
    url(r'^viewclass/(?P<pk>\d+)/$', views.ViewClass.as_view(), name="viewclass"),
    url(r'^$', views.GradeView.as_view(), name="grade"),
)