```python
import unittest
from unittest.mock import patch
from src import chatbot

class TestChatbot(unittest.TestCase):

    @patch('src.chatbot.Chatbot.generate_chat_response')
    def test_generate_chat_response(self, mock_generate_chat_response):
        mock_generate_chat_response.return_value = "Sure, I can help with that."
        response = chatbot.Chatbot().generate_chat_response("Can you help me find a strain?")
        self.assertEqual(response, "Sure, I can help with that.")

    @patch('src.chatbot.Chatbot.initiate_chat')
    def test_initiate_chat(self, mock_initiate_chat):
        mock_initiate_chat.return_value = True
        result = chatbot.Chatbot().initiate_chat()
        self.assertTrue(result)

    @patch('src.chatbot.Chatbot.end_chat')
    def test_end_chat(self, mock_end_chat):
        mock_end_chat.return_value = True
        result = chatbot.Chatbot().end_chat()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```