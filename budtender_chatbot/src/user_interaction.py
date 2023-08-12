```python
import json
from src.gpt4_api import generate_chat_response
from src.cannabis_api import get_strain_info
from src.voice_recognition import speak_to_text
from src.text_to_speech import text_to_speech

class UserInteraction:
    def __init__(self, gpt4_api_key, cannabis_api_key):
        self.gpt4_api_key = gpt4_api_key
        self.cannabis_api_key = cannabis_api_key

    def initiate_chat(self):
        user_query = input("Hello! I'm your budtender chatbot. How can I assist you today?")
        chat_response = generate_chat_response(self.gpt4_api_key, user_query)
        print(chat_response)

    def handle_user_query(self, user_query):
        if "strain" in user_query:
            strain_info = get_strain_info(self.cannabis_api_key, user_query)
            self.display_strain_info(strain_info)
        else:
            chat_response = generate_chat_response(self.gpt4_api_key, user_query)
            print(chat_response)

    def display_strain_info(self, strain_info):
        print(json.dumps(strain_info, indent=4))

    def speak_to_text(self):
        user_query = speak_to_text()
        self.handle_user_query(user_query)

    def text_to_speech(self, chat_response):
        text_to_speech(chat_response)

    def end_chat(self):
        print("It was nice chatting with you. Have a great day!")
```
