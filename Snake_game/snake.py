import turtle as t


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake_body()
        self.snake_head = self.snake_body[0]

    def create_snake_body(self):
        for _ in range(3):
            new_square = t.Turtle(shape="square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(STARTING_POSITION[_])
            self.snake_body.append(new_square)

    def move(self):
        for square_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[square_num - 1].xcor()
            new_y = self.snake_body[square_num - 1].ycor()
            self.snake_body[square_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
