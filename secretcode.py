import sys
from colorama import Fore, Back, Style

text = ''
result = ''
key = ''
decrypt = ''

print(Fore.GREEN + "Python Encryption Program(PEP) V1.6 AJITH   /\(-<o>-)/\  <-- me  ")
decrypt = input(Fore.GREEN + "\n \nDo you want to encrypt or decrypt?\ntype 'e' to encrypt, 'd' to decrypt, or 'q' to quit:    ")


if decrypt == "e":
    text = input(Fore.GREEN + "\nEnter your message (no spaces, use '_'):     ")


    for m in range(0, len(text)):
            result = result + chr(ord(text[m]) - 3)


    print(Fore.YELLOW + "\nYour encrypted message is: " + result)



if decrypt == "d":
    text = input(Fore.GREEN + "\nEnter your encrypted message:     ")


    for m in range(0, len(text)):
            result = result + chr(ord(text[m]) + 3)


    print(Fore.YELLOW + "\nYour decrypted message is: " + result)


if decrypt == "q":
    sys.exit(0)
