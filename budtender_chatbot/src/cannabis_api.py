import requests
import json

cannabis_api_key = "your_cannabis_api_key_here"

def get_strain_info(user_query):
    url = "https://th3k3rn3lpan1c-cannabis-api.p.rapidapi.com/strains/search/name/" + user_query

    headers = {
        'x-rapidapi-host': "th3k3rn3lpan1c-cannabis-api.p.rapidapi.com",
        'x-rapidapi-key': cannabis_api_key
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        strain_info = json.loads(response.text)
        return strain_info
    else:
        return None