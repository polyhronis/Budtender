```python
import speech_recognition as sr
from gtts import gTTS
import os

class VoiceLibraries:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def text_to_speech(self, text, language='en'):
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("start text.mp3")

    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
                return query
            except Exception as e:
                print("Say that again please...")
                return "None"
```