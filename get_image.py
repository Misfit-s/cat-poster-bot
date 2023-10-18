import requests
import os
import json

def url():

    # Put your token in a virtual environment 
    apiToken = os.getenv("CATS_API_TOKEN")

    url = f"https://api.thecatapi.com/v1/images/search?api_key={apiToken}"
    data = requests.get(url).content
    image_url = json.loads(data)[0]['url']

    return image_url


