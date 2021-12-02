
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from api.exceptions import *


class SuggestionsEndPoint(APIView):
    def getQuerySet(self, q):
        datos = City.objects.filter(name__icontains=q).order_by('-name')
        if datos.count() > 0:
            return datos
        raise ResponseError(f'No se encontró registro con valor: {q}', 404)

    def get(self, request, *args, **kwargs):
        q = self.request.query_params.get('q', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        queryset = self.getQuerySet(q)
        serializer = SuggestionsSerializer(queryset, many=True, context={'lat': latitude, 'lon': longitude})

        return Response({'suggestions': serializer.data})
