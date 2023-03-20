from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snaka Game")
screen.tracer(0)

snake = Snake()
fod = Food()
scre_board = ScoreBoard()



screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
# screen.onkey(scre_board.game_over, "Q")

screen.listen()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(fod)< 15:
        scre_board.increase_score()
        snake.add_new_element_to_snake()
        fod.refresh()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        scre_board.reset()
        snake.reset()
    if snake.colide_with_tail():
        scre_board.reset()
        game_is_on = False


    # screen.onkey(key='w', fun=turn_snake)










screen.exitonclick()