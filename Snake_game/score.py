from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def store_highscore(self):
        with open("high_score.txt", mode="w") as high_score:
            high_score.write(f"{self.high_score}")
