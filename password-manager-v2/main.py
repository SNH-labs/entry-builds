from tkinter import messagebox, simpledialog
from tkinter import *
from tkinter import ttk
import random
import pandas

data = pandas.read_csv("./data/saved_data.csv")


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Aptos"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    pass_list = []

    for n in range(7):
        pass_list.append(random.choice(LETTERS))

    for n in range(4):
        pass_list.append(random.choice(NUMBERS))

    for n in range(3):
        pass_list.append(random.choice(SYMBOLS))

    random.shuffle(pass_list)
    pass_str = "".join(pass_list)

    pass_input.delete(0, END)
    pass_input.insert(0, pass_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    email = email_input.get()
    psw = pass_input.get()

    data.loc[len(data)] = [web, email, psw]

    if web == "" or email == "" or psw == "":
        messagebox.showerror(title=web, message="One or more fields are empty. Password not saved.")

    else:

        ans = messagebox.askyesno(title=web, message=f"Do you want to save the current password:\n-{email}\n-{psw}")
        if ans:

            data.to_csv("./data/saved_data.csv", index=FALSE)

            messagebox.showinfo(title=web, message="Password details saved successfully!")

            web_input.delete(0, END)
            pass_input.delete(0, END)

        else:
            messagebox.showinfo(title=web, message="Password not saved.")

# ---------------------------- DISPLAY DATA ------------------------------- #
def display():
    lock = simpledialog.askstring(title="Access Data", prompt="Please enter password to access data.")

    if lock == "pantsynow":
        window_2 = Tk()
        window_2.config(padx=20, pady=20, bg=YELLOW)
        window_2.title("Password Data")

        tree = ttk.Treeview(window_2)
        tree["columns"] = list(data.columns)
        tree["show"] = "headings"
        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for _, row in data.iterrows():
            tree.insert("", "end", values=list(row))

        tree.column("Username", width=200)

        tree.pack(expand=True, fill='both')

        window_2.mainloop()

    else:
        messagebox.showerror(title="Access Data", message="Incorrect entry.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager V1.0")
window.minsize(600, 400)
window.config(bg=YELLOW)

bg_image = PhotoImage(file="./Data/pants_vault_img.png")

bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

web_label = Label(text="Website/Platform:", font=(FONT_NAME, 8, "bold"))
web_label.place(x=100, y=200)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 8, "bold"))
email_label.place(x=100, y=230)

pass_label = Label(text="Password:", font=(FONT_NAME, 8, "bold"))
pass_label.place(x=100, y=260)

web_input = Entry(width=35)
web_input.place(x=220, y=200)

email_input = Entry(width=35)
email_input.insert(END, "shaunhartley53@gmail.com")
email_input.place(x=220, y=230)

pass_input = Entry(width=18)
pass_input.place(x=220, y=260)

pass_btn = Button(text="Generate Password", width=15, font=(FONT_NAME, 7, "bold"), command=gen_pass)
pass_btn.place(x=340, y=260)

pass_add = Button(text="Add", font=(FONT_NAME, 8, "bold"), width=30, command=save)
pass_add.place(x=220, y=290)

display_btn = Button(text="Display Data", font=(FONT_NAME, 8, "bold"), width=30, command=display)
display_btn.place(x=220, y=320)

window.mainloop()