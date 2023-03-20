from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("data.txt", ) as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}",move=False,align="center",font=('Arial', 24, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", move=False, align="center", font=('Arial', 24, 'normal'))

    def reset(self):

        if(self.score > self.highscore):
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over ", move=False, align="center", font=('Arial', 24, 'normal'))