from tkinter import *
import random

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Aptos"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    new_pass = random.choice(letters) for n in range(6)
    pass_input.delete(0, END)
    pass_input.insert(END, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    email = email_input.get()
    psw = pass_input.get()

    items = f"{web}|{email}|{psw}" + "\n"
    with open("./data/saved_data.txt", mode="a") as file:
        file.write(items)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager V1.0")
window.minsize(600, 400)
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=190, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image= logo)
canvas.grid(column=2, row=1)

web_label = Label(text="Website/Platform:", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
web_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
email_label.grid(column=1, row=3)

pass_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
pass_label.grid(column=1, row=4)

web_input = Entry(width=40)
web_input.grid(column=2, row=2)

email_input = Entry(width=40)
email_input.insert(END, "shaunhartley53@gmail.com")
email_input.grid(column=2, row=3)

pass_input = Entry(width=20)
pass_input.grid(column=1, row=4, columnspan=5)

pass_btn = Button(text="Generate Password", font=(FONT_NAME, 8, "bold"), command=gen_pass)
pass_btn.grid(column=3, row=4)

pass_add = Button(text="Add", font=(FONT_NAME, 8, "bold"), width=34, command=save)
pass_add.grid(column=2, row=5)

window.mainloop()