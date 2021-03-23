import hashlib

#Encode to SHA224
def encode_sha224():
    text = str(input("Enter the text you want to hash in SHA224 format : "))
    result = hashlib.sha224(text.encode())
    print("The SHA224 hash is : ", result.hexdigest())

encode_sha224()