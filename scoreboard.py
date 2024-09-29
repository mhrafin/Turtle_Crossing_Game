from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(-100, 260)
        self.hideturtle()
        self.level = 1
        self.current_level()

    def current_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.fillcolor("white")
        self.write("Game Over!", False, "center", ("Courier", 30, "normal"))
