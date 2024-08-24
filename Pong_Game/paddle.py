import turtle as t
USER_STARTING_POSITION = [(450, 40),(450, 20), (450, 0), (450, -20), (450, -40)]
#COMPUTER_STARTING_POSITION = [(480, 0), (480, -20), (480, 20)]


class Paddle(t.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x, y)

    def move_up(self):
        if self.ycor() <= 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



