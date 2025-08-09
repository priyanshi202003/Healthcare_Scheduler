# google_tts.py
from gtts import gTTS
import os
import uuid

def google_tts(text, lang="en"):
    try:
        # Generate a unique filename
        filename = f"tts_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join("static", filename)

        # Create static folder if not exists
        os.makedirs("static", exist_ok=True)

        # Generate speech
        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)

        print(f"[gTTS] Audio saved to {filepath}")
        return filepath
    except Exception as e:
        print(f"[gTTS Error] {e}")
        return None
