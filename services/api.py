import sys
import requests
import datetime

datetime = datetime.datetime.now()

postrequest = {
    "UpdateYear": 2022,
    "OpenSpaces": "10",
    "ParkingLocation":
    "Fitton Green",
    "UpdateMonth": 0,
    "UpdateWeekDay" :1,
    "UpdateDay": 17,
    "LastUpdate": datetime
    }

url = "https://cfb32cwake.execute-api.us-west-2.amazonaws.com/"
x = requests.post(url, data=postrequest)
print(x.text)