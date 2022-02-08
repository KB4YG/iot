import requests 
import sys


def getWeatherConditions(lat, long):
    apiKey = "1039cb4688b71dfbab9df96f45f27677"
    x = requests.get('https://w3schools.com')
    print(x.status_code)
