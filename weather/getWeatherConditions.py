import requests 
from sys import argv
import json
from types import SimpleNamespace
#Units Available are: imperial, and metric
def getWeatherConditions(lat, long, units):
    apiKey = "1039cb4688b71dfbab9df96f45f27677"
    payload = {'lat': lat , 'lon': long, 'units': units, 'appid': apiKey}
    x = requests.get('https://api.openweathermap.org/data/2.5/weather',params=payload)
    weather = json.loads(x.text, object_hook=lambda d: SimpleNamespace(**d))
    if units == "imperial":
        if weather.main.temp > 32:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear for normal operations")
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature looks good, but bad weather may occur")
        else:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear, but temperature is below freezing")
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature is below freezing, and bad weather may occur")
    if units == "metric":
        if weather.main.temp > 0:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear for normal operations")
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature looks good, but bad weather may occur")
        else:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear, but temperature is below freezing")
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature is below freezing, and bad weather may occur")      

getWeatherConditions(*argv[1:])

