from random import randint
import pywhatkit
from sys import exit
rand_num = randint(0,3)

count = 10
def recurr_func(guesses=[],mynum=[]):
    global count

    while(count > 0): 
        if not guesses: #if no previous guesses are in the list
            user_guess = int(input("Please guess my number.\n It is from 0 to 9: "))
            compare_size(rand_num,user_guess)        
            turn = compare_nums(user_guess,rand_num)
            count -=1 
            guesses.append(user_guess)    
            mynum.append(rand_num)
            recurr_func(guesses,mynum) 

        else:
            user_guess = int(input("Try again.\n It is from 0 to 100: "))
            if user_guess in guesses:
                print("You guessed that number.")
                compare_size(rand_num,user_guess)
                count-=1
                recurr_func(guesses,mynum) 
            else:
                turn = compare_nums(user_guess,mynum[0])
                guesses.append(user_guess)
                count-=1
                print("count", count)
                recurr_func(guesses,mynum) 
        

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