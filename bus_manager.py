from bus import Bus


class BusManager:
    def __init__(self, level=1) -> None:
        self.current_level = level
        self.buses: list[Bus] = []
        for _ in range(10):
            self.create_bus()

        pass

    def create_bus(self):
        # self.buses: list[Bus] = []
        # for _ in range(self.current_level*4):
        a_bus = Bus(shape_width=2)
        self.buses.append(a_bus)

    def game_active(self):
        for bus in self.buses:
            bus.move_bus()
            bus.out_of_screen()

    def increase_level(self):
        self.current_level += 1
        for _ in range(self.current_level):
            self.create_bus()

        for bus in self.buses:
            bus.bus_speed += 0.2
            bus.new_level()
