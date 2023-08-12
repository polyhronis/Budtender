import unittest
from unittest.mock import patch
from src import app

class TestApp(unittest.TestCase):

    @patch('src.app.initiate_chat')
    def test_initiate_chat(self, mock_initiate_chat):
        app.initiate_chat()
        mock_initiate_chat.assert_called_once()

    @patch('src.app.end_chat')
    def test_end_chat(self, mock_end_chat):
        app.end_chat()
        mock_end_chat.assert_called_once()

    @patch('src.app.get_strain_info')
    def test_get_strain_info(self, mock_get_strain_info):
        app.get_strain_info('Blue Dream')
        mock_get_strain_info.assert_called_once_with('Blue Dream')

    @patch('src.app.generate_chat_response')
    def test_generate_chat_response(self, mock_generate_chat_response):
        app.generate_chat_response('What is the best strain for anxiety?')
        mock_generate_chat_response.assert_called_once_with('What is the best strain for anxiety?')

    @patch('src.app.speak_to_text')
    def test_speak_to_text(self, mock_speak_to_text):
        app.speak_to_text('What is the best strain for anxiety?')
        mock_speak_to_text.assert_called_once_with('What is the best strain for anxiety?')

    @patch('src.app.text_to_speech')
    def test_text_to_speech(self, mock_text_to_speech):
        app.text_to_speech('Blue Dream is a popular strain for anxiety.')
        mock_text_to_speech.assert_called_once_with('Blue Dream is a popular strain for anxiety.')

    @patch('src.app.display_strain_info')
    def test_display_strain_info(self, mock_display_strain_info):
        app.display_strain_info('Blue Dream')
        mock_display_strain_info.assert_called_once_with('Blue Dream')

    @patch('src.app.marketing_opportunities')
    def test_marketing_opportunities(self, mock_marketing_opportunities):
        app.marketing_opportunities()
        mock_marketing_opportunities.assert_called_once()

if __name__ == '__main__':
    unittest.main()