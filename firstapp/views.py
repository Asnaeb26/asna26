from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from firstapp.logic import *


def index(request):
    return render(request, 'firstapp/index.html')


def coordinates_view(request):
    queryset = serializers.serialize('json', Coordinates.objects.all(), fields=('latitude', 'longitude'))
    return JsonResponse(queryset, safe=False)


def create_location(request):
    str_json = request.POST.get('coordinates')
    save_location(str_json)
    response = {
        'data': str_json
    }
    return JsonResponse(response)
