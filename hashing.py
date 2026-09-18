import hashlib

def messageHash(message):
    byteString = message.encode('utf-8')

    hashString = hashlib.sha256(byteString).hexdigest()

    return hashString

while __name__ == "__main__":
    message = input("hash enter your message. ")
    print(messageHash(message))