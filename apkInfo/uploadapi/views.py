# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from django.core.files.storage import FileSystemStorage
from uploadapi.serializers import UploadSerializer
from uploadapi.models import Application
from lib import utilities as ut

# Create your views here.

class CreateViewApplications(APIView):
    """Class Based View"""
    """This class handles the http GET, PUT and DELETE requests."""
    parser_classes = (FileUploadParser,)
    queryset = Application.objects.all()
    serializer_class = UploadSerializer


    def post(self, request, serializer, format=None):
        '''Handle upload of apk files'''
        import pdb;pdb.set_trace()

        uploaded_file = request.FILES['file']
        uploaded_file_name = '{}'.format(uploaded_file.name)
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file_name, uploaded_file)
        uploaded_file_url = fs.url(filename)

        apk_info = ut.get_apk_data(destination_path)
        serializer.save(application=self.uploaded_file_url, package_name=apk_info['package_name'], package_version_code=['package_version'])
            

class DetailsViewApplication(generics.RetrieveUpdateDestroyAPIView):
    """Class Based View"""
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Application.objects.all()
    serializer_class = UploadSerializer