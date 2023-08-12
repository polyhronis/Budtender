```python
import pyttsx3

def text_to_speech(chat_response):
    engine = pyttsx3.init()
    engine.say(chat_response)
    engine.runAndWait()
```