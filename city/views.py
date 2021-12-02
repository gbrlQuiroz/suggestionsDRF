from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import *
from api.exceptions import *


class CityCreateView(CreateAPIView):
    serializer_class = CitySerializer

    def post(self, request, *args, **kwargs):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get('name')
            if City.objects.filter(name=name).count() > 0:
                raise ResponseError(f'Ya existe un registro con este nombre: {name}', 409)
            return self.create(request, *args, **kwargs)
        raise CamposIncorrectos(serializer.errors)
