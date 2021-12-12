FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(210, 260)
        self.write(f"Score: {self.score}", align = "center", font = FONT)

    def end_score(self):
        self.goto(0,0)
        self.write("Game Over", align= "center", font = FONT)