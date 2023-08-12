```python
import requests
from gpt4_api import GPT4
from cannabis_api import CannabisAPI
from character_profile import CharacterProfile

class Chatbot:
    def __init__(self, gpt4_api_key, cannabis_api_key):
        self.gpt4 = GPT4(gpt4_api_key)
        self.cannabis_api = CannabisAPI(cannabis_api_key)
        self.character_profile = CharacterProfile(age=25, personality="hippie chick", tone="flirty yet professional")

    def initiate_chat(self):
        self.chat_session = self.gpt4.start_chat()
        self.character_profile.greet_user()

    def get_user_message(self, user_query):
        self.user_query = user_query

    def generate_chat_response(self):
        if "strain" in self.user_query:
            strain_name = self.user_query.split("strain")[-1].strip()
            self.strain_info = self.cannabis_api.get_strain_info(strain_name)
            self.chat_response = self.character_profile.respond_with_strain_info(self.strain_info)
        else:
            self.chat_response = self.gpt4.generate_response(self.chat_session, self.user_query)
        return self.chat_response

    def end_chat(self):
        self.gpt4.end_chat(self.chat_session)
        self.character_profile.say_goodbye()
```
