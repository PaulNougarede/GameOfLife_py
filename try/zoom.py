import numpy as np
import pygame
import main.menu as Menu


def game(width, height, rows, cols, speed, rule_choice):
    # Dimensions de la grille de jeau
    initialRows, initialCols = rows, cols

    plate = np.random.choice([0, 1], size=(rows, cols))

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)

    # Tailles de cellule
    cell_width = width // cols
    cell_height = height // rows
    print("size of X : ", cell_width, "size of Y : ", cell_height)
    print("size2 of X : ", width // cols, "size2 of Y : ", height // rows)

    # Tableaux de Cellules vivantes et Itérations
    alives = []
    ite = 0

    # Fonction pour afficher le plateau
    def display_plate(plate, cell_width, cell_height):
        count = 0
        for row in range(rows):
            for col in range(cols):
                if plate[row, col] == 1:
                    color = white
                    count += 1
                else:
                    color = black
                # pygame.draw.rect(screen,color,(col * cell_width, row * cell_height, cell_width, cell_height))
                pygame.draw.rect(
                    screen,
                    color,
                    (row * cell_width, col * cell_height, cell_width, cell_height),
                )

    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    def cliqueCase(plate, screen, black, clickX, clickY):
        turn = 0
        while clickX > cell_width:
            turn += 1
            clickX = clickX - cell_width

        placeX = turn * cell_width
        turn = 0

        while clickY > cell_height:
            turn += 1
            clickY = clickY - cell_height

        placeY = turn * cell_height

        plate[int(placeX / cell_width)][int(placeY / cell_height)] = 1
        pygame.draw.rect(screen, black, (placeX, placeY, cell_width, cell_height))
        print(
            "X TABLE : ",
            int(placeX / cell_width),
            "AND Y TABLE : ",
            int(placeY / cell_height),
        )

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        count_alive = 0
        ite += 1

        rows, cols = rows, cols
        cell_width = width // cols
        cell_height = height // rows

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

        # Vérifie si un bouton de la souris est enfoncé
        button = pygame.mouse.get_pressed()
        if button[0]:  # 0 :bouton gauche
            clickX, clickY = event.pos
            print("Clique droit enfoncé X:", clickX, "Y:", clickY)
            cliqueCase(plate, screen, white, clickX, clickY)
            pygame.display.flip()

        display_plate(plate, cell_width, cell_height)
        Menu.draw_text(
            screen,
            f"{rows}*{cols}",
            pygame.font.SysFont("Futura", 20),
            (255, 0, 0),
            0,
            0,
        )
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
