from turtle import Turtle

STARTING_POS = (0, -270)


class TurtleCharacter(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.start_pos()

    def start_pos(self):
        self.goto(STARTING_POS)

    def move_up(self):
        if self.ycor() < 310:
            self.forward(10)

    def move_down(self):
        if self.ycor() > -270:
            self.backward(10)
