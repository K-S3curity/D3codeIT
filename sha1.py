import hashlib

#Encode to SHA1
def encode_sha1():
    text = str(input("Enter the text you want to encode to SHA1 : "))
    result = hashlib.sha1(text.encode())
    print("The SHA1 string is : ", result.hexdigest())

encode_sha1()
