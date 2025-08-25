import string
import sys
import time
import logging
import random

logging.basicConfig(filename='caesar_cipher.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

MASTER_KEY = 69 
class CaesarCipher:
    def __init__(self, shift=0, use_master_key=False):
        self.shift = shift
        self.use_master_key = use_master_key
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + ' '
        self.alphabet_size = len(self.alphabet)
        logging.info(f"Initialized CaesarCipher with shift={shift}, use_master_key={use_master_key}")

    def _get_effective_shift(self):
        if self.use_master_key:
            return MASTER_KEY % self.alphabet_size
        return self.shift % self.alphabet_size

    def encrypt(self, text):
        shift = self._get_effective_shift()
        logging.debug(f"Encrypting text with shift {shift}")
        return self._transform(text, shift)

    def decrypt(self, text):
        shift = self._get_effective_shift()
        logging.debug(f"Decrypting text with shift {shift}")
        return self._transform(text, -shift)

    def _transform(self, text, shift):
        result = []
        for ch in text:
            if ch in self.alphabet:
                idx = self.alphabet.index(ch)
                new_idx = (idx + shift) % self.alphabet_size
                result.append(self.alphabet[new_idx])
            else:
                logging.warning(f"Character '{ch}' not in alphabet, adding unchanged.")
                result.append(ch)
        return ''.join(result)

def clear_screen():
    print("\n" * 50)

def display_menu():
    clear_screen()
    print("=== Caesar Cipher Tool with Master Key ===")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Brute Force Decrypt")
    print("4. Generate Random Key")
    print("5. Toggle Master Key (Currently {})".format("ON" if cipher.use_master_key else "OFF"))
    print("6. Help and About")
    print("0. Exit")

def main_loop():
    global cipher
    cipher = CaesarCipher()
    while True:
        display_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            plaintext = input("Enter text to encrypt: ")
            if not cipher.use_master_key:
                while True:
                    try:
                        shift = int(input("Enter shift key (integer): "))
                        break
                    except ValueError:
                        print("Invalid input, please enter an integer.")
                cipher.shift = shift
            encrypted = cipher.encrypt(plaintext)
            print(f"Encrypted text: {encrypted}")
            logging.info(f"Encrypted '{plaintext}' with shift {cipher._get_effective_shift()}")
            input("Press Enter to continue...")
        elif choice == "2":
            ciphertext = input("Enter text to decrypt: ")
            if not cipher.use_master_key:
                while True:
                    try:
                        shift = int(input("Enter shift key (integer): "))
                        break
                    except ValueError:
                        print("Invalid input, please enter an integer.")
                cipher.shift = shift
            decrypted = cipher.decrypt(ciphertext)
            print(f"Decrypted text: {decrypted}")
            logging.info(f"Decrypted '{ciphertext}' with shift {cipher._get_effective_shift()}")
            input("Press Enter to continue...")
        elif choice == "3":
            ciphertext = input("Enter cipher text for brute force: ")
            results = cipher.brute_force(ciphertext)
            print("Possible decryptions (shift: text):")
            for s, text in results:
                print(f"{s}: {text}")
            input("Press Enter to continue...")
        elif choice == "4":
            rand_shift = random.randint(1, cipher.alphabet_size - 1)
            print(f"Generated random shift key: {rand_shift}")
            input("Press Enter to continue...")
        elif choice == "5":
            cipher.use_master_key = not cipher.use_master_key
            state = "enabled" if cipher.use_master_key else "disabled"
            print(f"Master Key mode is now {state}. (Shift fixed to {MASTER_KEY})")
            logging.info(f"Master Key mode toggled {state}.")
            input("Press Enter to continue...")
        elif choice == "6":
            print("Caesar Cipher with Master Key.\nMaster Key = 69 overrides user shift key when enabled.\nUse toggle in menu option 5.")
            input("Press Enter to continue...")
        elif choice == "0":
            print("Exiting... goodbye!")
            logging.info("Program exited by user.")
            sys.exit()
        else:
            print("Invalid selection, please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_loop()
