from turtle import Turtle, Screen
import turtle
import colorgram
import random as r
timmy_the_turtle = Turtle()
timmy_the_turtle.penup()
timmy_the_turtle.speed(9)
def new_row(turtle):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)

timmy_the_turtle.setheading(235)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
#
# def rectangle(turtle):
#     for _ in range(4):
#         turtle.right(90)
#         turtle.fd(100)
# def dash_line(turtle):
#     turtle.fd(10)
#     turtle.penup()
#     turtle.fd(10)
#     turtle.pendown()
#
# for i in range(10   ):
#     dash_line(timmy_the_turtle)
# # rectangle(timmy_the_turtle)
turtle.colormode(255)
colors = colorgram.extract('images.jpg', 10)
for i in range(len(colors)):
    colors[i] = tuple(colors[i].rgb)

# print(r.choice(colors))
# timmy_the_turtle.color(r.choice(colors))
for i in range(10):
    for _ in range(10):
        timmy_the_turtle.dot(20, r.choice(colors))
        timmy_the_turtle.forward(50)
    new_row(timmy_the_turtle)



screen = Screen()
screen.exitonclick()

