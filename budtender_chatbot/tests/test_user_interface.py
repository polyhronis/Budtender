import unittest
from unittest.mock import patch
from budtender_chatbot.src.user_interface import UserInterface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    @patch('budtender_chatbot.src.user_interface.speak_to_text')
    def test_speak_to_text(self, mock_speak_to_text):
        mock_speak_to_text.return_value = "Hello, I need help finding a strain."
        result = self.ui.speak_to_text()
        self.assertEqual(result, "Hello, I need help finding a strain.")

    @patch('budtender_chatbot.src.user_interface.text_to_speech')
    def test_text_to_speech(self, mock_text_to_speech):
        mock_text_to_speech.return_value = "Sure, I can help with that. What are you looking for in a strain?"
        result = self.ui.text_to_speech("Sure, I can help with that. What are you looking for in a strain?")
        self.assertEqual(result, "Sure, I can help with that. What are you looking for in a strain?")

    @patch('budtender_chatbot.src.user_interface.display_strain_info')
    def test_display_strain_info(self, mock_display_strain_info):
        mock_strain_info = {
            "name": "Blue Dream",
            "type": "Hybrid",
            "effects": "Relaxed, Happy, Euphoric",
            "medical": "Stress, Depression, Pain",
            "flavors": "Blueberry, Sweet, Berry"
        }
        mock_display_strain_info.return_value = mock_strain_info
        result = self.ui.display_strain_info(mock_strain_info)
        self.assertEqual(result, mock_strain_info)

if __name__ == '__main__':
    unittest.main()