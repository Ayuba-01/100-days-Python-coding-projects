from turtle import Turtle, Screen
import random
import turtle as t


t.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(size):
    for _ in range(int(360/size)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        current_heading = my_turtle.heading()
        my_turtle.setheading(current_heading + size)


draw_spirograph(1)


screen = Screen()
screen.exitonclick()