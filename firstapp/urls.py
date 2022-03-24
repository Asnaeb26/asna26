from django.urls import path

from firstapp import views

urlpatterns = [
    path('', views.index),
    path('coordinates_view', views.coordinates_view),
    path('create_location', views.create_location),
    path('erase_history', views.erase_history),
]
