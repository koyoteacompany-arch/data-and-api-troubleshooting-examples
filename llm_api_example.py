import requests

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "your_api_key_here"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Write a SQL query to calculate revenue by department"}
    ]
}

response = requests.post(API_URL, headers=headers, json=data)

print(response.json())
