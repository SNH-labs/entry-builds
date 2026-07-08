from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")


    def move(self):

        self.forward(20)

    def bounce(self):
        self.setheading(180)
        self.forward(20)

    def move_left(self):
        self.setheading(10)
        self.forward(20)

    def move_right(self):
        self.setheading(350)
        self.forward(20)

    def bounce_left(self):
        self.setheading(190)
        self.forward(20)

    def bounce_right(self):
        self.setheading(170)
        self.forward(20)

    def out_left(self):
        if self.xcor() <= -500:
            return True
        else:
            return False

    def out_right(self):
        if self.xcor() >= 500:
            return True
        else:
            return False