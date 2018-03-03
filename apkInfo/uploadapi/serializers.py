from rest_framework import serializers
from uploadapi.models import Application


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'application', 'package_name', 'package_version_code')
