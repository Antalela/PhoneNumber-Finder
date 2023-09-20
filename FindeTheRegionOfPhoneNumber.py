import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier

import webbrowser
 
from opencage.geocoder import OpenCageGeocode
 
# Enter the phonenumber along with the country code
number = "+905******235"

# Parsing the phonenumber (string) into phonenumber format
phoneNumber = phonenumbers.parse(number)

# Storing the API Key
Key = "6759620be********d32c9907b05"# ====>>> generate your api here https://opencagedata.com/api
 
# Using the geocoder module of phonenumbers to print the Location in console
phoneServicingRegion = geocoder.description_for_valid_number(phoneNumber , "en")
print("Servicing Region : " +phoneServicingRegion)
 

# Using the carrier module of phonenumbers to print the service provider name in console
phoneServiceProvider = carrier.name_for_number(phoneNumber , "en")
print("Service Provider : " +phoneServiceProvider)
 
# Using the geocoder to get url of map with location and storing it in url variable
geocoder = OpenCageGeocode(Key)
query = str(phoneServicingRegion)
results = geocoder.geocode(query)
 
url = results[0]['annotations']['OSM']['url']

# Using the webbrowser to open url with location in default browser
webbrowser.open(url , new=2 , autoraise=True)