from ..src.services.getWeatherConditions import getWeatherConditions
#Positive Lat = North of Equator
# Negative Lat = South of Equator
#Postitive Long  = East of Prime Meridian 
#Negative Long = West of Prime Meridian

#Some examples: 


#Corvallis:
lat= 44.5646 
lon= -123.2620 
units = "imperial"
x = getWeatherConditions(lat,lon,units)
print (x)


#Sydney, Australia
lat2= -33.8688
lon2= 151.2093
x = getWeatherConditions(lat2,lon2,units)
print (x)

#Los Angeles
lat3= 34.0522
lon3= -118.2437
x = getWeatherConditions(lat3,lon3,units)
print (x)


