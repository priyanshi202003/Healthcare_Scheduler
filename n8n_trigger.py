import os
import requests
from dotenv import load_dotenv

load_dotenv()

def trigger_n8n_action(data):
    n8n_url = os.getenv("N8N_WEBHOOK_URL")

    response = requests.post(n8n_url, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    return response.status_code == 200


