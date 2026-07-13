import pandas
from turtle import Turtle, Screen

df = pandas.read_csv("50_states.csv")

state_names = df.state.to_list()

screen = Screen()
screen.title("US States Quiz")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

points = 0
guessed_states = []

running = True
while running:
    choice = screen.textinput(f"{points}/50 states correct", "Name a state:").title()

    if choice in state_names:
        plot = Turtle()
        x_value = df[df.state == choice].x.item()
        y_value = df[df.state == choice].y.item()
        plot.penup()
        plot.hideturtle()
        plot.goto(x_value, y_value)
        plot.write(choice, False, "center", ("Arial", 8, "bold"))
        guessed_states.append(choice)
        points += 1

    elif choice == "Exit":
        missing_states = [states for states in state_names if states not in guessed_states]
        mis_df = pandas.DataFrame(missing_states)
        mis_df.to_csv("./missing_states.csv")
        running = False


screen.exitonclick()



