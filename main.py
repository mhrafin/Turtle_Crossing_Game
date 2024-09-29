import time
from turtle import Screen

from bus_manager import BusManager
from scoreboard import Scoreboard
from turtle_character import TurtleCharacter


def main():
    screen = Screen()
    screen.title("Turtle Cross")
    screen.setup(width=400, height=600, startx=1, starty=1)
    screen.tracer(0)

    screen.listen()

    player = TurtleCharacter()

    screen.onkeypress(fun=player.move_up, key="w")
    screen.onkeypress(fun=player.move_down, key="s")

    bus_manager = BusManager(level=1)

    scoreboard = Scoreboard()

    game_on = True
    while game_on:
        time.sleep(0.01)
        screen.update()

        bus_manager.game_active()

        if player.ycor() > 300:
            bus_manager.increase_level()
            player.start_pos()

            scoreboard.level = bus_manager.current_level
            scoreboard.current_level()

        for bus in bus_manager.buses:
            if player.distance(bus) < 20:
                scoreboard.game_over()
                game_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
