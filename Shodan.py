import os
import shodan
import sys
from termcolor import colored
from time import sleep
from pyfiglet import figlet_format

# ASCII art
art = figlet_format("@ROXA")
art2 = figlet_format("Shodan Scanner")
print(colored(art, 'yellow'), colored(art2, 'blue'))


# själja koden
n_str = "@roxaaaa\n"
m_str = "a simple shodan scanner\n"
for char in n_str:
    #sys.stdout.write(char)

    sys.stdout.flush()
    sleep(0.1)
sys.stdout.write(colored(n_str, 'red'))
for tar in m_str:
    sys.stdout.flush()
    sleep(0.08)
sys.stdout.write(colored(m_str, 'green'))
print()
print()
print()

print(colored("[+] 1.shodan", 'red'))
question1 = input(colored("menu > ", 'blue')).lower()
for lists in range(20):

    if question1 == "shodan":
        print("{+} 1.webcams\n{+} 2.apache2\n{+} 3.windows\n{+} 4.coustom\n{+} 5.extended")
        question2 = input(colored("shodan > ", 'blue')).lower()
        if question2 == "1":
            command = os.system("shodan search webcam")
            print(colored(command, 'red'))
        elif question2 == "2":
            command = os.system("shodan search apache2")
            print(colored(command, 'blue'))
        elif question2 == "3":
            command = os.system("shodan search windows")
            print(colored(command, 'green'))
        elif question2 == "4":
            command = os.system("shodan search " + input("> "))
            print(colored(command, 'yellow'))
        elif question2 == "5":
            shodan_api_key = input("Skriv in ditt Shodan API key > ")
            api = shodan.Shodan(shodan_api_key)
            api = shodan.Shodan(shodan_api_key)
            print(shodan_api_key)
            try:
                print("authenticating shodan kay", "*" * 6)
                resultat = api.search(input("enter phrases > "))
                print(colored(resultat, 'aqua blue'))
            except shodan.APIError:
                k_str = "[-] incorrect API key!"
                print(colored(k_str, 'red'))
            finally:
                print("[+] command completed")
        elif question2 == "exit" or "quit":
            break
            quit()
        else:
            print("[-] Unknown error")
    else:
        print("[-] Unknown Error")
    print()
    print()
    print()

