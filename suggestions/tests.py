# from django.test import TestCase
from rest_framework.test import APITestCase
import json
from rest_framework import status

from .models import *


def configDB():
    City.objects.create(name='Amherst', latitude=45.83345, longitude=-64.19874)
    City.objects.create(name='Amherstburg', latitude=42.11679, longitude=-83.04985)
    City.objects.create(name='Amos', latitude=48.56688, longitude=-78.11624)
    City.objects.create(name='Amityville', latitude=40.67899, longitude=-73.41707)
    City.objects.create(name='Amsterdam', latitude=42.93869, longitude=-74.18819)
    City.objects.create(name='Amesbury', latitude=42.85842, longitude=-70.93005)
    City.objects.create(name='Amherst Center', latitude=42.37537, longitude=-72.51925)
    City.objects.create(name='Ambler', latitude=40.15455, longitude=-75.22157)
    City.objects.create(name='Amqui', latitude=48.46382, longitude=-67.43134)
    City.objects.create(name='Beaumont', latitude=53.35013, longitude=-113.41871)
    City.objects.create(name='Belleville', latitude=44.16682, longitude=-77.38277)
    City.objects.create(name='Beloeil', latitude=45.56678, longitude=-73.19915)


# python manage.py test suggestions.tests.GetSuggestionsFilteredListTest
class GetSuggestionsFilteredListTest(APITestCase):
    def setUp(self):
        configDB()

    def test(self):
        response = self.client.get('/suggestions/list/')
        print(f'response JSON ===>>> ok \n {json.dumps(response.json(), ensure_ascii=False)} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/suggestions/list/?q=Am')
        print(f'response JSON ===>>> ok \n {json.dumps(response.json(), ensure_ascii=False)} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)