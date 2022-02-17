# from ml.main import run
from hardware.camera import cameraHandler
from services.api import sendParkingData
from setup.config import *
from ml.img_classifier import imgClassify
from services.getWeatherConditions import getWeatherConditions
from hardware.schedule import turnOffAndTurnOn
MDL_PATH = 'ml/models/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29' #TODO Move to constants

def mainRun():
    #Need to get lat and long from gps data?
    lat= 44.5646 
    lon= -123.2620 
    units = "imperial"
    weatherConditions = getWeatherConditions(lat, lon, units)
    print(weatherConditions)

    #take image
    #number is the time in milliseconds to expose the sensor (larger number = longer exposure)
    filePath = cameraHandler(1000)
    print(filePath)

    #send image to ml
    _, count = imgClassify(MDL_PATH, filePath)
    print(count)
    # send data to backend

    #Need to update this to send in the weather data as well.
    if "car" in count:
        sendParkingData(count["car"], weatherConditions.temp)
    else:
        print(weatherConditions["temp"])
        sendParkingData(0, weatherConditions["temp"])

    print("Successfully returned from the backend code")
    turnOffAndTurnOn(1)
    
    
# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI

if __name__ == '__main__':
    mainRun()
