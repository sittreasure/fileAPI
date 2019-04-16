from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os

from .minioClient import minioClient
from .serializers import MinioMetadataSerializer, MinioDataSerializer, MinioResultSerializer

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
      data = self.__minioClient.getFile(bucketName, objectName)
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

  def post(self, request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    objectData = body['objectData']
    name = body['name']
    objectName = name.split('/')
    sourceObject = './temp/{name}'.format(name = objectName[len(objectName) - 1])
    file = open(sourceObject, "w")
    file.write(objectData)
    file.close()
    result = self.__minioClient.putFile(bucketName, name, sourceObject)
    os.remove(sourceObject)
    data = {
      'result': result
    }
    result = MinioResultSerializer(data, many=False).data
    return Response(result)
