from django.urls import path, include
from rest_framework import routers

from .views import FileTypeViewSet

router = routers.DefaultRouter()

router.register(r'', FileTypeViewSet)

urlpatterns = [
  path(r'', include(router.urls))
]
