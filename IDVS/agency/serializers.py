from rest_framework.serializers import ModelSerializer
from .models import *




class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'