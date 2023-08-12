import unittest
from unittest.mock import patch
from src import text_to_speech

class TestTextToSpeech(unittest.TestCase):

    @patch('src.text_to_speech.pyttsx3.init')
    def test_text_to_speech(self, mock_init):
        mock_engine = mock_init.return_value
        text_to_speech.text_to_speech("Hello")
        mock_engine.say.assert_called_once_with("Hello")
        mock_engine.runAndWait.assert_called_once()

if __name__ == '__main__':
    unittest.main()