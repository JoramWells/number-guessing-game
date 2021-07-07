import tkinter as tk
from sys import exit
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


def update(text):
    result.configure(text=text)


def compare_size(rand,guess):
    if(rand > guess):
        return ("Value is less by: {}".format(rand - guess))

    elif(rand < guess):
        count -= 1
        return ("Value more by: ", guess - rand, " total score ", count)

    else:
        guess_btn.configure(state='disabled')
        no_form.configure(state='disabled')
        send_btn.config(state='normal')
        phone_form.config(state='normal')
        return "Please enter your number in the field above"

def phone_is_digit(number):
    number = number[1:]
    if(number.isdigit() == False):
        return False
    else:
        pass

def get_country_code(phone_number):
    code = phone_number[:4]
    if(code != "+254"):
        return False
    else:
        pass
def get_number_len(phone_number):
    if(len(phone_number) != 13):
        return False
    else:
        pass

def get_phone_number():
    phone_number = phone_form.get()
    code = get_country_code(phone_number)
    length = get_number_len(phone_number)
    is_digit = phone_is_digit(phone_number)

    if(code == False):
        result = "Country code begins with +254: "
        update(result)
    elif(length == False):        
        result =  "The number should be 13 digits. "
        update(result)
    elif(is_digit==False):
        result = "The number should be a digit. "
        update(result)
    else:
        send_msg(phone_number,count)

def send_msg(phone_number,count):
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    message = "You have successfully completed the game!!",count
    pywhatkit.sendwhatmsg(phone_number , count , hour , minute+2)
    exit()


def game():
    global count
    valid = False
    if(count >0):
        if not valid:
            try:
                count -= 1
                choice = int(no_form.get())
                result = compare_size(TARGET,choice)    
                update(result)
            except ValueError:
                result = "Invalid input"
                update(result)
    else:
        result = "Exceeded maximum trials please restart the game."
        update(result)


title = tk.Label(window,text="Amazing game",font=("Arial",18),fg="#fffcbd",bg="#36454f")

result = tk.Label(window, text="Start the game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#36454f", justify=tk.LEFT)
phone_lbl = tk.Label(window, text="Enter phone number", font=("Arial", 11, "normal", "italic"),fg = "Whitesmoke", bg="#36454f", justify=tk.LEFT)

guess_btn = tk.Button(window,text="Guess",font=("Arial",13), state='normal', fg="#13d675",bg="#282C35", command=game)
send_btn = tk.Button(window,text="SEND",font=("Arial",13), state='disabled', fg="white",bg="#0088D8", command=get_phone_number)

exit_btn = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
guessed_num = tk.StringVar()
phone_number = tk.StringVar()
no_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_num)
phone_form = tk.Entry(window,font=("Arial",11), state="disabled",textvariable=phone_number)


title.place(x=290, y=50)
result.place(x=250, y=250)

exit_btn.place(x=300,y=320)
guess_btn.place(x=450, y=145) 
send_btn.place(x=450, y=210) 

no_form.place(x=180, y=150)
phone_form.place(x=180, y=220)
phone_lbl.place(x=180, y=195)

window.mainloop()