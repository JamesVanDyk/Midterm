def sendMessage(message, sharedKey, file):
    cypher = [ord(char) for char in message]
    
    encryptedMessage = []

    for char in cypher:
        encryptedMessage.append(char*sharedKey)
    
    encryptedFile = open(file, 'w')

    for char in encryptedMessage:
        encryptedFile.write(str(char) + " ")

    encryptedFile.close()

while __name__ == "__main__":
    message = input("write your message to send ")
    sendMessage(message)