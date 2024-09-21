from Server import Server
from Babel import Babel
from colorama import Fore, Style, init
from tabulate import tabulate

init()

def main():
    server1 = Server(name="ENG#0001", language="English")
    server1.paid = True
    server1.addEvent("Hello, how are you?")

    babel = Babel()
    babel.addLanguageServer(server1)

    user_input = input(Fore.YELLOW + "Enter a message to translate: " + Style.RESET_ALL)
    translated_message = babel.translateService(user_input, "English", "Spanish")

    print(Fore.GREEN + "Translated Message:" + Style.RESET_ALL)
    print(Fore.CYAN + f"{translated_message}" + Style.RESET_ALL)

    server_data = [[server.name, server.language, "Paid" if server.paid else "Unpaid"] for server in babel.languageServers]
    print(Fore.BLUE + "\nLanguage Servers:" + Style.RESET_ALL)
    print(tabulate(server_data, headers=["Server Name", "Language", "Payment Status"], tablefmt="pretty"))

if __name__ == "__main__":
    main()
