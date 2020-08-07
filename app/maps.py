# coding: utf-8
import os
import json
import urllib.request
import gmaps
from constants import API_KEY, GEOCODE_BASE_URL

class maps:
    
    def geocode(address):

        params = urllib.parse.urlencode({"address": address, "key": API_KEY,})
        url = f"{GEOCODE_BASE_URL}?{params}"

        result = json.load(urllib.request.urlopen(url))

        if result["status"] in ["OK", "ZERO_RESULTS"]:
            return result["results"]

        raise Exception(result["error_message"])

    def display(latitude, longitude):

        gmaps.configure(api_key = API_KEY)
        marker_location = (latitude, longitude)

        fig = gmaps.figure()
        markers = gmaps.marker_layer(marker_location)
        fig.add_layer(markers)
        fig = gmaps.figure(center=(latitude, longitude), zoom_level=8)

if __name__ == "__main__":
    address= input("Que voulez-vous savoir?" "\n")
    results = maps.geocode(address.replace(' ', '+'))
    for r in results:
        latitude = json.dumps([r["geometry"]["location"]["lat"]]),
        longitude = json.dumps([r["geometry"]["location"]["lng"]]),
        place_id = json.dumps([r["place_id"]])
    print(latitude, longitude)

    maps.display(latitude, longitude)


# wikimedia: avec les coordonnées recupérer l'id 
# de page et après avec id de page demande un extrait (2 requetes)