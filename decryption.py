def readMessage():
    mysteryFile = open("encryptedFile.txt", "r")
    mysteryMessage = mysteryFile.readlines()
    mysteryFile.close()

    encryptedMessage = mysteryMessage[0]
    secretKey = int(mysteryMessage[1])

    messageChars = encryptedMessage.split()

    for item in range(len(messageChars)):
        messageChars[item] = int(messageChars[item]) // secretKey
        messageChars[item] = chr(messageChars[item])
    
    decryptedMessage = "".join(messageChars)
    
    decryptedFile = open("decryptedFile.txt", "w")
    decryptedFile.write(decryptedMessage)
    
readMessage()