"""
TP 1

"""
import time

from thread_manager import ThreadManager


def main() -> None:
    """
    Démarrage de tous les composants du tp et affichage du résultat
    """

    tm = ThreadManager()
    tm.start()

    while 1:
        time.sleep(1)


if __name__ == '__main__':
    main()
