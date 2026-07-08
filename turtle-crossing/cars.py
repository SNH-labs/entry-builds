from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["red", "blue", "green", "purple", "orange", "brown"]
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.color(random.choice(self.colors))
        self.penup()
        self.pin_y = random.randint(-200, 250)
        self.setposition(280, self.pin_y)
        self.setheading(180)
        self.movement = random.randint(2, 10)

    def drive(self, diff):
        self.forward(self.movement)
        if self.xcor() <= -320:
            self.pin_y = random.randint(-250, 250)
            self.setposition(280, self.pin_y)
            self.movement = random.randint(2 * diff, 10 * diff)

