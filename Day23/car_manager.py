from turtle import Turtle
import random as rr
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():

    def __init__(self):
        super().__init__()
        self.move_speed= STARTING_MOVE_DISTANCE
        self.cars = []


    def generate_one_car(self):
        c = Turtle()
        c.penup()
        c.shapesize(stretch_wid=1, stretch_len=2)
        c.shape('square')
        c.setheading(180)
        c.goto(300, rr.randint(-28,28)*10)
        c.color(rr.choice(COLORS))
        self.cars.append(c)

    def moving_cars(self):
        for _ in self.cars:
            _.forward(self.move_speed)

    def check_colision(self, player):
        for _ in self.cars:
            if _.distance(player.xcor() + 10, player.ycor()+5) < 20:
                return False
        return True

    def level_up(self):
        self.move_speed += MOVE_INCREMENT