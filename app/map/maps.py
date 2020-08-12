# coding: utf-8
import os
import requests
from .constants import API_KEY, GEOCODE_BASE_URL

    
def geocode(address):

    params = {
    	"address": address,
    	"key": API_KEY,
    	}

    url = f"{GEOCODE_BASE_URL}"
    result = requests.get(url, params=params)
    response_map = result.json()

    return response_map["results"][0]["geometry"]["location"]