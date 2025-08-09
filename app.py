from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from vapi_handler import handle_vapi_request
from openrouter_ai import generate_response
from google_tts import google_tts as text_to_speech
from n8n_trigger import trigger_n8n_action
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Your HTML form

@app.route("/schedule-appointment", methods=["POST"])
def schedule_appointment():
    data = request.json
    doctor = data.get("doctor")
    description = data.get("description")
    time = data.get("time")

    if not doctor or not description or not time:
        return jsonify({"error": "Missing required fields"}), 400

    # Step 1 – Create AI response
    prompt = (
    f"You are a helpful healthcare assistant. "
    f"Confirm that the appointment with Dr. {doctor} for {description} at {time} "
    f"has been successfully scheduled. "
    "Respond ONLY with a brief, polite confirmation message. "
    "Do NOT mention any limitations or inability to schedule."
)

    ai_text = generate_response(prompt)

    # Step 2 – Send to n8n to add in Google Calendar
    n8n_message = f"Doctor: {doctor}, Description: {description}, Time: {time}"
    trigger_n8n_action(n8n_message)

    # Step 3 – Convert AI text to audio (Google TTS)
    audio_url = text_to_speech(ai_text)

    return jsonify({
        "status": "success",
        "message": ai_text,
        "audioUrl": audio_url
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
