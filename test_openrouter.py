import requests
import json

# Your OpenRouter API key
OPENROUTER_API_KEY = "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"

# Function to test OpenRouter API
def test_openrouter():
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",  # You can change to your preferred model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, can you tell me a joke?"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        print("✅ Response from OpenRouter:")
        print(json.dumps(result, indent=2))
        print("\nAssistant:", result["choices"][0]["message"]["content"])
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
    except KeyError:
        print("⚠️ Unexpected response format:", response.text)


if __name__ == "__main__":
    test_openrouter()
