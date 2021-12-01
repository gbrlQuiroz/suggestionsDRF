from rest_framework import serializers
from .models import *


class SuggestionsFilteredListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     # repr['suggestions'] = instance

    #     # return {'suggestions' : repr}
    #     return repr
