import os
from dotenv import load_dotenv
from api.api_handler import call_google_ai

load_dotenv()

def main():
    response = call_google_ai("Your prompt here")
    print(response)

if __name__ == "__main__":
    main()
