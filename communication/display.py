"""
Affichage
"""
from communication.environment_controller import EnvironmentController
from simulator.robot import Robot


class Display:
    environment_controller = EnvironmentController()
    metric = Robot().believe.metric
    state = Robot().believe.state

    def __call__(self) -> None:
        self.environment_controller = EnvironmentController()
        return

    def print(self):
        """
        Affichage de la matrice
        """
        matrix = self.environment_controller.environment.get_matrix()
        print('------MAP-------')
        for y in range(len(matrix)-1, -1, -1):
            print(matrix[y])

        print('------TEST EXPLORATION-------')
        print(str(self.environment_controller.environment.test_exploration()))

        self.print_metric()

        self.print_state()

    def print_metric(self) -> None:
        print('-----METRIC-----')
        print(vars(self.metric))

    def print_state(self) -> None:
        print('-----STATE-----')
        print(vars(self.state))
