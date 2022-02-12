"""
Robot
"""
import random

from Environment import Environment

class Generator:
    am_i_alive = 1
    name = 'Manoir'

    def __call__(self) -> None:
        return

    def __init__(self):
        print("WSS")
        self.environment = Environment(5,5)
        return

    def execute(self):
        """Check to see if we're adding components to the map"""
        if (self.should_add_dust()):
            self.add_item(1)
        if (self.should_add_jewel()):
            self.add_item(2)

        """Printing map"""
        print(self.name + ": ")
        self.show_map()

    def boot(self) -> None:
        """
        Démarre le générateur du manoir
        """
        print("Booting Map")
        print("Name :", self.name)

    def should_add_dust(self):
        return True

    def should_add_jewel(self):
        return True

    def add_item(self, data_id):
        random.seed()
        rand_x = random.randrange(0, self.environment.get_size_x())
        rand_y = random.randrange(0, self.environment.get_size_y())
        self.environment.add_slot_data(rand_x, rand_y, data_id)

    def show_map(self):
        map = self.environment.get_map()
        for y in range(len(map)):
            print(map[y])
