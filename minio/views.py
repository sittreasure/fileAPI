from rest_framework.views import APIView
from rest_framework.response import Response

from .minioClient import minioClient

class MinioFileSet(APIView):
  __minioClient = None

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.__minioClient = minioClient()