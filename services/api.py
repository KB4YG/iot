import sys
import requests
import datetime

# time interval? or are we going to run once at boot

# take picture, save to sd card

# run ML algo that returns var with # of cars

datetime = datetime.datetime.now()
interval = CONSTANT;

postrequest = {
    "UpdateYear": 2022,
    "OpenSpaces": "10",
    "ParkingLocation":
    "Fitton Green",
    "UpdateMonth": 0,
    "UpdateWeekDay" :1,
    "UpdateDay": 17,
    "LastUpdate": datetime,
    "BatteryPercentage": 87,
    "Temperature": 32,
    "NextCommunication": datetime + interval,
    }

url = "https://cfb32cwake.execute-api.us-west-2.amazonaws.com/"
x = requests.post(url, data=postrequest)
print(x.text)

# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI