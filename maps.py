import sys
from io import BytesIO
import requests
from PIL import Image
from size import init_spn


toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(" + response.reason + ")")
    sys.exit(0)

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = init_spn(toponym)
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": delta,
    "l": "map",
    "pt": ",".join([toponym_longitude, toponym_lattitude, 'pm2rdm'])
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()