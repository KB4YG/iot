from time import sleep
import os
import time
from picamera import PiCamera
from fractions import Fraction
import datetime
class CameraFileNotFoundError(FileNotFoundError):
    '''Camera file not found after attempting to take picture'''


def takepicDark(exposureTime):
    
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M_low")

    camera = PiCamera(framerate=Fraction(1,6))

    # You can change these as needed. Six seconds (6000000)
    # is the max for shutter speed and 800 is the max for ISO.
    camera.shutter_speed = 1750000
    camera.iso = 800

    time.sleep(30)
    camera.exposure_mode = 'off'

    outfile = "%s.jpg" % (stub)
    camera.capture(outfile)

    camera.close()
 
    
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

