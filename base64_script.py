import base64

#-------------------------------------------------------Functions-------------------------------------------------------
#Encode in Base64
def choice1():
    string = input("Enter the your text :")
    str_ascii = string.encode('ascii')
    b64_encoded = base64.b64encode(str_ascii)
    result = b64_encoded.decode('ascii')
    print("The Base64 string is :")
    print(result)
#Decode Base64
def choice2():
    string = input("Enter the your Base64 string :")
    b64_decoded = base64.b64decode(string)
    result = b64_decoded.decode('ascii')
    print("The decoded Base64 string is :")
    print(result)

def invalid():
    print("Invalid Choice !")
    print("Type 1 to encode a string to Base64")
    print("Type 2 to decode a Base64 string")

#--------------------------------------------------------Script--------------------------------------------------------
#Say Hi
print("Hi !")
#Type 1 or 2
print("Type 1 to encode a string to Base64")
print("Type 2 to decode a Base64 string")

choice = int(input("1 / 2 =>  "))

if choice == 1:
    choice1()
if choice == 2:
    choice2()
while choice == 0 or choice >= 3 :
    invalid()
    int(input("1 / 2 =>  "))
