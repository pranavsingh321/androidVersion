# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Application

# Create your tests here.
class ApplicationTestcase(TestCase):
    """setup for ApplicationTestcase"""
    def setUp(self):
        self.application = '/media/test.apk'
        self.package_name = 'android'
        self.package_version_code = '4201'
        self.application_object = Application(application=self.application,
        	package_name=self.package_name, package_version_code=self.package_version_code)  
    
    def test_model_create_application(self):
        prev_count = Application.objects.count()
        self.application_object.save()
        new_count = Application.objects.count()
        self.assertEqual(prev_count+1, new_count)

class ViewAllApplications(TestCase):
	"""view  for all ViewAllApplications"""
    def setUp():
    	self.client = APIClient()
    	self.
		