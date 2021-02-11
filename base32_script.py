import base64

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
