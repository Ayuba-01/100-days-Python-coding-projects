from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    current_car_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-240, 240))
        self.setheading(180)
        self.move()

    def move(self):
        self.forward(CarManager.current_car_speed)

    @classmethod
    def increase_move(cls):
        cls.current_car_speed += MOVE_INCREMENT


