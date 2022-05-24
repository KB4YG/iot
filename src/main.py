from hardware.camera import cameraHandler
from services.api import sendParkingData
from obj_detection import objDetection 
from services.getWeatherConditions import getWeatherConditions
MDL_PATH = 'coco_ssd_mobilenet_v1_1.0_quant_2018_06_29' #TODO Move to constants

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
    #send image to ml
    result = objDetection(MDL_PATH, filePath)
    print("Number of vehicles: ",result["vehicles"])
    # send data to backend
    if "vehicles" in result:
      sendParkingData(result["vehicles"], weatherConditions["temp"])
      print(result["vehicles"])
    else:
      print(weatherConditions["temp"])
      sendParkingData(0, weatherConditions["temp"])     
    print("Successfully returned from the backend code")
    #1 Specifies that the Pi will turn on and off every minute
    # Change that value to adjust the tick-rate of the updates. 
    #turnOffAndTurnOn(1)
    
    
# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI

if __name__ == '__main__':
    mainRun()

