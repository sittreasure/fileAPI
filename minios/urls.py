from django.urls import path

from .views import MinioFileSet

app_name = 'minio'

urlpatterns = [
  path(r'/file', MinioFileSet.as_view())
]