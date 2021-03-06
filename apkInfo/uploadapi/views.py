# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError, ValidationError 
from rest_framework.parsers import MultiPartParser, FormParser
from uploadapi.serializers import UploadSerializer
from uploadapi.models import Application

from lib import utilities as ut

class AAPTError(APIException):
    status_code = 503
    default_message = 'AAPT Error. Please check for AAPT application.'

class CreateViewApplications(generics.ListCreateAPIView):
    """Class Based View"""
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Application.objects.all()
    parser_classes = (MultiPartParser, FormParser, )
    serializer_class = UploadSerializer

    def perform_create(self, serializer, format=None):
        '''Handle upload of apk files'''
        if self.request.FILES:
            uploaded_file_url, local_path = ut.store_file_locally(self.request)
            try:
                apk_info = ut.get_apk_data(ut.execute_ext_command(local_path))
            except OSError as e:
                raise AAPTError()
            if serializer.is_valid():
                serializer.save(application=uploaded_file_url,
                                package_name=apk_info['name'], package_version_code=apk_info['versionCode'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ParseError('File content not found')


class DetailsViewApplication(generics.RetrieveUpdateDestroyAPIView):
    """Class Based View"""
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Application.objects.all()
    serializer_class = UploadSerializer
