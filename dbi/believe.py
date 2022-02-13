from communication.environment_controller import EnvironmentController
from dbi.metric import Metric
from dbi.state import State

from simulator.environment import Environment


class Believe:
    metric = Metric()
    state = State()

    def __call__(self) -> None:
        return

    def observe_environment_with_my_sensors(self) -> Environment:
        """
        On retourne toute l'environment
        """

        # TODO On devrait se garder des listes de tous les poussières et de tous les bijoux et le stocker dans State

        return EnvironmentController().environment

