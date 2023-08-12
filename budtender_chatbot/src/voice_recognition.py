```python
import speech_recognition as sr

def speak_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            user_query = r.recognize_google(audio, language='en-US')
            print(f"User said: {user_query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return user_query
```