import requests
import json
from datetime import datetime

# API
api_url = "https://api.jcdecaux.com/vls/v1/stations?contract=maribor&apiKey=5e150537116dbc1786ce5bec6975a8603286526b"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    with open('data/raw/svezi_podatki.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
else:
    print("Error")