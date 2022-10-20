from unittest import result
import phonenumbers
import opencage
import folium
from myphone import numbers
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(numbers)
location = geocoder.description_for_number(pepnumber, "en")
print(location)
from phonenumbers import carrier

serviece_pro = phonenumbers.parse(numbers)
print(carrier.name_for_number(serviece_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key = 'bdae51e9001d44efb1c1155f30d4a0a6'

geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)
# print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save('mylocation.html')