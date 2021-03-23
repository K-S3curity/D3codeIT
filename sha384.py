import hashlib

#Encode to SHA384
def encode_sha384():
    text = str(input("Enter the text you want to hash in SHA384 format : "))
    result = hashlib.sha384(text.encode())
    print("The SHA384 hash is : ", result.hexdigest())

encode_sha384()