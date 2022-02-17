import requests 
from sys import argv
import json
from types import SimpleNamespace
#Units Available are: imperial, and metric
#Key for return statements:
# 0 = all clear 
# 1 = above freezing temperature/clear weather
# 2 = below freezing/clear weather
# 3 = below freezing/ bad weather
# None = none of the conditions were met
def getWeatherConditions(lat, long, units):
    apiKey = "1039cb4688b71dfbab9df96f45f27677"
    payload = {'lat': lat , 'lon': long, 'units': units, 'appid': apiKey}
    x = requests.get('https://api.openweathermap.org/data/2.5/weather',params=payload)
    weather = json.loads(x.text, object_hook=lambda d: SimpleNamespace(**d))
    print("API Status Code: ", str(weather.cod))
    print("City Name: " , weather.name)
    print("Current Temp: ", str(weather.main.temp))
    print("Current Weather: ", weather.weather[0].main)
    if units == "imperial":
        if weather.main.temp > 32:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear for normal operations")
                message = { 'code': 0, 'desc': 'Weather is clear for normal operations', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                return message
            else:
                 if weather.weather[0].main== "Rain" or weather.weather[0].main== "Clouds":
                     print("Temperature looks good, weather is bad, or there are clouds ")
                     message = { 'code': 1, 'desc': 'Temperature looks good, weather is bad, or there are clouds', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                     return message
        else:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear, but temperature is below freezing")
                message = { 'code': 2, 'desc': 'Weather is clear, but temperature is below freezing', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                return message
                
            else:
                 if weather.weather[0].main== "Rain" or weather.weather[0].main== "Clouds":
                     print("Temperature is below freezing, weather is bad, or there are clouds")
                     message = { 'code': 3, 'desc': 'Temperature is below freezing, weather is bad, or there are clouds', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                     return message
                     
    if units == "metric":
        if weather.main.temp > 0:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear for normal operations")
                message = { 'code': 0, 'desc': 'Weather is clear for normal operations', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                return message
                
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature looks good, but bad weather may occur")
                     message = { 'code': 1, 'desc': 'Temperature looks good, but bad weather may occur', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                     return message
        else:
            if(weather.weather[0].main =="Clear"):
                print("Weather is clear, but temperature is below freezing")
                message = { 'code': 2, 'desc': 'Weather is clear, but temperature is below freezing', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                return message
            else:
                 if weather.weather[0].main== "Rain":
                     print("Temperature is below freezing, and bad weather may occur") 
                     message = { 'code': 3, 'desc': 'Temperature is below freezing, and bad weather may occur', 'temp': weather.main.temp, 'sunrise': weather.sys.sunrise, 'sunset': weather.sys.sunset}
                     return message    
                      
    



