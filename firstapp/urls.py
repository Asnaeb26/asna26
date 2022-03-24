from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('coordinates_view', coordinates_view),
    path('create_location', create_location),
]
