import requests 
from sys import argv
import json
from types import SimpleNamespace

def getWeatherConditions(lat, long, units):
    apiKey = "1039cb4688b71dfbab9df96f45f27677"
    payload = {'lat': lat , 'lon': long, 'units': units, 'appid': apiKey}
    x = requests.get('https://api.openweathermap.org/data/2.5/weather',params=payload)
    weather = json.loads(x.text, object_hook=lambda d: SimpleNamespace(**d))
    print(weather.main.temp)
getWeatherConditions(*argv[1:])

