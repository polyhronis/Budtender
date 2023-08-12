```python
from src.voice_recognition import speak_to_text
from src.text_to_speech import text_to_speech
from src.user_interaction import initiate_chat, end_chat

class UserExperience:
    def __init__(self, user):
        self.user = user
        self.chat_active = False

    def start_chat(self):
        self.chat_active = True
        initiate_chat(self.user)

    def end_chat(self):
        end_chat(self.user)
        self.chat_active = False

    def handle_user_input(self, user_input):
        if self.chat_active:
            if user_input == 'speak':
                user_input = speak_to_text()
            elif user_input == 'listen':
                text_to_speech()
            else:
                return "Invalid input. Please either type your message or use 'speak' or 'listen' commands."

    def display_strain_info(self, strain_info):
        print(f"Strain Name: {strain_info['name']}")
        print(f"Strain Type: {strain_info['type']}")
        print(f"Strain Description: {strain_info['description']}")
        print(f"Strain Effects: {', '.join(strain_info['effects'])}")
        print(f"Strain Flavors: {', '.join(strain_info['flavors'])}")

    def run(self):
        while self.chat_active:
            user_input = input("Type your message or use 'speak' or 'listen' commands: ")
            self.handle_user_input(user_input)
```
