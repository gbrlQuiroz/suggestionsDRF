# Backend Coding Challenge

### Bussines Logic for score
For obtain the score, it's calculate the distance betwen the latitude and longitude given by the user with the record in database.
The score is put if the distance is in a range each 100 kilometers like this:
- 0 to 100 the score is 1.0
- 101 to 200 the score is 0.9
- 201 to 300 the score is 0.8... and so on...

### Notes
- Python 3.7.9
- Django 3.1.13
- Django Rest Framework 3.12.4
- Database sqlite
- To create Enviroment
> `python3 -m venv venv`
- To activate Enviroment (linux or osx)
> `source venv/bin/activate`
- To install dependencies
> `pip install -r requirements.txt`
- To run locally (warning: you must insert records in the database manually)
> `python manage.py runserver`

### Unit/Integration Tests
- Test without parameters of latitude and longitude
> `python manage.py test suggestions.tests.GetSuggestionsWithoutTest`
- Test all querystrings
> `python manage.py test suggestions.tests.GetSuggestionsWithLatitudeAndLongitudeTest`
- Test error
> `python manage.py test suggestions.tests.GetSuggestionsErrorTest`

- Test POST city
> `python manage.py test city.tests.PostCityTest`
> `python manage.py test city.tests.PostCityError400Test`
> `python manage.py test city.tests.PostCityError409Test`
- Test PUT city
> `python manage.py test city.tests.PutCityTest`
> `python manage.py test city.tests.PutCityError404Test`


### curl Test (examples)
- local
> `curl --location --request GET 'http://localhost:8080/suggestions/?q=A&latitude=45.00000&longitude=-75.00000'`


### Extras
None