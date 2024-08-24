import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

is_game_on = True
screen = t.Screen()
screen.setup(width=1000, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle(450, 0)
l_paddle = Paddle(-450, 0)
ball = Ball()
r_score = Score((40, 250))
l_score = Score((-40, 250))
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() >= 430 or ball.xcor() <= -430:
        if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
            ball.bounce_x()

    # when r_paddle misses
    if ball.xcor() >= 520:
        ball.reset_ball()
        l_score.increase_score()

    # when l_paddle misses
    if ball.xcor() <= -520:
        ball.reset_ball()
        r_score.increase_score()


screen.exitonclick()
