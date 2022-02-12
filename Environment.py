"""
Environnement
"""

class Environment:
    length_x = 5
    length_y = 5
    map = []

    def __call__(self) -> None:
        return

    def __init__(self, length_x, length_y) -> None:
        self.length_x = length_x
        self.length_y = length_y
        self.create_map()
        return

    def create_map(self):
        print(self.length_x)
        self.map = []
        for y in range(self.length_y):
            self.map.append([])
            for x in range(self.length_x):
                self.map[y].append(0)

    def get_map(self):
        return self.map

    def get_slot_data(self, x, y):
        return map[y][x]

    def add_slot_data(self, x, y, data_id):
        slot_id = self.map[y][x]
        if data_id == 2: #Is Jewel
            if slot_id == 1:
                self.map[y][x] = 3 #New Status = Both Jewel and Dust
            elif slot_id != 3:
                self.map[y][x] = data_id
        elif data_id == 1: #Is Dust
            if slot_id == 2:
                self.map[y][x] = 3
            elif slot_id != 3:
                self.map[y][x] = data_id

    def get_size_x(self):
        return self.length_x

    def get_size_y(self):
        return self.length_y