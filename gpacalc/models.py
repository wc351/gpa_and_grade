from django.contrib.auth.models import User
from django.db import models
from django import forms


class GPA(models.Model):
    user = models.CharField(max_length=25)
    class_name = models.CharField(max_length=100)
    credit_hours = models.FloatField(max_length=2)
    grade = models.CharField(max_length=3)

    def __unicode__(self):
        return self.user
