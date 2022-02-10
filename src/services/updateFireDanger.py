import json
from string import Template
import requests as requests
from pyproj import Transformer


# converts from EPSG:4326 (WGS84) to EPSG:3857 (Web Mercator)
# aka converts cordinates system to point system
def convertLatLongToXY(lat, long):
    transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
    x, y = transformer.transform(lat, long)
    return x, y


# Queries ODF fire danger website and returns current danger level for a given location
# This URL address was extracted from the ODF website and is not guaranteed to work
def getWeatherConditions(lat, long):
    x, y = convertLatLongToXY(lat, long)  # ArcGis API requires xy points (EPSG:3857) instead of long/lat (EPSG:4326)
    if x == float('inf') or y == float('inf'):
        print("Error: Invalid coordinates, values are incorrect or you may have mixed Latitude and Longitude")
        return -1

    # build the URL, only param that is required is the xy point in geometry={'x':$x,'y':$y}
    proxy = "https://gisapps.odf.oregon.gov/gisauthproxy/proxy.ashx?"
    urlbase = "https://gis.odf.oregon.gov/ags1/rest/services/Feature/FireRestrictions/mapserver/identify?f="
    param = Template("json&tolerance=1&returnGeometry=true&imageDisplay=0,400,96&geometry={'x':$x,'y':$y}&geometryType=esriGeometryPoint&sr=102100&mapExtent=-13735297.575898776,5543270.585318234,-13724195.09754037,5551401.574202059&layers=all:0,1,2")
    param = param.substitute(x=x, y=y)
    url = proxy + urlbase + param

    r = requests.get(url)
    if r.status_code != 200:
        print("Error: Unable to connect to Fire Restrictions Service")
        return -1

    # parse the JSON response, a sample of which can be found below
    r = json.loads(r.content)
    fireResults = r['results']
    if len(fireResults) < 3:
        print("Error: No Fire Restrictions found")
        return -1

    fd = fireResults[1]['attributes']
    print("Fire Danger Level: ", fd['FireDanger'])
    print("Fire Danger Restriction: ", fd['IfplRestrictionLevel'])
    print("'PendingChangeDateTime': ", fd['PendingChangeDateTime']) # time last updated? time it was ment to be updated?

    # dependent on frontend team requirements may return full json object instead of just the fire danger level
    return fd['FireDanger'] # Low, Medium, High, None


getWeatherConditions(44.576087, -123.370796) # Fitton green


"""
Sample JSON response from ODF website:

results is an array of 3 objects
[0] is Regulated Use
[1] is Fire Danger Levels (only one we use)
[2] is Industrial Fire Precaution Levels

results= [
{
   "layerId":1,
   "layerName":"Fire Danger Levels",
   "displayFieldName":"RegUseArea",
   "value":"WO-3",
   "attributes":{
      "OBJECTID":"68",
      "RegUseArea":"WO-3",
      "IfplRestrictionPending":"0",
      "IfplRestrictionLevel":"Fire Season Not In Effect",
      "FireDanger":"Low",
      "RegUseInEffect":"0",
      "PendingChangeDateTime":"10/5/2021 1:00:00 AM",
      "IfplRestrictionLevelChange":"Fire Season Not In Effect",
      "DebrisBurning":"NA",
      "Smoking":"Smoking in designated locations, vehicles on improved roads and boats in the water",
      "Mowing":"NA",
      "CuttingWelding":"NA",
      "CuttingWeldingOther":"NA",
      "Blasting":"NA",
      "Other":"NA",
      "Shape":"Polygon",
      "District":"West Oregon",
      "OpenFire":"Campfires in designated locations",
      "OpenFireWoodBurning":"NA",
      "OpenFireOther":"Portable cooking stoves using liquified fuels OK",
      "ExplodingTarget":"NA",
      "Firework":"No Fireworks",
      "CuttingWeldingPro":"NA",
      "PowerSaw":"NA",
      "PowerSawEquipment":"NA",
      "PowerSawFireWatch":"NA",
      "MotorVehicle":"NA",
      "ElectricFence":"NA",
      "MotorVehicleTool":"All vehicles must have a shovel and fire extinguisher or gallon of water. ATV\\'s and motorcycles must be equipped with a fire extinguisher"
   },
   "geometry":{}
}]
"""