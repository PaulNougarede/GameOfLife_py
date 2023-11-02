import numpy as np
import pygame
import function.click as click


# Fonction de jeu
# width, height = taille de la fenètre
# rows, cols = taille de la grille
# speed = vitesse du jeu


def game(width, height, rows, cols, speed, rule_choice):
    # Dimensions du plateau
    # width, height = width, height

    # Dimensions de la grille
    initialRows, initialCols = rows, cols

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
    pause = False

    # Fonction pour afficher le plateau
    def display_plate(plate):
        for row in range(rows):
            for col in range(cols):
                if plate[row, col] == 1:
                    color = white
                else:
                    color = black
                pygame.draw.rect(
                    screen,
                    color,
                    (row * cell_width, col * cell_height, cell_width, cell_height),
                )

    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        count_alive = 0

        rows, cols = rows, cols
        cell_width = width // cols
        cell_height = height // rows
        center = rows // 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if rows != 1 or cols != 1:
                        rows, cols = int(rows * 0.5), int(cols * 0.5)
                elif event.key == pygame.K_UP:
                    if rows * 2 <= initialRows or cols * 2 <= initialCols:
                        rows, cols = int(rows * 2), int(cols * 2)
                elif event.key == pygame.K_SPACE:
                    rows, cols = initialRows, initialCols
                elif event.key == pygame.K_p and not pause:
                    pause = True
                elif event.key == pygame.K_s and pause:
                    pause = False

        # Vérifie si un bouton de la souris est enfoncé
        button = pygame.mouse.get_pressed()
        if button[0]:  # 0 :bouton gauche
            clickX, clickY = event.pos
            click.cliqueCase(plate, clickX, clickY, cell_width, cell_height)
            pygame.display.flip()

        display_plate(plate)
        pygame.display.flip()

        if not pause:
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
