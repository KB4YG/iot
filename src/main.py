# from ml.main import run
from hardware.camera import cameraHandler
from services.api import sendParkingData
from setup.config import *
from ml.img_classifier import imgClassify

MDL_PATH = 'ml/models/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29' #TODO Move to constants

def mainRun():
    #take image
    #number is the time in milliseconds to expose the sensor (larger number = longer exposure)
    filePath = cameraHandler(1000)
    print(filePath)

    #send image to ml
    _, count = imgClassify(MDL_PATH, filePath)
    print(count)
    # send data to backend
    if "car" in count:
        sendParkingData(count["car"])
    else:
        sendParkingData(0)

    print("Successfully returned from the backend code")
    
# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI

if __name__ == '__main__':
    mainRun()
