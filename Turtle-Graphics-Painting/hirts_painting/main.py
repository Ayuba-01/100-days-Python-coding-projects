# import colorgram
#
#
# colors = colorgram.extract("dot_image.jpg", 30)
#
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r,g,b)
#     color_list.append(color_rgb)
# print(color_list)
from turtle import Turtle, Screen
import random
import turtle as t

colors_list = [
    (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5),
    (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
    (240, 245, 251),
    (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22),
    (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)
]
t.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed(0)
my_turtle.hideturtle()
my_turtle.penup()


height = 10
width = 10
i = 1
while i <= height:
    for _ in range(width):
        my_turtle.dot(20, random.choice(colors_list))
        my_turtle.forward(50)

    my_turtle.home()
    my_turtle.sety(50.00 * i)
    i += 1
    if i == 11:
        go_on = False



screen = Screen()
screen.exitonclick()
