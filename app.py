from random import randrange
import random
import pywhatkit
import unittest

# Send whatsapp message
def sendMsg():
    pywhatkit.sendwhatmsg('+254799980846','wtf',21,38)

def getInput():
    return input("Enter a number range 1 to 100: ")

score = 100

x = random.randint(0,6)
correct = 7
r = randrange(8)
val = getInput()
print(type(int(val)))
# if(int(val) > x):
#     print("Value is greater than input val", int(val) - x)
#     print("Current score", score - 1)
# elif(int(val) < x):
#     print("Value is lesser than input by", int(val)-x)
#     print("Current score", score - 1)
# print(r)

