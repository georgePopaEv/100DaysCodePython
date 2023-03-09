from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.screensize(canvwidth=800, canvheight=600)
my_screen.bgcolor(str('black'))
my_screen.title("Pong Game Boss")
my_screen.tracer(0)


player = Paddle('player')
cmp = Paddle('cmp')
ball = Ball()
scoreboard = Scoreboard()

my_screen.onkey(player.move_up, "Up")
my_screen.onkey(player.move_down, "Down")
my_screen.listen()

game_is_on = True
ball.bounce('x')
while game_is_on:
    my_screen.update()
    # time.sleep(0.1)
    cmp.moving_continue()
    ball.move()
    scoreboard.write_score()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')
    elif ball.distance(player.paddle) < 60 or ( ball.distance(cmp.paddle.xcor(),cmp.paddle.ycor()-50) or ball.distance(cmp.paddle.xcor(),cmp.paddle.ycor()+50))< 40:
        ball.bounce('x')
    elif ball.xcor() > 380:
        ball.reset()
        scoreboard.l_score +=1
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score += 1

        #ball.bounce('x')



# my_screen.update()









my_screen.exitonclick()
