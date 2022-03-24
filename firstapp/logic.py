import json

from firstapp.models import Coordinates


def save_to_db(model, data: list) -> object:
    lat, lng = data
    return model.objects.create(latitude=lat, longitude=lng)


def save_location(str_json: str) -> object:
    data = json.loads(str_json)
    return save_to_db(Coordinates, data)


def delete_coordinates(model) -> bool:
    model.objects.all().delete()
    return model.objects.all().count() == 0
