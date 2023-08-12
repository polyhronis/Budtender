```python
import requests

class StrainInfo:
    def __init__(self, cannabis_api_key):
        self.cannabis_api_key = cannabis_api_key
        self.base_url = "https://rapidapi.com/th3k3rn3lpan1c/api/the-cannabis-api/"

    def get_strain_info(self, strain_name):
        headers = {
            'x-rapidapi-key': self.cannabis_api_key,
            'x-rapidapi-host': "the-cannabis-api.p.rapidapi.com"
        }
        response = requests.request("GET", self.base_url + "strains/search/name/" + strain_name, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
```