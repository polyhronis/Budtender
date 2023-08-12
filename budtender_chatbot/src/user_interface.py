```python
import tkinter as tk
from voice_recognition import speak_to_text
from text_to_speech import text_to_speech

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Budtender Chatbot")
        self.chatbot_ui = tk.Text(self.window)
        self.user_query = tk.Entry(self.window)
        self.speak_to_text_button = tk.Button(self.window, text="Speak", command=self.speak_to_text)
        self.text_to_speech_button = tk.Button(self.window, text="Listen", command=self.text_to_speech)
        self.strain_info_display = tk.Text(self.window)

    def speak_to_text(self):
        self.user_query.delete(0, tk.END)
        self.user_query.insert(0, speak_to_text())

    def text_to_speech(self):
        text_to_speech(self.chatbot_ui.get("1.0", tk.END))

    def display_strain_info(self, strain_info):
        self.strain_info_display.delete("1.0", tk.END)
        self.strain_info_display.insert(tk.END, strain_info)

    def update_chat(self, user_message, chatbot_message):
        self.chatbot_ui.insert(tk.END, "User: " + user_message + "\n")
        self.chatbot_ui.insert(tk.END, "Chatbot: " + chatbot_message + "\n")

    def run(self):
        self.chatbot_ui.pack()
        self.user_query.pack()
        self.speak_to_text_button.pack()
        self.text_to_speech_button.pack()
        self.strain_info_display.pack()
        self.window.mainloop()
```