import numpy as np
import pygame


# Dimensions du plateau
width, height = 800, 800

# Dimensions de la grille
rows, cols = 100, 100

# Créez un tableau NumPy pour représenter le plateau
plate = np.random.choice([0, 1], size=(rows, cols))

# Initialisation de Pygame
pygame.init()

# Créez une fenêtre Pygame
screen = pygame.display.set_mode((width, height))

# Couleurs
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

    # Affichez le plateau à chaque itération
    display_plate(plate)
    pygame.display.flip()

    # Créez une copie temporaire du plateau pour mettre à jour les cellules
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

    # Mettez à jour le plateau
    plate = new_plate

    clock.tick(10)  # Ajustez la vitesse d'itération selon votre préférence

# Quittez Pygame
pygame.quit()
