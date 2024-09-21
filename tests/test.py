from Server import Server
from Babel import Babel

def test_babel_translation():
    server1 = Server(name="Server1", language="English")
    server1.paid = True
    server1.addEvent("Hello, how are you?")

    babel = Babel()
    babel.addLanguageServer(server1)

    translated_message = babel.translateService("Hello, how are you?", "English", "Spanish")
    print(f"Translated Message: {translated_message}")

test_babel_translation()