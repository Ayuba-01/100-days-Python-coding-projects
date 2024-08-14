import turtle as t


my_turtle = t.Turtle()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def move_clock_wise():
    my_turtle.right(10.0)


def move_counter_clock_wise():
    my_turtle.left(10.0)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clock_wise)
screen.onkey(key="d", fun=move_clock_wise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
