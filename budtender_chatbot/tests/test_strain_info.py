import unittest
from unittest.mock import patch
from src.strain_info import get_strain_info

class TestStrainInfo(unittest.TestCase):

    @patch('src.strain_info.requests.get')
    def test_get_strain_info(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            "data": {
                "name": "Blue Dream",
                "race": "hybrid",
                "flavors": ["Sweet", "Blueberry", "Berry"],
                "effects": {
                    "positive": ["Relaxed", "Happy", "Euphoric"],
                    "negative": ["Dry Mouth"],
                    "medical": ["Stress", "Anxiety", "Depression"]
                }
            }
        }

        strain_info = get_strain_info("Blue Dream")
        self.assertEqual(strain_info['name'], "Blue Dream")
        self.assertEqual(strain_info['race'], "hybrid")
        self.assertEqual(strain_info['flavors'], ["Sweet", "Blueberry", "Berry"])
        self.assertEqual(strain_info['effects']['positive'], ["Relaxed", "Happy", "Euphoric"])
        self.assertEqual(strain_info['effects']['negative'], ["Dry Mouth"])
        self.assertEqual(strain_info['effects']['medical'], ["Stress", "Anxiety", "Depression"])

if __name__ == '__main__':
    unittest.main()