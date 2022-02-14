"""
TP 1

"""
import time

from communication.display import Display
from communication.thread_manager import ThreadManager
from simulator.tweak import Tweak

def main() -> None:
    """
    Démarrage de tous les composants du tp et affichage du résultat
    """
    tweak = Tweak()
    display = Display()
    tm = ThreadManager()
    tm.start_robot(tweak.robot_loop_sleep)
    tm.start_generator(tweak.generator_loop_sleep)

    while 1:
        time.sleep(tweak.refresh_display_loop_sleep)
        display.print()


if __name__ == '__main__':
    main()
