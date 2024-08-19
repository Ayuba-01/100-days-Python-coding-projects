import turtle as t
from snake import Snake
from food import Food
from score import Score
import time


is_game_on = True
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.extend_snake()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect collision with body
    for body in snake.snake_body[1:]:
        if snake.snake_head.distance(body) < 10:
            is_game_on = False
            score.game_over()
    #if snake.snake_head.distance(snake.snake_body[])

screen.exitonclick()
