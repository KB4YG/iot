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
    filePath = ["./img/two_cars.jpg", "./img/seven_cars.jpg", "./img/five_cars.jpg"]
    #send image to ml
    result = objDetection(MDL_PATH, filePath[0])
    print("Number of vehicles: ",result["vehicles"])
    # send data to backend
    if "vehicles" in result:
      sendParkingData(result["vehicles"], weatherConditions["temp"])
      print(result["vehicles"])
    else:
      print(weatherConditions["temp"])
      sendParkingData(0, weatherConditions["temp"])     
    print("Successfully returned from the backend code")

if __name__ == '__main__':
    mainRun()
