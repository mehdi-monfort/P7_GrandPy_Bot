import requests


def wiki():

    url = "https://fr.wikipedia.org/w/api.php"
     
    latitude = 48.856614
    longitude = 2.3522219
     
    params = {
        "format": "json",
        "action": "query",
        "list": "geosearch",
        "gsradius": 10000,
        "gscoord": f"{latitude}|{longitude}"
    }

    response = requests.get(url, params=params)
    geosearch_data = response.json()
    page_id = geosearch_data['query']['geosearch'][0]['pageid']

    params = {
        "format": "json",
        "action": "query",
        "prop": "extracts|info",
        "inprop": "url",
        "explaintext": 1,
        "pageids": page_id
    }

    result = requests.get(url, params=params)
    result.raise_for_status()

    response_wiki = result.json()
    return response_wiki
    print(response['query']['pages'][str(page_id)]['extract'])

# faire class puis faire les test avec pytest