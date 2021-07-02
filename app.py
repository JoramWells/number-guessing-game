from random import randrange
import random

score = 100

x = random.randint(0,6)
correct = 7
r = randrange(8)
val = input("Enter your a number: ")
if(int(val) > x):
    print("Value is greater than input val", int(val) - x)
    print("Current score", score - 1)
elif(int(val) < x):
    print("Value is lesser than input by", int(val)-x)
    print("Current score", score - 1)

# def week(x):
#     switcher={
#         0:"Monday",
#         1:"Tuesday",
#         2:"Wednesday",
#         3:"Thursday",
#         4:"Friday",
#         5:"Sartuday",
#         6:"Sunday"

#     }
#     return switcher.get(x,"Invalid input")

# print(week(x))
print(r)