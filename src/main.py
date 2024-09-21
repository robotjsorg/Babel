from Server import Server
from Babel import Babel
import sys
def main():
    server1 = Server(name="Server1", language="English")
    server1.paid = True
    server1.addEvent("Hello, how are you?")

    babel = Babel()
    babel.addLanguageServer(server1)

    translated_message = babel.translateService(input(str()), "English", "Spanish")
    print(f"Translated Message: {translated_message}")
    register(
)  

if __name__ == "__main__":
    main()