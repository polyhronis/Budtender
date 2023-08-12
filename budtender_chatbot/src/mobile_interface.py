```python
from flask import Flask, render_template, request
from .user_interface import UserInterface
from .voice_recognition import speak_to_text
from .text_to_speech import text_to_speech

app = Flask(__name__)

class MobileInterface(UserInterface):
    def __init__(self):
        super().__init__()

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/chat', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':
            user_query = request.form['user_query']
            chat_response = self.generate_chat_response(user_query)
            return render_template('chat.html', chat_response=chat_response)
        else:
            return render_template('chat.html')

    @app.route('/speak_to_text', methods=['POST'])
    def convert_speak_to_text():
        audio_file = request.files['audio_file']
        user_query = speak_to_text(audio_file)
        return user_query

    @app.route('/text_to_speech', methods=['POST'])
    def convert_text_to_speech():
        text = request.form['text']
        audio_file = text_to_speech(text)
        return audio_file

    @app.route('/strain_info', methods=['GET'])
    def display_strain_info():
        strain_info = self.get_strain_info()
        return render_template('strain_info.html', strain_info=strain_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```