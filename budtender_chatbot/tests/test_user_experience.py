import unittest
from unittest.mock import patch
from src import user_experience

class TestUserExperience(unittest.TestCase):

    @patch('src.user_experience.speak_to_text')
    @patch('src.user_experience.text_to_speech')
    def test_speak_to_text_and_text_to_speech(self, mock_speak_to_text, mock_text_to_speech):
        user_experience.speak_to_text('Hello')
        mock_speak_to_text.assert_called_once_with('Hello')

        user_experience.text_to_speech('Hello')
        mock_text_to_speech.assert_called_once_with('Hello')

    @patch('src.user_experience.initiate_chat')
    @patch('src.user_experience.end_chat')
    def test_chat_session(self, mock_initiate_chat, mock_end_chat):
        user_experience.initiate_chat()
        mock_initiate_chat.assert_called_once()

        user_experience.end_chat()
        mock_end_chat.assert_called_once()

    @patch('src.user_experience.display_strain_info')
    def test_display_strain_info(self, mock_display_strain_info):
        strain_info = {'name': 'Blue Dream', 'type': 'Hybrid', 'effects': 'Relaxed, Happy, Euphoric'}
        user_experience.display_strain_info(strain_info)
        mock_display_strain_info.assert_called_once_with(strain_info)

if __name__ == '__main__':
    unittest.main()