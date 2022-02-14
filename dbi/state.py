"""
Tous les indicateurs de performance que le robot possède
"""
from dbi.metric import Metric
from simulator.environment import Environment


class State:
    x = None
    y = None
    action_plan = None
    all_peace_is_clean = False
    collected_all_jewel = False

    def __call__(self) -> None:
        return

    def set_current_position(self, x, y) -> None:
        """
        Met à jour la position actuel du robot
        """
        self.x = x
        self.y = y

    def update(self, environment: Environment, metric: Metric) -> None:
        """
        Met à jour tous les états de l'agent
        """

        # self.set_current_position(environment.robot_position_x, environment.robot_position_y)
        self.x = environment.robot_position_x
        self.y = environment.robot_position_y

        # TODO Utiliser les metrics pour mettre des infos dans l'état
        pass
