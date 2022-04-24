from rest_framework import serializers

from file_storage.models import StoredFile


class StoredFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoredFile
        fields = ('file', )