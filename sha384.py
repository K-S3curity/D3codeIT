import hashlib

#Encode to SHA384
def encode_sha384():
    text = str(input("Enter the text you want to hash in SHA384 format : "))
    result = hashlib.sha384(text.encode())
    print("The SHA384 hash is : ")
    print(result.hexdigest())
    choice = int(input("Type a number from the list above =>  "))

encode_sha384()