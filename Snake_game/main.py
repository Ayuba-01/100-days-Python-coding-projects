import turtle as t
from snake import Snake
import time

is_game_on = True
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()