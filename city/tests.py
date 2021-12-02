# from django.test import TestCase
from rest_framework.test import APITestCase
import json
from rest_framework import status

from suggestions.models import *


def configDB():
    City.objects.create(name='Amherst', latitude=45.83345, longitude=-64.19874)
    City.objects.create(name='Amherstburg', latitude=42.11679, longitude=-83.04985)
    City.objects.create(name='Amos', latitude=48.56688, longitude=-78.11624)
    City.objects.create(name='Amityville', latitude=40.67899, longitude=-73.41707)
    City.objects.create(name='Amsterdam', latitude=42.93869, longitude=-74.18819)
    City.objects.create(name='Amesbury', latitude=42.85842, longitude=-70.93005)
    City.objects.create(name='Amherst Center', latitude=42.37537, longitude=-72.51925)
    City.objects.create(name='Ambler', latitude=40.15455, longitude=-75.22157)
    City.objects.create(name='Amqui', latitude=48.46382, longitude=-67.43134)  # este se modifica
    City.objects.create(name='Beaumont', latitude=53.35013, longitude=-13.41871)
    City.objects.create(name='Belleville', latitude=44.16682, longitude=-77.38277)
    City.objects.create(name='Beloeil', latitude=45.56678, longitude=-73.19915)


#  Probar POST para crear un registro de City
# python manage.py test city.tests.PostCityTest
class PostCityTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "Pachuca de Soto",
            "latitude": 333.333,
            "longitude": 999.999
        }

    def test(self):

        response = self.client.post('/city/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#  Probar POST para crear un registro de City
# python manage.py test city.tests.PostCityError400Test
class PostCityError400Test(APITestCase):
    def setUp(self):
        configDB()

        self.json = {}

    def test(self):

        response = self.client.post('/city/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#  Probar POST con error 409
# python manage.py test city.tests.PostCityError409Test
class PostCityError409Test(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "Amqui",
            "latitude": 333.333,
            "longitude": 999.999
        }

    def test(self):

        response = self.client.post('/city/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)


#  Probar PUT  para modificar un registro de City
# python manage.py test city.tests.PutCityTest
class PutCityTest(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "Pachuca",
            "latitude": 333.333,
            "longitude": 999.999
        }

    def test(self):

        self.assertEqual('Amqui', City.objects.get(id=9).name)

        response = self.client.put('/city/9/update/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual('Pachuca', City.objects.get(id=9).name)


#  Probar PUT  error 404
# python manage.py test city.tests.PutCityError404Test
class PutCityError404Test(APITestCase):
    def setUp(self):
        configDB()

        self.json = {
            "name": "Pachuca",
            "latitude": 333.333,
            "longitude": 999.999
        }

    def test(self):

        response = self.client.put('/city/369/update/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
