from turtle import Turtle

class Turt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.teleport(0, -260)
        self.setheading(90)

    def move(self):
        self.setheading(90)
        self.forward(20)

    def move_back(self):
        self.setheading(270)
        self.forward(20)

    def made_it(self):
        self.teleport(0, -260)




