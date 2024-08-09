from turtle import Turtle, Screen
import random
import turtle as t


t.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.pensize(10)
my_turtle.speed(9)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


direction = [0, 90, 180, 270]
for _ in range(200):
    my_turtle.forward(40)
    my_turtle.color(random_color())
    my_turtle.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()