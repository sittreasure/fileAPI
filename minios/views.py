from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .minioClient import minioClient
from .serializers import MinioMetadataSerializer, MinioDataSerializer

bucketName = 'mockjsp'

class MinioFileView(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()

  def get(self, request):
    result = None
    objectName = request.GET.get('object_name', '')
    if len(objectName) != 0:
      data = self.__minioClient.get(bucketName, objectName)
      data = {
        'data': data
      }
      result = MinioDataSerializer(data, many=False).data
      pass
    else:
      prefixName = request.GET.get('prefix_name')
      listObjects = self.__minioClient.listFiles(bucketName, prefixName)
      listNewObjects = list(map(
        lambda object:
          {
            'name': object.object_name,
            'isDir': object.is_dir
          },
        listObjects
      ))
      result = MinioMetadataSerializer(listNewObjects, many=True).data
      pass
    return Response(result)