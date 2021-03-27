#!/usr/bin/python
import base64
import hashlib
import os
import bcrypt
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Base85~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------Functions----------------------
#Encode in Base85
def choice_one_85():
    string = input("Enter your text : ")
    str_ascii = string.encode('ascii')
    b85_encoded = base64.b85encode(str_ascii)
    result = b85_encoded.decode('ascii')
    print("The Base85 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))
#Decode Base85
def choice_two_85():
    string = input("Enter the your Base85 string : ")
    b85_decoded = base64.b85decode(string)
    result = b85_decoded.decode('ascii')
    print("The decoded Base85 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))

def invalid():
    print("Invalid Choice !")
    print("Type 1 to encode a string to Base85")
    print("Type 2 to decode a Base85 string")

def base85_menu() :
    print("1 - Encode a string to Base85")
    print("2 - Decode a Base85 string")
    choice_base85 = int(input("Type 1 /2 =>  "))
    if choice_base85 == 1:
        choice_one_85()
    if choice_base85 == 2:
        choice_two_85()
    while choice_base85 == 0 or choice_base85 >= 3 :
        invalid()
        choice_base85

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Base64~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------Functions----------------------
#Encode in Base64
def choice_one():
    string = input("Enter your text : ")
    str_ascii = string.encode('ascii')
    b64_encoded = base64.b64encode(str_ascii)
    result = b64_encoded.decode('ascii')
    print("The Base64 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))
#Decode Base64
def choice_two():
    string = input("Enter the your Base64 string : ")
    b64_decoded = base64.b64decode(string)
    result = b64_decoded.decode('ascii')
    print("The decoded Base64 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))

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
    print("The Base32 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))
#Decode Base64
def choice_two_32():
    string = input("Enter the your Base32 string : ")
    b32_decoded = base64.b32decode(string)
    result = b32_decoded.decode('ascii')
    print("The decoded Base32 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))

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
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Base16~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------Functions----------------------
#Encode in Base16
def choice_one_16():
    string = input("Enter your text : ")
    str_ascii = string.encode('ascii')
    b16_encoded = base64.b16encode(str_ascii)
    result = b16_encoded.decode('ascii')
    print("The Base16 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))
#Decode Base16
def choice_two_16():
    string = input("Enter the your Base16 string : ")
    b16_decoded = base64.b16decode(string)
    result = b16_decoded.decode('ascii')
    print("The decoded Base16 string is : ", result)
    choice = int(input("Type a number from the list above =>  "))

def invalid_16():
    print("Invalid Choice !")
    print("Type 1 to encode a string to Base16")
    print("Type 2 to decode a Base16 string")

def base16_menu() :
    print("1 - Encode a string to Base16")
    print("2 - Decode a Base16 string")
    choice_base16 = int(input("Type 1 /2 =>  "))
    if choice_base16 == 1:
        choice_one_16()
    if choice_base16 == 2:
        choice_two_16()
    while choice_base16 == 0 or choice_base16 >= 3 :
        invalid_16()
        choice_base16
    choice = int(input("Type a number from the list above =>  "))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Encode to SHA1
def encode_sha1():
    text = str(input("Enter the text you want to hash in SHA1 format : "))
    result = hashlib.sha1(text.encode())
    print("The SHA1 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA224~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Encode to SHA224
def encode_sha224():
    text = str(input("Enter the text you want to hash in SHA224 format : "))
    result = hashlib.sha224(text.encode())
    print("The SHA224 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA256~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to SHA256
def encode_sha256():
    text = str(input("Enter the text you want to hash in SHA256 format : "))
    result = hashlib.sha256(text.encode())
    print("The SHA256 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA384~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Encode to SHA384
def encode_sha384():
    text = str(input("Enter the text you want to hash in SHA384 format : "))
    result = hashlib.sha384(text.encode())
    print("The SHA384 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHA512~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to SHA256
def encode_sha512():
    text = str(input("Enter the text you want to hash in SHA512 format : "))
    result = hashlib.sha512(text.encode())
    print("The SHA512 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MD5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to MD5
def encode_md5():
    text = str(input("Enter the text you want to hash in MD5 format : "))
    result = hashlib.md5(text.encode())
    print("The MD5 hash is : ", result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MD5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Encode to Bcrypt
def encode_bcrypt():
    text = str(input("Enter the text you want to hash in Bcrypt format : "))
    str_ascii = text.encode('ascii')
    result = bcrypt.hashpw(str_ascii, bcrypt.gensalt())
    print("The Bcrypt hash is : ", result)
    choice = int(input("Type a number from the list above =>  "))
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
    print("1 - Base85 Encode/Decode")
    print("2 - Base64 Encode/Decode")
    print("3 - Base32 Encode/Decode")
    print("4 - Base16 Encode/Decode")
    print("5 - SHA1 Encode")
    print("6 - SHA224 Encode")
    print("7 - SHA256 Encode")
    print("8 - SHA384 Encode")
    print("9 - SHA512 Encode")
    print("10 - MD5 Encode")
    print("11 - Bcrypt Encode")

menu()
choice = int(input("Type a number from the list above =>  "))

if choice == 1:
    base85_menu()
elif choice == 2:
    base64_menu()
elif choice == 3:
    base32_menu()
elif choice == 4:
    base16_menu()
elif choice == 5:
    encode_sha1()
elif choice == 6:
    encode_sha224()
elif choice == 7:
    encode_sha256()
elif choice == 8:
    encode_sha384()
elif choice == 9:
    encode_sha512()
elif choice == 10:
    encode_md5()
elif choice == 11:
    encode_bcrypt()

else :
    print("Invalid choice !")
    menu()
    choice = int(input("Type a number from the list above =>  "))
