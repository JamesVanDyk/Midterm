def readMessage(message, sharedKey):
    """
    mysteryFile = open(file, "r")
    mysteryMessage = mysteryFile.readlines()
    mysteryFile.close()

    encryptedMessage = mysteryMessage[0]
    secretKey = int(mysteryMessage[1])
    """
    messageChars = message.split()

    for item in range(len(messageChars)):
        messageChars[item] = int(messageChars[item]) // sharedKey
        messageChars[item] = chr(messageChars[item])
    
    decryptedMessage = "".join(messageChars)

    return decryptedMessage
    #decryptedFile = open("decryptedFile.txt", "w")
    #decryptedFile.write(decryptedMessage)
    
