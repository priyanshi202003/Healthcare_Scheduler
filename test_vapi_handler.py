# test_vapi_handler.py
from vapi_handler import handle_vapi_request

# Simulate VAPI sending a transcript
test_data = {
    "transcript": "Schedule appointment with Dr. Smith at 4 PM"
}

result = handle_vapi_request(test_data)

print("\n=== Test Output ===")
print("Generated Text:", result["text"])
print("Audio File:", result["audioUrl"])
