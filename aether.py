import requests
import time
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

def get_wikipedia_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('extract', "No summary available.")
    else:
        return "Sorry, I couldn't find that topic."

def futuristic_banner():
    banner = pyfiglet.figlet_format("AETHER")
    print(Fore.CYAN + banner)
    print(Fore.MAGENTA + "Your futuristic AI assistant\n")
    time.sleep(1)

if __name__ == "__main__":
    futuristic_banner()
    while True:
        user_input = input(Fore.YELLOW + "Ask Aether about anything: ")
        if user_input.lower() in ["quit", "exit"]:
            print(Fore.RED + "Shutting down Aether... Goodbye!")
            break
        print(Fore.GREEN + "\nAether says:\n")
        print(Fore.CYAN + get_wikipedia_summary(user_input))
        print(Style.RESET_ALL + "\n---\n")
