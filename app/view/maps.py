# coding: utf-8
import os
import requests
from .constants import API_KEY, GEOCODE_BASE_URL
from pprint import pprint


class maps:

    def geocode(address):
        params = {
            "address": address,
            "key": API_KEY,
            "region": 'FR',
            }
        url = f"{GEOCODE_BASE_URL}"
        result = requests.get(url, params=params)
        response_map = result.json()
        location = {'lat': 1, 'lng': 1}

        return response_map['results'][0]['geometry']['location']
        # return response_map['results'][0]['formatted_address']

# print(os.getenv('MAPS'))
# maps.geocode('peux tu me dire quel est la capitale de la france?')