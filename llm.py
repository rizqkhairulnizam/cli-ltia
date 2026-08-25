import requests
import json
from config import LLM_URL

def ask_llm(prompt):
    response = requests.post(
        LLM_URL,
        json={
            "model": "local",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": True
        },
        stream=True
    )

    response.raise_for_status()

    for line in response.iter_lines():
        if not line:
            continue

        line = line.decode("utf-8")

        if line.startswith("data: "):
            line = line[6:]

        if line == "[DONE]":
            break

        data = json.loads(line)

        token = data["choices"][0]["delta"].get("content")

        if token:
            print(token, end="", flush=True)

    print()






