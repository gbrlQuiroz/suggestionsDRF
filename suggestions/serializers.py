from rest_framework import serializers
from .models import *

from haversine import haversine


class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        lat = self.context.get('lat')
        lon = self.context.get('lon')
        if lat is None or lon is None:
            repr['score'] = 1.0
            return repr
        else:
            lat = float(lat)
            lon = float(lon)
            valor = haversine((lat, lon), (instance.latitude, instance.longitude))
            if int(valor) < 100:
                repr['score'] = 1.0
                return repr
            if int(valor) > 100 and int(valor) < 200:
                repr['score'] = 0.9
                return repr
            if int(valor) > 200 and int(valor) < 300:
                repr['score'] = 0.8
                return repr
            if int(valor) > 300 and int(valor) < 400:
                repr['score'] = 0.7
                return repr
            if int(valor) > 400 and int(valor) < 500:
                repr['score'] = 0.6
                return repr
            if int(valor) > 500 and int(valor) < 600:
                repr['score'] = 0.5
                return repr
            if int(valor) > 600 and int(valor) < 700:
                repr['score'] = 0.4
                return repr
            if int(valor) > 700 and int(valor) < 800:
                repr['score'] = 0.3
                return repr
            if int(valor) > 800 and int(valor) < 900:
                repr['score'] = 0.2
                return repr
            if int(valor) > 900:
                repr['score'] = 0.1
                return repr
