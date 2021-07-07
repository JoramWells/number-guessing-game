import tkinter as tk
import random
import pywhatkit
import datetime

window = tk.Tk()

# Set the dimensions of the created window
window.geometry("750x550")

# Set the background color of the window
window.config(bg="#36454f")

window.resizable(width=True,height=True)

window.title('Guessing Game')

# The code for the buttons and text and other 
# interactive UI elements go here 

TARGET = random.randint(0, 1000)
count = 10


def update_result(text):
    result.configure(text=text)

# Create a new game
def new_game():
    guess_button.config(state='normal')
    global TARGET
    TARGET = random.randint(0, 1000)
    update_result(text="Guess a number between 1 and 1000")

def compare_size(rand,guess,count):
    if(rand > guess):
        count -= 1
        hint = "Value is less by: ", rand - guess, " total score " , count
        return hint

    elif(rand < guess):
        return "Value more by: ", guess - rand, " total score ", count

    else:
        guess_button.configure(state='disabled')
        number_form.configure(state='disabled')
        send_button.configure(state='normal')
        return "Total score is ", count, " please enter your number in the field above"


def get_phone_number():
    phone_number = phone_form.get()
    if(len(phone_number) != 13):
        result =  "Please enter a valid phone number: "
        update_result(result)

    if(phone_number[:4] != "+254"):
        result = "Country code begins with +254: "
        update_result(result)


    send_msg(phone_number)

def send_msg(phone_number):
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    message = "You scored  out of 10"
    update_result(message)
    pywhatkit.sendwhatmsg(phone_number , message , hour , minute+2)


        


# Continue the ongoing game or end it
def play_game():
    global count
    valid = False
    if not valid:
        try:
            choice = int(number_form.get())
            result = compare_size(TARGET,choice,count)    
            update_result(result)
        except ValueError:
            result = "Invalid input"
            update_result(result)


# Heading of our game
title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#36454f")

# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)

# Play Button
play_button = tk.Button(window, text="START", font=("Arial", 12, "bold"), fg = "Black", bg="#00B25D", command=new_game)

# Guess Button
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="#282C35", command=play_game)
send_button = tk.Button(window,text="SEND",font=("Arial",13), state='disabled', fg="gray",bg="#0088D8", command=get_phone_number)


# Exit Button
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)


# Entry Fields
guessed_number = tk.StringVar()
phone_number = tk.StringVar()

number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
phone_form = tk.Entry(window,font=("Arial",11),textvariable=phone_number)


# Place the labels

title.place(x=250, y=50)
result.place(x=250, y=250)

# Place the buttons
exit_button.place(x=300,y=320)
guess_button.place(x=450, y=145) 
send_button.place(x=450, y=190) 

play_button.place(x=325, y=90)

# Place the entry field
number_form.place(x=180, y=150)
phone_form.place(x=180, y=200)


# Start the window
window.mainloop()