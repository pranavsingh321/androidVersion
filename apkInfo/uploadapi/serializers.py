from rest_framework import serializers
from uploadapi.models import Application


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
    	fields = '__all__'
        model = Application
        read_only_fields = ('id', 'application', 'package_name', 'package_version_code')
