from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .minioClient import minioClient
from .serializers import MinioMetadataSerializer

class MinioFileSet(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()

  def get(self, request):
    prefixName = request.GET.get('prefix_name')
    bucketName = getattr(settings, 'MINIO_BUCKET_NAME')
    listObjects = self.__minioClient.listFiles(bucketName, prefixName)
    listNewObjects = list(map(
      lambda object:
        {
          'object_name': object.object_name,
          'is_dir': object.is_dir
        },
      listObjects
    ))
    result = MinioMetadataSerializer(listNewObjects, many=True).data
    return Response(result)