from django.conf import settings
from minio import Minio

class minioClient:
  __minio = None

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    minioUrl = getattr(settings, 'MINIO_URL')
    minioAccessKey = getattr(settings, 'MINIO_ACCESS_KEY')
    minioSecretKey = getattr(settings, 'MINIO_SECRET_KEY')
    self.__minio = Minio(
      minioUrl,
      access_key=minioAccessKey,
      secret_key=minioSecretKey,
      secure=True
    )

  def listFiles(self, bucketName, prefixName):
    listObjects = self.__minio.list_objects(bucketName, prefix=prefixName)
    return listObjects