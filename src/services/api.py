import sys
import requests
import datetime
from ..ml.main import run as ml

# time interval? or are we going to run once at boot

# take picture, save to sd card

# run ML algo that returns var with # of cars

# datetime = datetime.datetime.now()
# interval = CONSTANT;

# postrequest = {
#     "UpdateYear": 2022,
#     "OpenSpaces": "10",
#     "ParkingLocation":
#     "Fitton Green",
#     "UpdateMonth": 0,
#     "UpdateWeekDay" :1,
#     "UpdateDay": 17,
#     "LastUpdate": datetime,
#     "BatteryPercentage": 87,
#     "Temperature": 32,
#     "NextCommunication": datetime + interval,
#     }

# url = "https://cfb32cwake.execute-api.us-west-2.amazonaws.com/"
# x = requests.post(url, data=postrequest)
# print(x.text)


# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Call ML algo
result = ml()
print(result)

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "afabojvlqjyw-ats.iot.us-west-2.amazonaws.com"
CLIENT_ID = "basicPubSub"
PATH_TO_CERTIFICATE = "/home/pi/iot/setup/certificates/TestNode1/23af9987dae6a24f2cf0805ae70a74425e67743e0fca1fc70fbd68a87593c6e9-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "/home/pi/iot/setup/certificates/TestNode1/23af9987dae6a24f2cf0805ae70a74425e67743e0fca1fc70fbd68a87593c6e9-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "/home/pi/iot/setup/certificates/TestNode1/AmazonRootCA1.pem"
#MESSAGE = "Hello World – What's going on DAVID"
MESSAGE = {
  "LocationId": "1234",
  "OpenGeneral": "10",
  "OpenHandicap": "10",
  "UsedGeneral": "2",
  "UsedHandicap": "2",
  "Temp": "42",
  "Confidence": "80"
}
TOPIC = "topic_1"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{}".format(MESSAGE)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()


# Modify settings if response says to. i.e. change interval or sleep.

#Shut down PI