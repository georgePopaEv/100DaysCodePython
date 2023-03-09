from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.directionX_Y = {'x':10,
                             'y':10}


    def create_ball(self):
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.shape('circle')

    def move(self):
        self.goto(self.xcor() + self.directionX_Y['x'], self.ycor() + self.directionX_Y['y'])
        time.sleep(0.01)

    def bounce(self, p):
        self.directionX_Y[p] *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce('x')