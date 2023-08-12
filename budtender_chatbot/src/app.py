```python
from flask import Flask, render_template, request
from .chatbot import Chatbot
from .user_interaction import UserInteraction
from .user_experience import UserExperience
from .marketing import Marketing

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_query = request.form.get('user_message')
    chatbot = Chatbot()
    chat_response = chatbot.generate_chat_response(user_query)
    return render_template('chat.html', chat_response=chat_response)

@app.route('/strain_info', methods=['GET', 'POST'])
def strain_info():
    user_query = request.form.get('user_message')
    strain_info = chatbot.get_strain_info(user_query)
    return render_template('strain_info.html', strain_info=strain_info)

@app.route('/marketing', methods=['GET', 'POST'])
def marketing():
    marketing = Marketing()
    marketing_opportunities = marketing.get_marketing_opportunities()
    return render_template('marketing.html', marketing_opportunities=marketing_opportunities)

if __name__ == "__main__":
    app.run(debug=True)
```