import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car1 = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.up)

game_is_on = True
counter = 0
car_list = [car1]
while game_is_on:
    time.sleep(0.1)
    counter += 1
    if counter == 4:
        new_car = CarManager()
        car_list.append(new_car)
        counter = 0
    for car in car_list:
        car.move()
        # detect collision
        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()
        # detect if turtle has crossed the screen
        if player.is_at_finish_line() is True:
            player.refresh_turtle()
            car.increase_move()
            level.increase_level()
    screen.update()


screen.exitonclick()
