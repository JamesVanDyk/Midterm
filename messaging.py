from createSecretKey import createKey
from digitalSignatures import createSignature, receiveSignature
from encryption import sendMessage
from decryption import readMessage

def writeToOne():
    publicFile = open("public.txt", "r")
    encryptedText = publicFile.read()
    publicFile.close()

    userOneFile = open("userOne.txt", "w")
    userOneFile.write(readMessage(encryptedText, secretKey))
    userOneFile.close()
    return

def writeToTwo():
    publicFile = open("public.txt", "r")
    encryptedText = publicFile.read()
    publicFile.close()
    
    userTwoFile = open("userTwo.txt", "w")
    userTwoFile.write(readMessage(encryptedText, secretKey))
    userTwoFile.close()
    return

while __name__ == "__main__":
    #get messager info, message and encrypt it
    userNum = input("User 1 or 2? (enter only the number) ")
    secretKey = createKey()
    message = input("please enter your message. ")
    sendMessage(message, secretKey, "public.txt")

    #create the signature
    encryptedFile = open("public.txt", "r")
    encryptedMessage = encryptedFile.read()
    createSignature(encryptedMessage, secretKey)

    #verify the signature
    verified = receiveSignature(secretKey)
    if verified:
        if userNum == "1":
            writeToTwo()
        elif userNum == "2":
            writeToOne()
    else:
        print("message failed to send.")
    continue