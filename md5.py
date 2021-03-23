import hashlib

#Encode to MD5
def encode_md5():
    text = str(input("Enter the text you want to hash in MD5 format : "))
    result = hashlib.md5(text.encode())
    print("The MD5 hash is : ", result.hexdigest())

encode_md5()