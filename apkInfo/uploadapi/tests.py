# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
import requests as rq

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
    def setUp(self):
        self.client = APIClient()

        whattsap_apk_url='https://www.cdn.whatsapp.net/android/2.18.72/WhatsApp.apk'
        file_path=self._download_save_test_application(whattsap_apk_url)

    def test_upload_application(self):
        post_url = reverse('uploadapi:api/applications')
        data = self._download_save_test_application(self.whattsap_apk_url)
        response = client.post(post_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('created', response.data)

    def _download_save_test_application(self, url):
        file_name = url[url.rfind("/")+1:]
        ro = rq.get(url, stream=True)        
        return {'file': ro}