import numpy as np
import pygame
from pygame.locals import *
import function.click as click
import sys
import menu as Menu
import save as Save


def game(width, height, rows, cols, speed, rule_choice, plate, nbr_tour):

    # Dimensions du plateau
    game_width, game_height = 1100, 800
    initialRows, initialCols = rows, cols

    # random plate
    if len(plate)==0:
        plate = np.random.choice([0, 1], size=(rows, cols))

    # init display
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Tailles de cellule
    cell_width = game_width // cols
    cell_height = game_height // rows

    # Tableaux de Cellules vivantes et Itérations
    alives = []
    dead = []

    # init image
    iconePause1 = pygame.image.load(
        "main/images/icone_pause_1.png").convert_alpha()
    iconePause1 = pygame.transform.scale(iconePause1, (53, 53))
    iconePause2 = pygame.image.load(
        "main/images/icone_pause_1.png").convert_alpha()
    iconePause2 = pygame.transform.scale(iconePause2, (53, 53))
    iconeStop = pygame.image.load("main/images/icone_stop.png").convert_alpha()
    iconeStop = pygame.transform.scale(iconeStop, (45, 45))
    iconeQuitter = pygame.image.load(
        "main/images/icone_quitter.png").convert_alpha()
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50))
    iconeZoomArriere = pygame.image.load(
        "main/images/icone_zoom_-.png").convert_alpha()
    iconeZoomArriere = pygame.transform.scale(iconeZoomArriere, (50, 50))
    iconeZoomAvant = pygame.image.load(
        "main/images/icone_zoom_+.png").convert_alpha()
    iconeZoomAvant = pygame.transform.scale(iconeZoomAvant, (50, 50))

    # Fonction pour afficher uniquement les cellules modifiées
    def displayPlate(plate):
        for row in range(rows):
            for col in range(cols):
                if plate[row, col] == 1:
                    color = white
                else:
                    color = black
                pygame.draw.rect(screen,color,(row * cell_width, col * cell_height, cell_width, cell_height),)

    def drawPlate(screen, alives, dead, tour):
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1400, 800))
        screen.blit(iconePause1, (1150, 20))
        screen.blit(iconeStop, (1230, 23))
        screen.blit(iconeQuitter, (1300, 20))
        screen.blit(iconeZoomArriere, (1170, 700))
        screen.blit(iconeZoomAvant, (1270, 700))
        pygame.draw.rect(screen, (191, 191, 191), (1150, 100, 200, 550))  # cadre gris pour les infos de jeu

        #Info de jeu
        font=pygame.font.SysFont("Futura", 30)
        text_alive = font.render("Cellule en vie :", True, (255,255,255))
        screen.blit(text_alive, (1160,130))
        text_dead = font.render("Cellule morte :", True, (255,255,255))
        screen.blit(text_dead, (1160,180))
        if alives :
            nbr_cellule = str(alives[-1])
            affichage_nbr_cellule = font.render(nbr_cellule, True, (9,120,0))
            screen.blit(affichage_nbr_cellule, (1190,150))
        if dead :
            nbr_mort = str(dead[-1])
            affichage_nbr_mort = font.render(nbr_mort, True, (120,9,0))
            screen.blit(affichage_nbr_mort, (1190, 200))
        
        text_tour = font.render("Nombre de tour :", True, (255,255,255))
        screen.blit(text_tour, (1160,500))
        nbr_tour = str(tour)
        affichage_nbr_tour = font.render(nbr_tour, True, (255,255,255))
        screen.blit(affichage_nbr_tour, (1190,520))
        


    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    pause = False

    nbr_tour = int(nbr_tour)


    while running:
        count_alive = 0
        count_dead = 0
        nbr_tour += 1
        rows, cols = rows, cols
        cell_width = game_width // cols
        cell_height = game_height // rows

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (1300 <= mouse_x <= 1300 + iconeQuitter.get_width()and 20 <= mouse_y <= 20 + iconeQuitter.get_height()):
                        sys.exit()
                    elif (1230 <= mouse_x <= 1230 + iconeStop.get_width()and 23 <= mouse_y <= 23 + iconeStop.get_height()):
                        Save.save(plate, nbr_tour, rule_choice)
                    elif (1170 <= mouse_x <= 1170 + iconeZoomArriere.get_width()and 700 <= mouse_y <= 700 + iconeZoomArriere.get_height()):
                        if rows * 2 <= initialRows or cols * 2 <= initialCols:
                            rows, cols = int(rows * 2), int(cols * 2)
                    elif (1270 <= mouse_x <= 1270 + iconeZoomAvant.get_width()and 700 <= mouse_y <= 700 + iconeZoomAvant.get_height()):
                        if rows != 1 or cols != 1:
                            rows, cols = int(rows * 0.5), int(cols * 0.5)
                    elif (1150 <= mouse_x <= 1150 + iconePause1.get_width()and 20 <= mouse_y <= 20 + iconePause1.get_height()):
                        if not pause:
                            screen.blit(iconePause2, (1150, 20))
                            pause = True
                        elif pause:
                            screen.blit(iconePause1, (1150, 20))
                            pause = False
                    else:
                        click.cliqueCase(plate, mouse_x, mouse_y, cell_width, cell_height)

        drawPlate(screen, alives, dead, nbr_tour)
        displayPlate(plate)
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
                        count_dead +=1
                        if count == 3:
                            new_plate[row, col] = 1

            alives.append(count_alive)
            dead.append(count_dead)
            plate = new_plate

        clock.tick(speed)  # Ajustez la vitesse d'itération

    # Quittez Pygame
    pygame.quit()

    return alives
