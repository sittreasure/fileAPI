from django.urls import path

from .views import MinioFileView, MinioBucketView

app_name = 'minio'

urlpatterns = [
  path(r'bucket/', MinioBucketView.as_view()),
  path(r'file/', MinioFileView.as_view())
]