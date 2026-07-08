from turtle import Turtle, Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time


def draw_net():
    net = Turtle()
    net.hideturtle()
    net.color("white")
    net.pensize(3)
    net.speed("fastest")
    net.teleport(0, -350)
    net.setheading(90)
    for n in range(35):
        net.forward(10)
        net.penup()
        net.forward(10)
        net.pendown()

def paddle_setup():
    for segs in player_1.paddle_list:
        segs.setx(-480)

    for segs in player_2.paddle_list:
        segs.setx(480)

def clear():
    ball.reset()
    for n in range(3):
        player_1.paddle_list[n].reset()
        player_2.paddle_list[n].reset()


screen = Screen()
screen.tracer(0)
screen.listen()
screen.title("Pong V1.0")
screen.bgcolor("black")
screen.setup(1000, 700)
draw_net()
score = Score()

on = True
while on:

    ball = Ball()
    player_1 = Paddle()
    player_2 = Paddle()
    paddle_setup()
    game_over = False

    while not game_over:

        screen.update()
        time.sleep(0.05)

        ball.forward(20)



        if player_2.paddle_list[1].distance(ball) < 10:
            ball.bounce()

        elif player_1.paddle_list[1].distance(ball) < 10:
            ball.setheading(0)
            ball.move()

        elif player_1.paddle_list[2].distance(ball) <20:
            ball.move_left()

        elif player_1.paddle_list[0].distance(ball) <20:
            ball.move_right()

        elif player_2.paddle_list[2].distance(ball) < 20:
            ball.bounce_right()

        elif player_2.paddle_list[0].distance(ball) < 20:
            ball.bounce_left()

        elif ball.out_left():
            score.score_2 += 1
            score.score_update()
            game_over = True
            clear()

        elif ball.out_right():
            score.score_1 += 1
            score.score_update()
            game_over = True
            clear()

        screen.onkeypress(player_1.up, "w")
        screen.onkeypress(player_1.down, "s")
        screen.onkeypress(player_2.up, "Up")
        screen.onkeypress(player_2.down, "Down")




















screen.exitonclick()