```python
import requests
import json

gpt4_api_key = "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"

def generate_chat_response(user_query):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {gpt4_api_key}'
    }

    data = {
        'prompt': user_query,
        'max_tokens': 60
    }

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, data=json.dumps(data))
    response_json = response.json()

    chat_response = response_json['choices'][0]['text'].strip()

    return chat_response
```