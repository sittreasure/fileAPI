import json
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .minioClient import minioClient
from .serializers import MinioMetadataSerializer, MinioDataSerializer, MinioResultSerializer
from base.jwt import getUserId

coreBucket = 'core'

class MinioBucketView(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()

  def post(self, request):
    userId = getUserId(request)
    userId = str(userId)
    existBucket = self.__minioClient.existBucket(userId)
    data = None
    if existBucket:
      data = {
        'result': existBucket
      }
    else:
      createBucket = self.__minioClient.createBucket(userId)
      data = {
        'result': createBucket
      }
    result = MinioResultSerializer(data, many=False).data
    return Response(result)

class MinioFolderView(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()

  def get(self, request):
    userId = getUserId(request)
    userId = str(userId)
    folderName = request.GET.get('folder_name', '')
    listFiles = self.__minioClient.listFiles(coreBucket, folderName, True)
    success = False
    for fileName in listFiles:
      objectName = fileName.object_name
      success = self.__minioClient.copyFile(coreBucket, objectName, userId, objectName)
      if not success:
        break
    data = {
      'result': success
    }
    result = MinioResultSerializer(data, many=False).data
    return Response(result)

class MinioFileView(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()

  def get(self, request):
    userId = getUserId(request)
    bucketName = str(userId)
    result = None
    objectName = request.GET.get('object_name', '')
    if len(objectName) != 0:
      data = self.__minioClient.getFile(bucketName, objectName)
      data = {
        'data': data
      }
      result = MinioDataSerializer(data, many=False).data
    else:
      existBucket = self.__minioClient.existBucket(bucketName)
      if not existBucket:
        createBucket = self.__minioClient.createBucket(bucketName)
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
    return Response(result)

  def post(self, request):
    userId = getUserId(request)
    bucketName = str(userId)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    objectData = body['objectData']
    name = body['name']
    objectName = name.split('/')
    objectSource = './temp/{name}'.format(name = objectName[len(objectName) - 1])
    file = open(objectSource, "w")
    file.write(objectData)
    file.close()
    result = self.__minioClient.putFile(bucketName, name, objectSource)
    os.remove(objectSource)
    data = {
      'result': result
    }
    result = MinioResultSerializer(data, many=False).data
    return Response(result)

  def delete(self, request):
    userId = getUserId(request)
    bucketName = str(userId)
    objectName = request.GET.get('object_name', '')
    result = self.__minioClient.removeFile(bucketName, objectName)
    data = {
      'result': result
    }
    result = MinioResultSerializer(data, many=False).data
    return Response(result)
