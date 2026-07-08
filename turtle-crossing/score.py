from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.level = 1
        self.teleport(-250, 270)
        self.write(f"Level: {self.level}", False, "center", ("Arial", 12, "bold"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", ("Arial", 12, "bold"))

    def hit(self):
        self.clear()
        self.teleport(0,0)
        self.write("GAME OVER", False, "center", ("Arial", 18, "bold"))