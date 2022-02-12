"""
Robot
"""


class Robot:
    am_i_alive = 1
    name = 'Aspirobot T-0.1'

    def __call__(self) -> None:
        return

    def execute(self):
        print(self.name + ": " + "Execute")
        pass

    def boot(self) -> None:
        """
        Démarre le robot
        """
        print("Boot Robot")
        print("Name :", self.name)
