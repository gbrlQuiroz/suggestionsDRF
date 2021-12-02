from rest_framework import serializers
from suggestions.models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
