import unittest
from unittest.mock import patch
from src import user_interaction

class TestUserInteraction(unittest.TestCase):

    @patch('src.user_interaction.get_strain_info')
    @patch('src.user_interaction.generate_chat_response')
    def test_initiate_chat(self, mock_generate_chat_response, mock_get_strain_info):
        user_interaction.initiate_chat()
        mock_generate_chat_response.assert_called_once()
        mock_get_strain_info.assert_called_once()

    @patch('src.user_interaction.get_strain_info')
    @patch('src.user_interaction.generate_chat_response')
    def test_end_chat(self, mock_generate_chat_response, mock_get_strain_info):
        user_interaction.end_chat()
        mock_generate_chat_response.assert_not_called()
        mock_get_strain_info.assert_not_called()

    @patch('src.user_interaction.speak_to_text')
    def test_speak_to_text(self, mock_speak_to_text):
        user_interaction.speak_to_text("Hello")
        mock_speak_to_text.assert_called_once_with("Hello")

    @patch('src.user_interaction.text_to_speech')
    def test_text_to_speech(self, mock_text_to_speech):
        user_interaction.text_to_speech("Hello")
        mock_text_to_speech.assert_called_once_with("Hello")

    @patch('src.user_interaction.display_strain_info')
    def test_display_strain_info(self, mock_display_strain_info):
        user_interaction.display_strain_info("Sativa")
        mock_display_strain_info.assert_called_once_with("Sativa")

if __name__ == '__main__':
    unittest.main()