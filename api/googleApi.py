import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

def call_google_ai(prompt):
    response = genai.generate(prompt=prompt)
    return response