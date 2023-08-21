```python
import requests
import json

class StrainAPI:
    def __init__(self):
        self.base_url = "https://strainapi.evanbusse.com/"
        self.api_key = "your_api_key"  # replace with your actual API key

    def fetch_strain_data(self, user_preferences):
        """
        Fetch strain data from the Strain API based on user preferences.
        """
        strain_data = {}
        for preference in user_preferences:
            response = requests.get(f"{self.base_url}/{self.api_key}/strains/search/{preference}")
            if response.status_code == 200:
                strain_data[preference] = response.json()
            else:
                print(f"Error: {response.status_code}")
        return strain_data
```