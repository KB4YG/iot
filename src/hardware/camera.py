from time import sleep
import os
import time

class CameraFileNotFoundError(FileNotFoundError):
    '''Camera file not found after attempting to take picture'''

def takepic(exposureTime): 
    fileName = "img_" + str(time.time()) + ".jpg"
    filePath = "./img/" + fileName
    command = "libcamera-still -t " + str(exposureTime) + " -o "  + filePath
    print(command)
    os.system(command)
    sleep(10)
    
    f = open(filePath, "r")
    if f:
        print("File opened successfully")
        return filePath
    else:
        #raise exception
        #handle error
        #retry photo
        #contact our homebase with error  
        print("IN CAMERA FUNC, CAN'T OPEN FILE")
        raise FileNotFoundError('Camera file not found')
 

def cameraHandler(exposureTime = 1000):
    # try: 
       fileName = takepic(exposureTime)
       return fileName
    # except FileNotFoundError as err:
    #     print(err.args)
    #     print("Attempting to try to take picture again")
    #     fileName = takepic(exposureTime)
