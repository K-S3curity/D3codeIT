import hashlib

#Encode to SHA256
def encode_sha256():
    text = str(input("Enter the text you want to hash in SHA256 format : "))
    result = hashlib.sha256(text.encode())
    print("The SHA256 hash is : ", result.hexdigest())

encode_sha256()