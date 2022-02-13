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
        matrix = self.environment_controller.environment.matrix
        matrix_with_robot = matrix.copy()
        robot_x = self.environment_controller.environment.robot_position_x
        robot_y = self.environment_controller.environment.robot_position_y
        # Affichage du robot : Ajoute 10
        matrix_with_robot[robot_y][robot_x] += 10
        print('------MAP-------')
        for y in range(len(matrix_with_robot)):
            print(matrix_with_robot[y])

        self.print_metric()

        self.print_state()
        # TODO Je sais pas pourquoi la copy fonctione pas pour cloner l'array on doit le remettre normal après
        #  l'affichage
        matrix_with_robot[robot_y][robot_x] -= 10

    def print_metric(self) -> None:
        print('-----METRIC-----')
        print(vars(self.metric))

    def print_state(self) -> None:
        print('-----STATE-----')
        print(vars(self.state))
