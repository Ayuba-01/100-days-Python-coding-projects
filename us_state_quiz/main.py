import turtle
import pandas
FONT = ("Courier", 7, "normal")

game_on = True
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
score = 0
t = turtle.Turtle()
t.hideturtle()
while game_on:
    answer_state = screen.textinput(title=f"{score}/{len(state_list)} State Correct", prompt="Type a state name").title()
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        state_xcor = state_data.x
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f"{answer_state}", False, "center")
        score += 1
        if score == 50:
            game_on = False

t.goto(0,0)
t.write("Congratulations you have guessed all 50 states", False, "center", ("Courier", 14, "normal"))

screen.exitonclick()
