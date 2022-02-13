"""
Controller pour utiliser l'environement
Rend l'écriture dans l'environment thread safe
"""
from simulator.environment import Environment
from threading import Lock


class EnvironmentController:
    environment = Environment(5, 5, 2, 2)
    lock = Lock()

    def __call__(self) -> None:
        return

    def add(self, x, y, data_id) -> None:
        # Pour gérer le multithread
        self.lock.acquire()
        self.environment.add_slot_data(x, y, data_id)
        self.lock.release()

    def set_robot_position(self, x, y) -> None:
        self.lock.acquire()
        self.environment.set_robot_position()
        self.lock.release()
