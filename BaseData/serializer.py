from rest_framework import serializers
from .models import *

class baseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseDataAPI
        fields = '__all__'