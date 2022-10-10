from art import *
import base64 as b64
import binascii
import codecs
import sys
# Program to decrypt various basic ciphers
# It's a messy program, but oh well!

# Dictionary for morse_code function
morse_code_dict = { 
        'A':'.-',     'B':'-...',   'C':'-.-.',   'D':'-..',    'E':'.', 
        'F':'..-.',   'G':'--.',    'H':'....',   'I':'..',     'J':'.---', 
        'K':'-.-',    'L':'.-..',   'M':'--',     'N':'-.',     'O':'---', 
        'P':'.--.',   'Q':'--.-',   'R':'.-.',    'S':'...',    'T':'-', 
        'U':'..-',    'V':'...-',   'W':'.--',    'X':'-..-',   'Y':'-.--', 
        'Z':'--..',   '1':'.----',  '2':'..---',  '3':'...--',  '4':'....-', 
        '5':'.....',  '6':'-....',  '7':'--...',  '8':'---..',  '9':'----.', 
        '0':'-----',  ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
        '-':'-....-', '(':'-.--.',  ')':'-.--.-' }

# Dictionary for atbash function
atbash_dict = {
        'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 
        'Z' : 'A' }

# Main (initial) function
def main():
    # Prints to terminal in ASCII
    tprint("Crypto Decrypto")
    
    # Eternal loop. Ends with input '7'
    while(1):
        print("\nReview the options below:")
        print(
            '1. Decrypt binary\n'
            '2. Decrypt hexadecimal\n'
            '3. Decrypt base64\n'
            '4. Decrypt ROT-13\n'
            '5. Decrypt atbash\n'
            '6. Decrypt morse code\n'
            '7. Quit\n' )
        option = input("Enter an option by number: ")
        
        if option == '7':
            # Exits basic_crypto_decrypto.py program
            sys.exit()
        
        hash_input = input("Enter a hash to decrypt: ")
        
        # Calls function depending on which option was input
        if option == '1':
            binary(hash_input)

        elif option == '2':
            hexadecimal(hash_input)

        elif option == '3':
            base64(hash_input)

        elif option == '4':
            rot_13(hash_input)

        elif option == '5':
            atbash(hash_input)

        elif option == '6':
            morse_code(hash_input)

        else:
            print("The option entered is not valid. Try again.\n")

# Decrypts morse code
def morse_code(morse_code_input):
    text = ''
    morse_code_input += ' '
    cipher = ''
    
    for x in morse_code_input:
        # Morse code often contains '/' for the purpose of being a separator and not valid morse
        # This skips the character '/'
        if x == '/':
            continue
        
        # When there is a space, resets i (new word)
        if x != ' ':
            i = 0
            cipher += x
        
        # If it is a character, it proceeds to decrypt based on morse_code_dict keys and values
        else:
            i += 1
            
            if i == 2:
                text += ' '
                
            else:
                text += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(cipher)]
                cipher = ''
                
    print(text + '\n')

# Decrypts atbash
def atbash(atbash_input):
    text = ''
    # Converts text to uppercase to match atbash_dictionary (I'm lazy)
    atbash_input = atbash_input.upper()
    
    # Decrypts based on keys and values in atbash_dictionary
    for x in atbash_input:
        if(x != ' '):
            text += atbash_dict[x]
        else:
            text += ' '
            
    print(text + '\n')

# Decrypts ROT-13
def rot_13(rot_13_input):
    # Uses codecs module to decrypt ROT-13 
    text = codecs.encode(rot_13_input, 'rot_13')
    print(text + '\n')

# Decrypts base64
def base64(b64_input):
    # Uses base64 module to decrypt base64
    b64_bytes = b64_input.encode('ascii')
    input_bytes = b64.b64decode(b64_bytes)
    text = input_bytes.decode('ascii')
    print(text + '\n')

# Decrypts hexadecimal
def hexadecimal(hex_input):
    # Uses bytes to decrypt hexadecimal
    hex_bytes = bytes.fromhex(hex_input)
    text = hex_bytes.decode("ASCII")
    print(text + '\n')

# Decrypts binary
def binary(binary_input):
    # Uses binascii module to decrypt binary
    text = binascii.b2a_uu(binary_input)
    print(text + '\n')

# Calls main 
if __name__ == "__main__":
    main()

