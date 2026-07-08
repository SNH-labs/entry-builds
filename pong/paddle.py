from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle_list = []
        self.create_paddle()

    def create_paddle(self):

        y_position = -20
        for n in range(3):
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.teleport(0,y_position)
            self.paddle_list.append(paddle)
            y_position += 20


    def up(self):
        for segs in self.paddle_list:
            segs.setheading(90)
            segs.forward(20)

    def down(self):
        for segs in self.paddle_list:
            segs.setheading(270)
            segs.forward(20)

