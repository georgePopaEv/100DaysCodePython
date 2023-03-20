import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
UP = ['W','w', 'Up']

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
freq_cars = 0.5
player = Player()
car = CarManager()
t_new_car = 0
for k in UP:
    screen.onkey(player.go_up, k)
screen.listen()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    t_new_car += 0.1
    # if t_new_car == 0.1:
    car.moving_cars()
    if round(t_new_car,ndigits=1) == freq_cars:
        t_new_car = 0
        car.generate_one_car()

    game_is_on = car.check_colision(player)
    if game_is_on is not True:
        scoreboard.write_game_over()

    if player.ycor() > 280:
        scoreboard.increase_level()
        scoreboard.write_level()
        freq_cars -= 0.1
        car.level_up()
        player.next_level()

    screen.update()

screen.exitonclick()