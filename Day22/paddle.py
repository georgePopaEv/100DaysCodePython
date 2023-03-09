from turtle import Turtle
import time
direction = 10
class Paddle:
    def __init__(self, p):
        self.paddle = self.create_paddle()
        self.paddle.goto(350,0) if p=='player' else self.paddle.goto(-350,0)

    def create_paddle(self):
        padd = Turtle()
        padd.shape('square')
        padd.color('white')
        padd.setheading(90)
        padd.shapesize(stretch_wid=1, stretch_len=5)
        padd.penup()
        return padd

    def moving_continue(self):
        self.paddle.forward(10)
        time.sleep(0.06)
        self.change_direction()

    def move_up(self):
        self.paddle.forward(10)

    def move_down(self):
        self.paddle.forward(-10)
    def change_direction(self):
        if self.paddle.ycor() > 300:
            self.paddle.setheading(270)
        elif self.paddle.ycor() < -300:
            self.paddle.setheading(90)


