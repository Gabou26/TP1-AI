"""
Exécution des actions
"""
from communication.environment_controller import EnvironmentController


class Intention:
    environment_controller = EnvironmentController()

    def __call__(self) -> None:
        return

    def execute_action_plan(self, action_plan: []) -> []:

        if not action_plan:
            print("Aucun plan d'action à faire")
            return []
        next_move = action_plan[0]
        print("print next move". next_move)
        updated_metric = []
        # TODO Vérifier si les directions sont les bonnes
        if next_move == 2:
            # Haut
            self.environment_controller.environment.robot_position_y -= 1
            updated_metric.append('move')
        if next_move == 3:
            # Bas
            self.environment_controller.environment.robot_position_y += 1
            updated_metric.append('move')
        if next_move == 1:
            # Left
            self.environment_controller.environment.robot_position_x -= 1
            updated_metric.append('move')
        if next_move == 0:
            # Gauche
            self.environment_controller.environment.robot_position_x += 1
            updated_metric.append('move')
        if next_move == 4:
            # TODO Aspirer ce qui est sur cette case
            print('Aspire')
            # TODO Updater les bonnes métriques
            updated_metric.append('aspired_dust')
            updated_metric.append('aspired_jewel')
        if next_move == 5:
            # TODO Collect
            updated_metric.append('collected_jewel')
        return updated_metric
