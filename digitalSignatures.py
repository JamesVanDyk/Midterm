from hashing import messageHash
from encryption import sendMessage
from decryption import readMessage




def createSignature(message, sharedKey):
     
    hashMessage = messageHash(message)

    sendMessage(hashMessage, sharedKey, "encryptedFile.txt")

    encryptedFile = open("encryptedFile.txt", "r")
    encryptedMessage = encryptedFile.read()
    
    signatureFile = open("signatureFile.txt", "w")
    signatureFile.write(encryptedMessage)
    signatureFile.close()

    #dataFile = open("dataFile.txt", "w")
    #dataFile.write(message)
    #dataFile.close()


def receiveSignature(sharedKey):
    signatureFile = open("signatureFile.txt", "r")
    receivedSignature = signatureFile.read()
    signatureFile.close()

    dataFile = open("public.txt", "r")
    receivedData = dataFile.read()
    dataFile.close()
    dataHashed = messageHash(receivedData)

    signatureHash = readMessage(receivedSignature, sharedKey)

    if dataHashed == signatureHash:
        return True
    else:
        return False


while __name__ == "__main__":
    sendOrReceive = input("send or receive signature? (s or r) ")
    userNum = input("User 1 or 2? (enter only the number) ")

    if sendOrReceive == "s": 
        message = input("please enter your message. ")    
        createSignature(message, 3)
    elif sendOrReceive == "r":
        receiveSignature(userNum)
    else:
        print("Invalid input.\nTry again.")