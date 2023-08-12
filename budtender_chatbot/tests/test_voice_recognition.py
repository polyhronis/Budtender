import unittest
from src.voice_recognition import speak_to_text

class TestVoiceRecognition(unittest.TestCase):

    def setUp(self):
        self.sample_audio = "sample_audio.wav"

    def test_speak_to_text(self):
        expected_text = "Hello, I am looking for a strain that can help with anxiety."
        result = speak_to_text(self.sample_audio)
        self.assertEqual(result, expected_text)

if __name__ == '__main__':
    unittest.main()