from power_api import SixfabPower, Definition, Event
import time
import requests

pms = SixfabPower()
epoch = time.time()

# Remove all events
print("Result removing all Scheduled Event: " + str(pms.remove_all_scheduled_events(200)))

# create power off event to power off the device in 20 seconds
event = Event()
event.id = 1
event.schedule_type = Definition.EVENT_INTERVAL
event.repeat = Definition.EVENT_ONE_SHOT
event.time_interval = 20
event.interval_type = Definition.INTERVAL_TYPE_SEC
event.action = Definition.HARD_POWER_OFF

result = pms.create_scheduled_event_with_event(event, 500)

print("Create S. Event Result: " + str(result))
print("IDs of Scheduled Events: " + str(pms.get_scheduled_event_ids()))


# create power off event to power back on the device in 40 seconds
event = Event()
event.id = 2
event.schedule_type = Definition.EVENT_INTERVAL
event.repeat = Definition.EVENT_ONE_SHOT
event.time_interval = 20
event.interval_type = Definition.INTERVAL_TYPE_SEC
event.action = Definition.HARD_POWER_OFF

result = pms.create_scheduled_event_with_event(event, 500)

print("Create S. Event Result: " + str(result))
print("IDs of Scheduled Events: " + str(pms.get_scheduled_event_ids()))




def getBatteryFactor():
    percentage = pms.get_battery_level()
    if    percentage > 90 : return 0.8
    elif  percentage > 75 : return 0.6
    elif  percentage > 50 : return 0.5
    elif  percentage > 40 : return 0.3
    # Hibernate until battery increases
    elif  percentage > 40 : return 0.05

def getCloudinessFactor():
    percentage = pms.get_battery_level()
    if    percentage > 90 : return 0.8
    elif  percentage > 75 : return 0.6
    elif  percentage > 50 : return 0.5
    elif  percentage > 40 : return 0.3
    # Hibernate until battery increases
    elif  percentage > 40 : return 0.05

    

def getSunriseAndSunset(date):
    #coordinates = readFile()
    r = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today')
    
    #return touple with sunrise and sunset


def figureOutWhenToTurnBackOnAgain():
    # grab battery percentage
    # Is park closed? grab day of the week, grab date and time
    # Grab sunset/sunset time
    # command sent from backend, with override?

    #perform calculations

    turnOffAndTurnOn(20)


def turnOffAndTurnOn(turnOnAgainMin):
    # create power off event to power off the device in 20 seconds
    turnOffEvent = Event()
    turnOffEvent.id = 1
    turnOffEvent.schedule_type = Definition.EVENT_INTERVAL
    turnOffEvent.repeat = Definition.EVENT_ONE_SHOT
    turnOffEvent.time_interval = 10
    turnOffEvent.interval_type = Definition.INTERVAL_TYPE_SEC
    turnOffEvent.action = Definition.HARD_POWER_OFF

    result = pms.create_scheduled_event_with_event(turnOffEvent, 500)

    print("Create S. Event Result: " + str(result))
    print("IDs of Scheduled Events: " + str(pms.get_scheduled_event_ids()))


    # create power off event to power back on the device in 40 seconds
    turnOnEvent = Event()
    turnOnEvent.id = 2
    turnOnEvent.schedule_type = Definition.EVENT_INTERVAL
    turnOnEvent.repeat = Definition.EVENT_ONE_SHOT
    turnOnEvent.time_interval = turnOnAgainMin
    turnOnEvent.interval_type = Definition.INTERVAL_TYPE_MIN
    turnOnEvent.action = Definition.HARD_POWER_OFF

    result2 = pms.create_scheduled_event_with_event(turnOnEvent, 500)

    print("Create S. Event Result: " + str(result2))
    print("IDs of Scheduled Events: " + str(pms.get_scheduled_event_ids()))
