from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}",move=False,align="center",font=('Arial', 24, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ", move=False, align="center", font=('Arial', 24, 'normal'))