# coding: utf-8
import os
# print(os.getenv('MAPS', 'No value found'))
import json
import urllib.request


# The maps_key defined below isn't a valid Google Maps API key.
# You need to get your own API key.
# See https://developers.google.com/maps/documentation/geocoding/get-api-key
API_KEY = os.getenv('MAPS')
GEOCODE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

def geocode(address):
    # Join the parts of the URL together into one string.
    params = urllib.parse.urlencode({"address": address, "key": API_KEY,})
    url = f"{GEOCODE_BASE_URL}?{params}"

    result = json.load(urllib.request.urlopen(url))

    if result["status"] in ["OK", "ZERO_RESULTS"]:
        return result["results"]

    raise Exception(result["error_message"])

if __name__ == "__main__":
    results = geocode(address= input("Que voulez-vous savoir?" "\n").replace(' ', '+'))
    print(json.dumps([r["geometry"]["location"]["lat"]for r in results]))
    print(json.dumps([r["geometry"]["location"]["lng"]for r in results]))
    print(json.dumps([s["formatted_address"] for s in results]))

# [{'address_components': [{'long_name': 'Rosporden', 'short_name': 'Rosporden', 'types': ['locality', 'political']}, 
# {'long_name': 'Finistere', 'short_name': 'Finistere', 'types': ['administrative_area_level_2', 'political']}, 
# {'long_name': 'Brittany', 'short_name': 'Brittany', 'types': ['administrative_area_level_1', 'political']}, 
# {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '29140', 'short_name': '29140', 'types': ['postal_code']}],
#  'formatted_address': '29140 Rosporden, France', 'geometry': {'location': {'lat': 47.96849, 'lng': -3.8282244}, 'location_type': 'GEOMETRIC_CENTER',
#   'viewport': {'northeast': {'lat': 47.96983898029149, 'lng': -3.826875419708498}, 'southwest': {'lat': 47.9671410197085, 'lng': -3.829573380291502}}},
#    'place_id': 'ChIJzeyxx0jeEEgR4EWaHlTfyp4', 'plus_code': {'compound_code': 'X59C+9P Rosporden, France', 'global_code': '8CVRX59C+9P'},
#     'types': ['establishment', 'health', 'point_of_interest']}]
