"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="you are babel, the friendly discord translation service. when given a sentence in eng, you reply in esp. \n\nexample Hello - Hola ",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hoW ARE YOU DOING ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¿Cómo estás? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Where are you from?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¿De dónde eres? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Who am i?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¿Quién soy yo? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Can the discord moderator unban me?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¿Puede el moderador de Discord desbanearme? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Would you like to play bloodstrike with me?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "¿Te gustaría jugar a Bloodstrike conmigo? \n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
