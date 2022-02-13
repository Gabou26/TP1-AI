"""
Exécution des actions
"""
from communication.environment_controller import EnvironmentController


class Intention:
    environment_controller = EnvironmentController()

    def __call__(self) -> None:
        return

    def execute_action_plan(self, action_plan: []) -> []:
        next_move = action_plan[0]
        updated_metric = []
        # TODO Vérifier si les directions sont les bonnes
        if next_move == 'up':
            self.environment_controller.environment.robot_position_y -= 1
            updated_metric.append('move')
        if next_move == 'down':
            self.environment_controller.environment.robot_position_y += 1
            updated_metric.append('move')
        if next_move == 'left':
            self.environment_controller.environment.robot_position_x -= 1
            updated_metric.append('move')
        if next_move == 'right':
            self.environment_controller.environment.robot_position_x += 1
            updated_metric.append('move')
        if next_move == 'aspire':
            # TODO Aspirer ce qui est sur cette case
            print ('aspire')
            # TODO Updater les bonnes métriques
            updated_metric.append('aspired_dust')
            updated_metric.append('aspired_jewel')
        if next_move == 'collect':
            # TODO Collect
            updated_metric.append('collected_jewel')
        return updated_metric
