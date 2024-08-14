import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racing")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-80, -50, -20, 10, 40, 70]
turtles = []
for _ in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[_])
    new_turtle.goto(x=-230, y=position[_])
    turtles.append(new_turtle)


user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race: ").lower()
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"Congratulation you won, the {winning_turtle} turtle wins the race")
            else:
                print(f"Sorry you lost, the {winning_turtle} turtle wins the race")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
