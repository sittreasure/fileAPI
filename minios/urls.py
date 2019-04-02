from django.urls import path

from .views import MinioFileView

app_name = 'minio'

urlpatterns = [
  path(r'file', MinioFileView.as_view())
]