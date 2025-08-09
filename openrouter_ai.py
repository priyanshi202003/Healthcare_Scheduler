import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4",
        "max_tokens": 200,  # ✅ Lower than 666 credits limit
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json=payload,
        headers=headers
    )

    data = response.json()

    # Handle API errors
    if "error" in data:
        print("Error from API:", data["error"])
        return f"[OpenRouter Error] {data['error']['message']}"

    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    test_prompt = "Write me a 2-sentence fun fact about space."
    response = generate_response(test_prompt)
    print("AI Response:", response)

