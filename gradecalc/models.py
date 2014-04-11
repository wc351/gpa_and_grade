from django.contrib.auth.models import User
from django.db import models
#
#
# class Category(models.Model):
#     user = models.CharField(max_length=50)
#     class_name = models.CharField(max_length=50)
#     subject = models.CharField(max_length=100)
#     percentage = models.FloatField(max_length=4)
#     point_total = models.FloatField(max_length=4)
#     point_possible = models.FloatField(max_length=4)
#     final_grade = models.FloatField(max_length=4)
#
#     def __unicode__(self):
#         return self.user


class Grade(models.Model):
    user = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    homework_percent = models.FloatField(max_length=3)
    homework_total = models.IntegerField(max_length=3)
    homework_possible = models.IntegerField(max_length=3)
    tests_percent = models.FloatField(max_length=3)
    tests_total = models.IntegerField(max_length=3)
    tests_possible = models.IntegerField(max_length=3)
    final_percent = models.FloatField(max_length=3)
    final_total = models.IntegerField(max_length=3)
    final_possible = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.user