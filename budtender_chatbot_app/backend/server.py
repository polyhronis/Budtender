```python
from flask import Flask, request, jsonify
from strain_api import fetchStrainData
from gpt4_integration import processUserInput, generateRecommendations

app = Flask(__name__)

userPreferences = {}
strainData = {}
recommendations = []

@app.route('/api/chat', methods=['POST'])
def chat():
    userMessage = request.json['UserMessage']
    userPreferences.update(processUserInput(userMessage))
    strainData.update(fetchStrainData(userPreferences))
    recommendations = generateRecommendations(userPreferences, strainData)
    botMessage = {
        'BotMessage': 'Here are some recommendations based on your preferences.',
        'Recommendations': recommendations
    }
    return jsonify(botMessage)

@app.route('/api/voice', methods=['POST'])
def voice():
    # This function will be implemented in the voice_libraries.py file
    pass

if __name__ == '__main__':
    app.run(debug=True)
```