"""
Robot
"""


class Robot:
    am_i_alive = 0
    name = 'Aspirobot T-0.1'

    def __call__(self) -> None:
        return

    def execute(self):
        print("Execute")
        pass

    def boot(self) -> None:
        """
        Démarre le robot
        """
        print("Boot Robot")
        print("Name :", self.name)
