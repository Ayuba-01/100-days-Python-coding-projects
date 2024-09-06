from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-250, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level = {self.level}", False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_level()