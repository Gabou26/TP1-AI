"""
Affichage
"""


class Display:

    def __call__(self) -> None:
        return

    def print(self, matrix):
        """
        Affichage de la matrice
        """
        for y in range(len(matrix)):
            print(matrix[y])
        pass
