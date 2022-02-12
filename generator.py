"""
Générateur de poussière et bijoux
"""
import random

from display import Display
from environment import Environment


class Generator:
    am_i_alive = 1
    name = 'Manoir'
    dust_generation_rate = 30
    jewel_generation_rate = 5

    def __call__(self) -> None:
        return

    def __init__(self):
        print("WSS")
        self.environment = Environment(5, 5)
        self.display = Display()
        return

    def execute(self):
        """Check to see if we're adding components to the map"""
        if self.should_add_dust():
            print("Dust spawn")
            self.add_item(1)
        if self.should_add_jewel():
            print("Jewel spawn")
            self.add_item(2)

        self.display.print(self.environment.get_matrix())

    def boot(self) -> None:
        """
        Démarre le générateur du manoir
        """
        print("Booting Map")
        print("Name :", self.name)

    def should_add_dust(self):
        """
        Nous avons 30 % de chance de généré une poussière
        """
        if random.randint(0, 100) < self.dust_generation_rate:
            return True
        return False

    def should_add_jewel(self):
        """
        Nous avons 5 % de chance de généré une un bijou
        """
        if random.randint(0, 100) < self.jewel_generation_rate:
            return True
        return True

    def add_item(self, data_id):
        random.seed()
        rand_x = random.randrange(0, self.environment.get_size_x())
        rand_y = random.randrange(0, self.environment.get_size_y())
        self.environment.add_slot_data(rand_x, rand_y, data_id)

    def show_map(self):
        matrix = self.environment.get_matrix()
        for y in range(len(matrix)):
            print(matrix[y])
