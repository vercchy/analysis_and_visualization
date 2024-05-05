from rest_framework import serializers
from .models import UploadedTable


class UploadedTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedTable
        fields = '__all__'


class CreateUploadedTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedTable
        fields = ['title', 'uploaded_at']
