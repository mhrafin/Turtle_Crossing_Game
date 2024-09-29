import random
from turtle import Turtle


class Bus(Turtle):
    def __init__(self, shape_width) -> None:
        super().__init__()
        self.penup()

        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        self.color(random.choice(self.colors))

        self.shape("square")

        self.shape_wid = shape_width
        self.resizemode("user")
        self.shapesize(self.shape_wid, 1, None)

        self.setheading(90)
        self.goto(-250, 0)
        self.bus_speed = 1

    def move_bus(self):
        self.goto(self.xcor() - self.bus_speed, self.ycor())

    def out_of_screen(self):
        if self.xcor() < -200:
            self.goto(self.random_x_y())

    def new_level(self):
        self.goto(self.random_x_y())

    def random_x_y(self):
        randomxy = (random.randint(200, 600), random.randint(-240, 240))
        return randomxy
