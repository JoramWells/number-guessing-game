from random import randint
import pywhatkit
from sys import exit
import compare_nums
rand_num = randint(0,99)

count = 10

def recurr_func(guesses=[],num=[]):
    # Declare count as global
    global count

    while(count > 0): 
        if not guesses: #if no previous guesses are in the list
            user_guess = int(input("Please guess another number.\nRange(0,99)\n"))
            compare_size(rand_num,user_guess)        
            turn = compare_nums(user_guess,rand_num)
            count -=1 
            print("You have", count ," more chances to go")
            guesses.append(user_guess)    
            num.append(rand_num)
            recurr_func(guesses,num) 

        else:
            user_guess = int(input("Try again.\nRange(0,99)\n "))
            if user_guess in guesses:
                print("Please guess another number.")
                compare_size(rand_num,user_guess)
                count-=1
                print("You have", count ," more chances to go")
                recurr_func(guesses,num) 
            else:
                turn = compare_nums(user_guess,num[0])
                guesses.append(user_guess)
                count-=1
                print("You have", count ," to go")
                recurr_func(guesses,num) 
        

def compare_nums(your_guess,my_num):
    if your_guess == my_num:
        send_msg()
        exit()
    else:
        return
def compare_size(rand,guess):
    if(rand > guess):
        print("Value is less by: ", rand - guess)
    elif(rand<guess):
        print("Value more by: ", guess - rand)
    else:
        return


# Send whatsapp message
def send_msg():
    pywhatkit.sendwhatmsg('+254799980846','wtf',22,56)


recurr_func()