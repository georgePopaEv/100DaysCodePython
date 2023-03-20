from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-170,270)
        self.clear()
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
