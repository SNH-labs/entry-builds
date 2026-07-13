from tkinter import *

window = Tk()
window.title("Distance Convertor")
window.minsize(300, 100)
window.config(padx=20, pady=20)

def button_click():
    value = int(choice.get())
    new_value = round(value * 1.609344, 2)
    label_result.config(text=new_value)

label_equal = Label(text="is equal to", font=("Arial", 10, "normal"))
label_equal.grid(column=1, row=2)

my_button = Button(text="Calculate", command=button_click)
my_button.grid(column=2, row=3)

label_miles = Label(text="Miles", font=("Arial", 10, "normal"))
label_miles.grid(column=3, row=1)

label_km = Label(text="Km", font=("Arial", 10, "normal"))
label_km.grid(column=3, row=2)

label_result = Label(text="0", font=("Arial", 10, "normal"))
label_result.grid(column=2, row=2)

choice = Entry(width=10)
choice.grid(column=2, row=1)


window.mainloop()