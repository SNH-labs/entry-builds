from tkinter import *

window = Tk()
window.title("Distance Convertor")
window.minsize(200, 80)
window.config(padx=20, pady=20)

def button_click():
    new_text = choice.get()
    print(new_text)

my_label = Label(text="I am a label", font=("Arial", 16, "bold"))
my_label.grid(column=1, row=1)

my_button = Button(text="Click me", command=button_click)
my_button.grid(column=2, row=2)

my_button_2 = Button(text="Click me", command=button_click)
my_button_2.grid(column=3, row=1)

choice = Entry(width=10)
choice.grid(column=4, row=3)


window.mainloop()