from rest_framework import serializers

class MinioMetadataSerializer(serializers.Serializer):
  name = serializers.CharField()
  isDir = serializers.BooleanField()

class MinioDataSerializer(serializers.Serializer):
  data = serializers.CharField()