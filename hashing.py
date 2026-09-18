import hashlib

def messageHash(message):
    byteString = message.encode('utf-8')

    hashString = hashlib.sha256(byteString).hexdigest()

    return hashString