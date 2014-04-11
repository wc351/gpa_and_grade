"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from gpa_and_grade import gradecalc


class SimpleTest(TestCase):
    """ gradecalc model tests"""

    def test_unicode(self):

        grade = gradecalc(question="What color is the sky?",
                              pub_date=datetime.now())

        self.assertEquals(str(grade),
                          "What color is the sky?")
