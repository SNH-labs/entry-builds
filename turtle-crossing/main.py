from turtle import Turtle, Screen
from turt import Turt
from score import Score
from cars import Cars
import time

screen = Screen()
screen.setup(600, 600)

pants = Turt()
screen.tracer(0)
screen.listen()

score = Score()
cars = []
traffic = 5

for n in range(traffic):
    car = Cars()
    cars.append(car)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)

    for guy in cars:
        guy.drive(score.level)

    if pants.ycor() >= 300:
        pants.made_it()
        score.level_up()
        traffic += 2
        car = Cars()
        cars.append(car)

    for col in cars:
        if col.distance(pants) <= 25 and col.ycor() < 20:
            game_over = True
            score.hit()

        elif col.distance(pants) <= 25 and col.ycor() > -20:
            game_over = True
            score.hit()


    screen.onkey(pants.move, "Up")
    screen.onkey(pants.move_back, "Down")



screen.exitonclick()