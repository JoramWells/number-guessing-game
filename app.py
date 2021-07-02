from random import randrange
import random
import pywhatkit
import unittest

# Correct input value
correct = 7

# Total score
score = 100

# Generate input value from 0 to 99
x = random.randint(0,99)


# Send whatsapp message
def send_msg():
    pywhatkit.sendwhatmsg('+254799980846','wtf',21,38)


# Get input from user
def get_input(): 
    try:
        val = input("Enter a number range 1 to 100: ")
        return val
    except Exception as e:
        return e

val = int(get_input())
print(type(int(val)))

def calc_value(num):
    if(int(val) > num):
        print("Value is greater than input val by", int(val) - num)
        print("Current score", score - 1)
        return int(val)-num
    elif(int(val) < num):
        print("Value is lesser than input by", int(val)-num)
        print("Current score", score - 1)
        return  int(val)-num
print(calc_value(x))

