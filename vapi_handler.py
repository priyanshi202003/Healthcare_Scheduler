from openrouter_ai import generate_response
from google_tts import google_tts   # ✅ Use Google TTS
from n8n_trigger import trigger_n8n_action
import os
from dotenv import load_dotenv

load_dotenv()

VAPI_API_KEY = os.getenv("VAPI_API_KEY")

def handle_vapi_request(data):
    user_text = data.get("transcript", "")
    print("User said:", user_text)

    # Step 1: Generate AI response
    ai_response = generate_response(user_text)

    # Step 2: Optionally trigger workflow
    if "appointment" in user_text.lower():
        trigger_n8n_action(user_text)

    # Step 3: Convert response to audio (Google TTS returns local file path)
    audio_file_path = google_tts(ai_response)

    if audio_file_path:
        audio_url = f"/{audio_file_path}"  # assuming static hosting
    else:
        audio_url = None

    return {
        "text": ai_response,
        "audioUrl": audio_url
    }
