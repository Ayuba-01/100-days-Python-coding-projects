from turtle import Turtle, Screen
import random


my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
colours = ["Blue", "Red", "Black", "Pink", "Purple", "Burlywood", "LawnGreen", "Crimson"]
sides = [3,4,5,6,7,8,9,10]
for side in sides:
    angle = 360/side
    for _ in range(side):
        my_turtle.forward(100)
        my_turtle.color(random.choice(colours))
        my_turtle.right(angle)


screen = Screen()
screen.exitonclick()