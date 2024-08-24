from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 25, "bold")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(self.score, False, align=ALIGNMENT, font=FONT)
