import unittest
from unittest.mock import patch
from src import cannabis_api

class TestCannabisAPI(unittest.TestCase):

    @patch('src.cannabis_api.requests.get')
    def test_get_strain_info(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            "name": "Blue Dream",
            "race": "hybrid",
            "flavors": ["Sweet", "Blueberry", "Berry"],
            "effects": {
                "positive": ["Relaxed", "Happy", "Euphoric"],
                "negative": ["Dry Mouth"],
                "medical": ["Stress", "Anxiety", "Depression"]
            }
        }

        strain_info = cannabis_api.get_strain_info("Blue Dream")
        self.assertEqual(strain_info['name'], "Blue Dream")
        self.assertEqual(strain_info['race'], "hybrid")
        self.assertEqual(strain_info['flavors'], ["Sweet", "Blueberry", "Berry"])
        self.assertEqual(strain_info['effects']['positive'], ["Relaxed", "Happy", "Euphoric"])
        self.assertEqual(strain_info['effects']['negative'], ["Dry Mouth"])
        self.assertEqual(strain_info['effects']['medical'], ["Stress", "Anxiety", "Depression"])

        mock_get.assert_called_once_with(
            "https://rapidapi.com/th3k3rn3lpan1c/api/the-cannabis-api/",
            headers={
                "x-rapidapi-key": "cannabis_api_key",
                "x-rapidapi-host": "th3k3rn3lpan1c.api.rapidapi.com"
            },
            params={"strain_name": "Blue Dream"}
        )

if __name__ == '__main__':
    unittest.main()