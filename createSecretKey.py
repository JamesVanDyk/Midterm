from sympy import randprime
from random import randint

def createKey():
    Prime = randprime(75, 200)
    Base = randint(3, 50)
    userOneK = randint(3, 500)
    userTwoK = randint(3, 500)
    
    userOneProduct = Base**userOneK%Prime
    userTwoProduct = Base**userTwoK%Prime
    userOneFinal = userTwoProduct**userOneK%Prime
    userTwoFinal = userOneProduct**userTwoK%Prime
    if userOneFinal == userTwoFinal:
        secretKey = userOneFinal
    else:
        raise Exception
    return secretKey