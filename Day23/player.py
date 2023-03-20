from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape('turtle')
        self.penup()
        self.goto(0, -270)
        self.setheading(90)
    def go_up(self):
        self.forward(10)

    def next_level(self):
        self.goto(0, -270)
