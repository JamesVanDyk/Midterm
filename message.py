from createSecretKey import createKey
#from digitalSignatures import createSignature, receiveSignature
from encryption import sendMessage

def writeToOne(input):
    return

def writeToTwo(input):
    return


while __name__ == "__main__":
    userNum = input("User 1 or 2? (enter only the number) ")
    secretKey = createKey()
    message = input("please enter your message. ")
    sendMessage(message, secretKey)
    continue