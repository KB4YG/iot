from hardware.camera import cameraHandler
from services.api import sendParkingData
from setup.config import *
from ml.img_classifier import imgClassify
from services.getWeatherConditions import getWeatherConditions
from hardware.schedule import turnOffAndTurnOn
MDL_PATH = 'ml/models/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29' #TODO Move to constants
IMG_1 = 'images/five_cars.jpg'
IMG_2 = 'images/one_car.jpg'
IMG_3 = 'images/seven_cars.jpg'
IMG_4 = 'images/three_cars.jpg'
imgArr = [IMG_1,IMG_2, IMG_3, IMG_4];

def mainRun():
    #Need to get lat and long from gps data?
    lat= 44.5646 
    lon= -123.2620 
    units = "imperial"
    weatherConditions = getWeatherConditions(lat, lon, units)
    print(weatherConditions)

    #take image
    #number is the time in milliseconds to expose the sensor (larger number = longer exposure)
    for i in imgArr:
        filePath = imgArr[i]
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

        print("Successfully returned from the backend code, loading next image file")

    
# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI

if __name__ == '__main__':
    mainRun()
