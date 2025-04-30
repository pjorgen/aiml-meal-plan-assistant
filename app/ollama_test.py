import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:1b",
        "prompt": "Explain quantum entanglement.",
        "stream": False
    }
)

print(response.json())
