from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from file_storage.models import StoredFile
from file_storage.serializers import StoredFileSerializer


class StoredFileViewSet(
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    serializer_class = StoredFileSerializer
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser, MultiPartParser)

    def get_queryset(self):
        return StoredFile.objects.all()
