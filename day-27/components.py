# Labels:
my_label = Label(text="I am a label", font=("Arial", 16, "bold"))
my_label.pack()

#Buttons:
def button_click():
    new_text = choice.get()
    print(new_text)

my_button = Button(text="Click me", command=button_click)
my_button.pack()

# Basic Entry:
choice = Entry(width=10)
choice.pack()

# Text Box:
text = Text(height=5, width=20)
text.insert(END, "What's up")
print(text.get("1.0", END))
text.pack()

#Spin Box:
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Check Box:
def check_used():
    print(checked.get())

checked = IntVar()
checkbox = Checkbutton(text="Is this on?", variable=checked, command=check_used)
checkbox.pack()

#Scale:
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Radio Button:
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

#List Box:
def list_used(event):
    print(list_box.get(list_box.curselection()))

names = ["Shaun", "Sian", "Bodi"]
list_box = Listbox(height=4)
for n in names:
    list_box.insert(names.index(n), n)

list_box.bind("<<ListboxSelect>>", list_used)

list_box.pack()