from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'city'

urlpatterns = [
    path('create/', CityCreateView.as_view(), ),

]
