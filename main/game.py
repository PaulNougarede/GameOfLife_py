import numpy as np
import pygame


# Fonction de jeu
# width, height = taille de la fenètre
# rows, cols = taille de la grille
# speed = vitesse du jeu


def game(width, height, rows, cols, speed, rule_choice):
    # Dimensions du plateau
    width, height = width, height

    # Dimensions de la grille
    rows, cols = rows, cols

    plate = np.random.choice([0, 1], size=(rows, cols))

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)

    # Tailles de cellule
    cell_width = width // cols
    cell_height = height // rows

    # Tableaux de Cellules vivantes et Itérations
    alives = []
    ite = 0

    # Fonction pour afficher le plateau
    def display_plate(plate):
        count = 0
        for row in range(rows):
            for col in range(cols):
                if plate[row, col] == 1:
                    color = white
                    count += 1
                else:
                    color = black
                pygame.draw.rect(
                    screen,
                    color,
                    (col * cell_width, row * cell_height, cell_width, cell_height),
                )

    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        count_alive = 0
        ite += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_plate(plate)
        pygame.display.flip()

        new_plate = plate.copy()

        for row in range(rows):
            for col in range(cols):
                count = (
                    get_cell(row - 1, col - 1)
                    + get_cell(row - 1, col)
                    + get_cell(row - 1, col + 1)
                    + get_cell(row, col - 1)
                    + get_cell(row, col + 1)
                    + get_cell(row + 1, col - 1)
                    + get_cell(row + 1, col)
                    + get_cell(row + 1, col + 1)
                )

                if plate[row, col] == 1:
                    count_alive += 1
                    if count < 2 or count > 3:
                        new_plate[row, col] = 0
                else:
                    if count == 3:
                        new_plate[row, col] = 1

        alives.append(count_alive)

        plate = new_plate

        clock.tick(speed)  # Ajustez la vitesse d'itération

    # Quittez Pygame
    pygame.quit()
    return alives
