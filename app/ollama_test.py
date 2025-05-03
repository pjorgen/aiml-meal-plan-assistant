import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": "Say hello!",
        "stream": False
    }
)

print(response.json())
