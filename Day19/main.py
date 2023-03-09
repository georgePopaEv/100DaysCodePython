# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def forward():
#     tim.forward(5)
#
# def backward():
#     tim.backward(5)
#
# def rotate_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clock_rotate():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear_all():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun = forward)
# screen.onkey(key="s", fun = backward)
# screen.onkey(key="a", fun = rotate_left)
# screen.onkey(key="d", fun = clock_rotate)
# screen.onkey(key="c", fun = clear_all)
# screen.exitonclick()
#
#
# # Passing a funtion to another funtion
# def add(n1,n2):
#     return n1+n2
# def calculator(n1, n2, func):
#     return func(n1,n2)
#
# print(calculator(12,3,add))

from turtle import Turtle, Screen
import random
def create_caracteristic_turtle(color,posX,posY):
    t = Turtle(shape='turtle')
    t.color(color)
    t.penup()
    t.goto(posX,posY)
    t.pendown()
    return t

screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
pos = -190
for _ in range(len(colors)):
    turtles.append(create_caracteristic_turtle(colors[_],-240,pos))
    pos += 50


if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor()>230:
            is_race_on = False
            win_race = t.color()[0]
        t.forward(random.randint(0,10))
if user_bet.lower() == win_race.lower():
    print(f"You had right It won {win_race} color")
else:
    print(f"I am sorrry but the win color is {win_race} and you bet {user_bet}")
screen.exitonclick()