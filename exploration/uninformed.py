"""
Légende: Actions Robot
0-Gauche
1-Droite
2-Haut
3-Bas
4-Aspirer
5-Cueillir
"""


class Uninformed:
    def __call__(self) -> None:
        return

    #Params : Pos Robot - Pos Destination
    def calculate_path(self, robot_x, robot_y, dest_x, dest_y, matrix) -> []:
        pos_cour_x = robot_x
        pos_cour_y = robot_y
        path = []

        #Calcul Différentiel
        diff_x = dest_x - robot_x
        diff_y = dest_y - robot_y

        # Mouv X
        while diff_x != 0:
            if diff_x > 0:
                pos_cour_x += 1
                diff_x -= 1
                path.append(1)
            elif diff_x < 0:
                pos_cour_x -= 1
                diff_x += 1
                path.append(0)
            if self.contains_dust(pos_cour_x, pos_cour_y, matrix):
                path.append(4)

        # Mouv Y
        while diff_y != 0:
            if diff_y > 0:
                pos_cour_y += 1
                diff_y -= 1
                path.append(2)
            elif diff_y < 0:
                pos_cour_y -= 1
                diff_y += 1
                path.append(3)

            #Check Actions
            if self.contains_dust(pos_cour_x, pos_cour_y, matrix):
                path.append(4)
            elif self.contains_jewel(pos_cour_x, pos_cour_y, matrix):
                path.append(5)

        return path

    def contains_dust(self, pos_x, pos_y, matrix):
        data_id = matrix[pos_x, pos_y]
        if data_id == 1 or data_id == 3:
            return True
        return False

    def contains_jewel(self, pos_x, pos_y, matrix):
        if matrix[pos_x, pos_y] == 2:
            return True
        return False