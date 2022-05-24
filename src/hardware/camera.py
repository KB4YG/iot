from time import sleep
import os
import time

class CameraFileNotFoundError(FileNotFoundError):
    '''Camera file not found after attempting to take picture'''
#Function for taking a picture using the camera
def takepic(exposureTime): 
    fileName = "img_" + str(time.time()) + ".jpg"
    filePath = "./img/" + fileName
    command = "libcamera-still -t " + str(exposureTime) + " -o "  + filePath
    print(command)
    os.system(command)
    sleep(10)
    #The camera will fill images into the img/ directory
    #Delete old pictures to ensure sufficent storage
    #Check to make sure the image file exists
    f = open(filePath, "r")
    if f:
        print("File opened successfully")
        return filePath
    else:
        raise FileNotFoundError('Camera file not found')
 

def cameraHandler(exposureTime = 1000):
       fileName = takepic(exposureTime)
       return fileName
