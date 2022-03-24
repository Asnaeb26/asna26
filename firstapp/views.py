from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from firstapp import logic
from firstapp.models import Coordinates


def index(request):
    return render(request, 'firstapp/index.html')


def coordinates_view(request):
    queryset = serializers.serialize('json', Coordinates.objects.all(), fields=('latitude', 'longitude'))
    return JsonResponse(queryset, safe=False)


def create_location(request):
    str_json = request.POST.get('coordinates')
    logic.save_location(str_json)
    response = {
        'data': str_json
    }
    return JsonResponse(response)