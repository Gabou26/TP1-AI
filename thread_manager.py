"""
Gère les threads
"""
import threading
import time

from robot import Robot
from generator import Generator

def robot_loop(sleep) -> None:
    """
    Boucle sans fin du robot
    """
    robot = Robot()
    robot.boot()

    while robot.am_i_alive:
        time.sleep(sleep)
        robot.execute()


def environment_generator_loop(sleep) -> None:
    """
    Boucle sans fin de l'environment
    """
    generator = Generator()
    generator.boot()

    while generator.am_i_alive:
        time.sleep(sleep)
        generator.execute()


class ThreadManager:
    robot_sleep_second = 2
    generator_sleep_second = 3

    def __call__(self) -> None:
        return

    def start(self):
        """
        Démarre tous les threads
        """
        # Programme le thread sur la function loop
        generator = threading.Thread(target=environment_generator_loop, args=(self.generator_sleep_second,))
        generator.start()

        robot = threading.Thread(target=robot_loop, args=(self.robot_sleep_second,))
        robot.start()
        pass
