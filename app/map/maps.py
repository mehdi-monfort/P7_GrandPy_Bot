# coding: utf-8
import os
import json
import urllib.request
# import gmaps
from .constants import API_KEY, GEOCODE_BASE_URL

# class maps:
    
def geocode(address):

    params = urllib.parse.urlencode({"address": address, "key": API_KEY,})
    url = f"{GEOCODE_BASE_URL}?{params}"

    result = json.load(urllib.request.urlopen(url))

    if result["status"] in ["OK", "ZERO_RESULTS"]:
        return result["results"]

    raise Exception(result["error_message"])
    # address= input()
    # results = geocode(address.replace(' ', '+'))
    # # for r in results:
    # #     place_id = json.dumps([r["place_id"]])

    # #     return place_id
