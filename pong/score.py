from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0

        self.teleport(-100, 300)
        self.write(f"Score: {self.score_1}", False, "Center", ("Arial", 20, "normal"))
        self.teleport(100, 300)
        self.write(f"Score: {self.score_2}", False, "Center", ("Arial", 20, "normal"))

    def score_update(self):
        self.clear()
        self.teleport(-100, 300)
        self.write(f"Score: {self.score_1}", False, "Center", ("Arial", 20, "normal"))
        self.teleport(100, 300)
        self.write(f"Score: {self.score_2}", False, "Center", ("Arial", 20, "normal"))
