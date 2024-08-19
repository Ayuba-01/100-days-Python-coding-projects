import turtle as t


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake_body()
        self.snake_head = self.snake[0]
        self.snake_body = self.snake[1:]

    def add_to_snake_body(self, position):
        new_square = t.Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.snake.append(new_square)

    def create_snake_body(self):
        for position in STARTING_POSITION:
            self.add_to_snake_body(position)

    def extend_snake(self):
        last_snake_body = self.snake[-1]
        # last_xcor = last_snake_body.xcor()
        # last_ycor = last_snake_body.ycor()
        # new_xcor = last_xcor - 20
        # new_position = (new_xcor, last_ycor)
        new_position = last_snake_body.position()
        self.add_to_snake_body(new_position)

    def move(self):
        for square_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[square_num - 1].xcor()
            new_y = self.snake[square_num - 1].ycor()
            self.snake[square_num].goto(new_x, new_y)
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


