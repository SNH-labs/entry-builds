import turtle
from turtle import Turtle

turtle.register_shape("cowboy", "cowboy_3.png")

class Turt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("cowboy")
        self.penup()
        self.teleport(0, -260)
        self.setheading(90)
        self.shapesize(2, 2)
        print(self.shapesize())

    def move(self):
        self.setheading(90)
        self.forward(20)

    def move_back(self):
        self.setheading(270)
        self.forward(20)

    def made_it(self):
        self.teleport(0, -260)




