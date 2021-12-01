from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, BooleanFilter, NumberFilter

from .serializers import *


class SuggestionsFilter(FilterSet):
    q = CharFilter(field_name='name', lookup_expr='icontains')
    latitude = CharFilter(field_name='latitude', lookup_expr='icontains')
    longitude = CharFilter(field_name='longitude', lookup_expr='icontains')

    class Meta:
        model = City
        fields = ['q', 'latitude', 'longitude']


class SuggestionsFilteredListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = SuggestionsFilteredListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SuggestionsFilter
