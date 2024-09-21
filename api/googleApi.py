import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

def call_google_ai(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Write a story about a magic backpack.")
    print(response.text)