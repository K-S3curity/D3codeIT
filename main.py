#!/usr/bin/python
import base64
import hashlib
import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Base64~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------Functions----------------------
#Encode in Base64
def choice_one():
    string = input("Enter your text :")
    str_ascii = string.encode('ascii')
    b64_encoded = base64.b64encode(str_ascii)
    result = b64_encoded.decode('ascii')
    print("The Base64 string is : ")
    print(result)
#Decode Base64
def choice_two():
    string = input("Enter the your Base64 string : ")
    b64_decoded = base64.b64decode(string)
    result = b64_decoded.decode('ascii')
    print("The decoded Base64 string is : ")
    print(result)

def invalid():
    print("Invalid Choice !")
    print("Type 1 to encode a string to Base64")
    print("Type 2 to decode a Base64 string")

def base64_menu() :
    print("1 - Encode a string to Base64")
    print("2 - Decode a Base64 string")
    choice_base64 = int(input("Type 1 /2 =>  "))
    if choice_base64 == 1:
        choice_one()
    if choice_base64 == 2:
        choice_two()
    while choice_base64 == 0 or choice >= 3 :
        invalid()
        choice_base64

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Base32~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------Functions----------------------
#Encode in Base64
def choice_one_32():
    string = input("Enter your text : ")
    str_ascii = string.encode('ascii')
    b32_encoded = base64.b32encode(str_ascii)
    result = b32_encoded.decode('ascii')
    print("The Base32 string is : ")
    print(result)
#Decode Base64
def choice_two_32():
    string = input("Enter the your Base32 string : ")
    b32_decoded = base64.b32decode(string)
    result = b32_decoded.decode('ascii')
    print("The decoded Base32 string is : ")
    print(result)

def invalid_32():
    print("Invalid Choice !")
    print("Type 1 to encode a string to Base32")
    print("Type 2 to decode a Base32 string")

def base32_menu() :
    print("1 - Encode a string to Base32")
    print("2 - Decode a Base32 string")
    choice_base32 = int(input("Type 1 /2 =>  "))
    if choice_base32 == 1:
        choice_one_32()
    if choice_base32 == 2:
        choice_two_32()
    while choice_base32 == 0 or choice_base32 >= 3 :
        invalid_32()
        choice_base32



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Encode to SHA1
def encode_sha1():
    text = str(input("Enter the text you want to hash in SHA1 format : "))
    result = hashlib.sha1(text.encode())
    print("The SHA1 hash is : ")
    print(result.hexdigest())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA256~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to SHA256
def encode_sha256():
    text = str(input("Enter the text you want to hash in SHA256 format : "))
    result = hashlib.sha256(text.encode())
    print("The SHA256 hash is : ")
    print(result.hexdigest())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA512~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to SHA256
def encode_sha512():
    text = str(input("Enter the text you want to hash in SHA512 format : "))
    result = hashlib.sha512(text.encode())
    print("The SHA512 hash is : ")
    print(result.hexdigest())
    
#----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Script--------------------------------------------------------


#Clear the interpreter
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')
clear_console()
print('''

8888888b.   .d8888b.                        888         8888888 88888888888 
888  "Y88b d88P  Y88b                       888           888       888     
888    888      .d88P                       888           888       888     
888    888     8888"   .d8888b .d88b.   .d88888  .d88b.   888       888     
888    888      "Y8b. d88P"   d88""88b d88" 888 d8P  Y8b  888       888     
888    888 888    888 888     888  888 888  888 88888888  888       888     
888  .d88P Y88b  d88P Y88b.   Y88..88P Y88b 888 Y8b.      888       888     
8888888P"   "Y8888P"   "Y8888P "Y88P"   "Y88888  "Y8888 8888888     888     
                                                                            
                                                                            
                                                                            
                                                                   
                                                                              
''')
#Say Hi
print("Hi !")
#Choose encoding mode
def menu() :
    print("1 - Base64 Encode/Decode")
    print("2 - Base32 Encode/Decode")
    print("3 - SHA1 Encode")
    print("4 - SHA256 Encode")
    print("5 - SHA512 Encode")

menu()
choice = int(input("Type 1 / 2 / 3 / 4 / 5 =>  "))

if choice == 1:
    base64_menu()
if choice == 2:
    base32_menu()
if choice == 3:
    encode_sha1()
if choice == 4:
    encode_sha256()
if choice == 5:
    encode_sha512()
while choice == 0 or choice >= 6:
    print("Invalid choice !")
    menu()
    choice = int(input("Type 1 / 2 / 3 / 4 / 5 =>  "))
