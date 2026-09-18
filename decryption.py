def readMessage(message, sharedKey):
    messageChars = message.split()

    for item in range(len(messageChars)):
        messageChars[item] = int(messageChars[item]) // sharedKey
        messageChars[item] = chr(messageChars[item])
    
    decryptedMessage = "".join(messageChars)

    return decryptedMessage