# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
import requests as rq
from rest_framework import status

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

        self.whattsap_apk_url='https://www.cdn.whatsapp.net/android/2.18.72/WhatsApp.apk'

    def test_upload_application(self):
        post_url = reverse('application_list')
        file_path = self._download_save_test_application(self.whattsap_apk_url)
        data = open(file_path, 'rb')
        response = self.client.post(post_url, {'file': data}, format='multipart')
        os.remove(file_path)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def _download_save_test_application(self, url):
        file_name = url[url.rfind("/")+1:]
        file_path = '/tmp/'+file_name
        r = rq.get(url, stream=True)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                   f.write(chunk)
        return file_path

