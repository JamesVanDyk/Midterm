from hashing import messageHash
from encryption import sendMessage
from decryption import readMessage




def createSignature(message, sharedKey):
     
    hashMessage = messageHash(message)

    encryptedMessage = sendMessage(hashMessage, sharedKey)

    signatureFile = open("signatureFile.txt", "w")
    signatureFile.write(encryptedMessage)
    signatureFile.write("\n" + str(sharedKey))
    signatureFile.close()

    dataFile = open("dataFile.txt", "w")
    dataFile.write(message)
    dataFile.close()


def receiveSignature():
    signatureFile = open("signatureFile.txt", "r")
    receivedSignature = signatureFile.readlines()
    signatureFile.close()

    dataFile = open("dataFile.txt", "r")
    receivedData = dataFile.read()
    dataFile.close()
    dataHashed = messageHash(receivedData)

    signatureHash = readMessage(receivedSignature[0], int(receivedSignature[1]))

    if dataHashed == signatureHash:
        print("data verified.")
    else:
        print("Error. Data and signature doesn't match.")


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