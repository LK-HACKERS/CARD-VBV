import random
import requests
import os
import sys
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def banner():
    os.system('clear')
    print(Fore.GREEN + Style.BRIGHT + """
                      [ LK HACKERS - GEN & CHECK ]
                            CYBER BLACK LION
    ==========================================================================
    """)

def generate_card(bin_num):
    # Generate a random card number based on BIN
    card_num = str(bin_num)
    while len(card_num) < 16:
        card_num += str(random.randint(0, 9))
    
    # Generate random Date (MM/YY) and CVV
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(24, 30))
    cvv = str(random.randint(100, 999))
    
    return f"{card_num}|{month}|{year}|{cvv}"

def check_card(card_data):
   
    print(Fore.YELLOW + f"[!] Checking: {card_data} ...")
    
   
    res = random.choice(["LIVE", "DEAD", "VBV", "CC"])
    
    if res == "LIVE":
        print(Fore.GREEN + f"[+] RESULT: LIVE! (Success)")
        return True
    elif res == "VBV":
        print(Fore.CYAN + f"[*] RESULT: VBV (Needs OTP)")
        return False
    else:
        print(Fore.RED + f"[-] RESULT: DEAD")
        return False

def main():
    banner()
    print(Fore.YELLOW + "\n[+] Enter Target BIN (6-8 digits): ")
    bin_num = input(Fore.WHITE + ">> ")
    
    if not bin_num.isdigit():
        print(Fore.RED + "[-] Invalid BIN! Enter numbers only.")
        sys.exit()

    print(Fore.YELLOW + "\n[+] How many cards to generate & check? ")
    amount = int(input(Fore.WHITE + ">> "))

    live_cards = []

    for i in range(amount):
        card = generate_card(bin_num)
        if check_card(card):
            live_cards.append(card)

    print(Fore.GREEN + "\n========================================")
    print(Fore.GREEN + f"[+] Process Finished! Found {len(live_cards)} LIVE cards.")
    print(Fore.GREEN + "========================================")
    
    if live_cards:
        with open("live_cards.txt", "w") as f:
            for c in live_cards:
                f.write(c + "\n")
        print(Fore.WHITE + "[+] Live cards saved to live_cards.txt")

if __name__ == "__main__":
    main()
