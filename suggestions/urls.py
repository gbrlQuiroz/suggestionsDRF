from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'suggestions'

urlpatterns = [
    path('', SuggestionsEndPoint.as_view(), ),

]
