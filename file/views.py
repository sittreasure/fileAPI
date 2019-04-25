from rest_framework import viewsets

from .models import FileType
from .serializers import FileTypeSerializer

class FileTypeViewSet(viewsets.ModelViewSet):
  queryset = FileType.objects.all()
  serializer_class = FileTypeSerializer
