from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(f"SCORE: {self.score}", False, align="center", font=("Ariel", 20, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="center", font=("Ariel", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Ariel", 20, "normal"))