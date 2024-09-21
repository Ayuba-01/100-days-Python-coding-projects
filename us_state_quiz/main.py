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
guessed_states = []
t = turtle.Turtle()
t.hideturtle()
while game_on:
    answer_state = screen.textinput(title=f"{score}/{len(state_list)} State Correct",
                                    prompt="Type a state name").title()

    if answer_state == "Exit":
        state_to_learn = [state for state in state_list if state not in guessed_states]
        df = pandas.DataFrame(state_to_learn)
        df.to_csv("State to Learn")
        t.goto(0, 0)
        t.write(f"Click anywhere to exit", False, "center",
                ("Courier", 14, "normal"))
        break
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        guessed_states.append(answer_state)
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f"{answer_state}", False, "center")
        score += 1
        if score == len(state_list):
            game_on = False
            t.goto(0, 0)
            t.write(f"Congratulations you have guessed all {len(state_list)} states", False, "center",
                    ("Courier", 14, "normal"))

screen.exitonclick()
