"""
C'est l'algorithme de recherche
"""
from dbi.state import State


class Desire:
    def __call__(self) -> None:
        return

    def execute_exploration(self, state: State) -> []:
        # Récupère la position du robot
        x = state.x
        y = state.y

        # TODO Calculer le bon résultat
        action_plan = ['left', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'aspire', 'collect']
        return action_plan

