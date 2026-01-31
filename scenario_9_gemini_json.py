import json
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config={"response_mime_type": "application/json"}
)
response = model.generate_content(
    "List 3 benefits of Python for data science."
)
try:
    data = json.loads(response.text)
except json.JSONDecodeError:
    data = {
        "error": "Invalid JSON response",
        "raw_response": response.text
    }
print(data)
