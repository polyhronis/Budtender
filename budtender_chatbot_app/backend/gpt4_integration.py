```python
import openai
import json

openai.api_key = 'your-api-key'

def processUserInput(userInput):
    userPreferences = {}

    # Use GPT-4 to process user's input and update userPreferences
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=userInput,
        temperature=0.5,
        max_tokens=100
    )

    # Parse the response and update userPreferences
    response_data = json.loads(response.choices[0].text.strip())
    userPreferences.update(response_data)

    return userPreferences

def sendBotMessage(userPreferences):
    # Use GPT-4 to generate bot's message based on userPreferences
    prompt = json.dumps(userPreferences)
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    # Parse the response and return bot's message
    botMessage = response.choices[0].text.strip()
    return botMessage
```