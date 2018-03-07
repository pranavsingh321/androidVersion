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
    	self._create_test_file('/tmp/test_upload.apk')
    	tmp_file = tempfile.NamedTemporaryFile(suffix='.apk')
	    response = self.client.post('my_url', {'image': tmp_file}, format='multipart')

	def _create_test_file(self, path):
        f = open(path, 'w')
        f.write('test123\n')
        f.close()
        f = open(path, 'rb')
        return {'datafile': f}
    def _download_test_application(self, url):
    	