from communication.environment_controller import EnvironmentController
from dbi.metric import Metric
from dbi.state import State
from robot.sensor import Sensor

from simulator.environment import Environment


class Believe:
    metric = Metric()
    state = State()
    sensor = Sensor()

    def __call__(self) -> None:
        return

    def observe_environment_with_my_sensors(self) -> Environment:
        """
        Entièrement observable
        """

        # TODO On devrait se garder des listes de tous les poussières et de tous les bijoux et le stocker dans State

        #sensor.get_dust_and_jewel();

        #all_peace_is_clean = True

        #collected_all_jewel = True

        return EnvironmentController().environment

