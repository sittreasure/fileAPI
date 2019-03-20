from rest_framework import serializers

class MinioMetadataSerializer(serializers.Serializer):
  object_name = serializers.CharField()
  is_dir = serializers.BooleanField()