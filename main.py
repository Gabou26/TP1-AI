"""
TP 1

"""
import time

from communication.display import Display
from communication.thread_manager import ThreadManager


def main() -> None:
    """
    Démarrage de tous les composants du tp et affichage du résultat
    """
    display = Display()
    tm = ThreadManager()
    tm.start()

    while 1:
        time.sleep(2)
        display.print()


if __name__ == '__main__':
    main()
