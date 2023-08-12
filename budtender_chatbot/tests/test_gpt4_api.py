import unittest
from unittest.mock import patch
from src import gpt4_api

class TestGpt4Api(unittest.TestCase):

    @patch('src.gpt4_api.requests.get')
    def test_generate_chat_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'message': 'Hello, I am your budtender chatbot.'
        }

        gpt4_api_key = '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'
        user_query = 'What is the best strain for anxiety?'

        response = gpt4_api.generate_chat_response(gpt4_api_key, user_query)
        self.assertEqual(response, 'Hello, I am your budtender chatbot.')

    @patch('src.gpt4_api.requests.get')
    def test_generate_chat_response_error(self, mock_get):
        mock_get.return_value.status_code = 404

        gpt4_api_key = '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'
        user_query = 'What is the best strain for anxiety?'

        response = gpt4_api.generate_chat_response(gpt4_api_key, user_query)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()