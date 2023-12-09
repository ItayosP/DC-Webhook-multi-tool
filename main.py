import time
import requests
import os
import sys
from pystyle import Colors, Colorate

# Colors for terminal output
cyan = "\033[0;36m"
light_white = "\033[1;37m"

def clear_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def show_menu():
    return f"""
                    [1] Delete Webhook
                    [2] Spam Messages
                    [3] Ping everyone
"""

def main():
    clear_terminal()

    logo = f"""
    Made By:
                                    ______                         ____ 
                                   /  _/ /_____ ___  ______  _____/ __ 
                                   / // __/ __ `/ / / / __ \/ ___/ /_/ /
                                 _/ // /_/ /_/ / /_/ / /_/ (__  ) ____/ 
                                /___/\__/\__,_/\__, /\____/____/_/      
                                          /____/                    
                                >> [Webhook Multitool]
                                > [github.com/ItayosP]
                                > [discord: itayos69]
    """


    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))
    
    webhook = input(f"{cyan}[>]{light_white} URL: ")

    while True:
        print(Colorate.Horizontal(Colors.cyan_to_blue, show_menu(), 1))
        option = int(input(f"{cyan}[>]{light_white} Choose an option (0 to exit): "))

        if option == 0:
            break

        if option == 1:
            requests.delete(webhook)
            print(f"{cyan}Deleted webhook{light_white}")
            break

        elif option == 2:
                spam_custom_message = input(f"{cyan}[>]{light_white} Custom message: ")
                data = {'content': spam_custom_message}
                while (True):
                    time.sleep(0.1)
                    requests.post(webhook, data=data)

        elif option == 3:
            while True:
                data = {'content': "@everyone"}
                requests.post(webhook, data=data)

if __name__ == "__main__":
    main()
