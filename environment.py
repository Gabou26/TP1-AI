"""
Environment
"""


class Environment:
    length_x = 5
    length_y = 5
    matrix = []

    def __call__(self) -> None:
        return

    def __init__(self, length_x, length_y) -> None:
        self.length_x = length_x
        self.length_y = length_y
        self.create_matrix()
        return

    def create_matrix(self):
        print(self.length_x)
        self.matrix = []
        for y in range(self.length_y):
            self.matrix.append([])
            for x in range(self.length_x):
                self.matrix[y].append(0)

    def get_matrix(self):
        return self.matrix

    def get_slot_data(self, x, y):
        return self.matrix[y][x]

    def add_slot_data(self, x, y, data_id):
        slot_id = self.matrix[y][x]
        if data_id == 2:  # Is Jewel
            if slot_id == 1:
                self.matrix[y][x] = 3  # New Status = Both Jewel and Dust
            elif slot_id != 3:
                self.matrix[y][x] = data_id
        elif data_id == 1:  # Is Dust
            if slot_id == 2:
                self.matrix[y][x] = 3
            elif slot_id != 3:
                self.matrix[y][x] = data_id

    def get_size_x(self):
        return self.length_x

    def get_size_y(self):
        return self.length_y
