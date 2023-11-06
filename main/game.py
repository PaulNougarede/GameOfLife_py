import numpy as np
import pygame
from pygame.locals import *
import function.click as click
import sys


# Fonction de jeu
# width, height = taille de la fenètre
# rows, cols = taille de la grille
# speed = vitesse du jeu


def game(width, height, rows, cols, speed, rule_choice):
    # Dimensions du plateau
    # width, height = width, height

    # Dimensions de la grille
    game_width, game_height = 1100, 800 #taille du plateau de jeu
    
    initialRows, initialCols = rows, cols

    plate = np.random.choice([0, 1], size=(rows, cols))

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    white = (255, 255, 255)
    black = (0, 0, 0)

    # Tailles de cellule
    cell_width = game_width // cols
    cell_height = game_height // rows

    # Tableaux de Cellules vivantes et Itérations
    alives = []
    pause = False
    
    iconePause1 = pygame.image.load("main/images/icone_pause_1.png").convert_alpha() #icone quitter le jeu
    iconePause1 = pygame.transform.scale(iconePause1, (53, 53)) #mise à l'échelle
    
    iconePause2 = pygame.image.load("main/images/icone_pause_1.png").convert_alpha() #icone quitter le jeu
    iconePause2 = pygame.transform.scale(iconePause2, (53, 53)) #mise à l'échelle
    
    iconeStop = pygame.image.load("main/images/icone_stop.png").convert_alpha() #icone quitter le jeu
    iconeStop = pygame.transform.scale(iconeStop, (45, 45)) #mise à l'échelle
    
    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha() #icone quitter le jeu
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50)) #mise à l'échelle
    
    iconeZoomArriere = pygame.image.load("main/images/icone_zoom_-.png").convert_alpha() #icone quitter le jeu
    iconeZoomArriere = pygame.transform.scale(iconeZoomArriere, (50, 50)) #mise à l'échelle
    
    iconeZoomAvant = pygame.image.load("main/images/icone_zoom_+.png").convert_alpha() #icone quitter le jeu
    iconeZoomAvant = pygame.transform.scale(iconeZoomAvant, (50, 50)) #mise à l'échelle

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

    def drawPlate(screen, initialRows, initialCols, rows, cols, pause):
    
        fondNoir = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1400, 800))
    
        screen.blit(iconePause1, (1150, 20))
        screen.blit(iconeStop, (1230, 23))
        screen.blit(iconeQuitter, (1300, 20))
        screen.blit(iconeZoomArriere, (1170, 700))
        screen.blit(iconeZoomAvant, (1270, 700))
        
        cadreGris = pygame.draw.rect(screen, (191, 191, 191), (1150, 100, 200, 550)) #cadre gris pour les infos de jeu
        
    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        
        drawPlate(screen, initialRows, initialCols, rows, cols, pause)
         
        count_alive = 0

        rows, cols = rows, cols
        cell_width = game_width // cols
        cell_height = game_height // rows
        center = rows // 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quitter
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: #zoom +
                    if rows != 1 or cols != 1:
                        rows, cols = int(rows * 0.5), int(cols * 0.5)
                elif event.key == pygame.K_UP: #zoom -
                    if rows * 2 <= initialRows or cols * 2 <= initialCols:
                        rows, cols = int(rows * 2), int(cols * 2)
                elif event.key == pygame.K_SPACE: #revenir à la taille initiale
                    rows, cols = initialRows, initialCols
                elif event.key == pygame.K_p and not pause: #pause
                    pause = True
                elif event.key == pygame.K_s and pause: #start
                    pause = False
                    
        # conditions pour les icones
        
        button = pygame.mouse.get_pressed()
        if button[0]:  # 0 :bouton gauche
            mouse_x, mouse_y = pygame.mouse.get_pos() #coordonnées de la souris
            if 1300 <= mouse_x <= 1300 + iconeQuitter.get_width() and 20 <= mouse_y <= 20 + iconeQuitter.get_height(): #si la souris est sur l'icône quitter
                sys.exit()
            
            elif 1230 <= mouse_x <= 1230 + iconeStop.get_width() and 23 <= mouse_y <= 23 + iconeStop.get_height(): #si la souris est sur l'icône stop
                sys.exit() #remplacer par la sauvegarde
                    
            elif 1170 <= mouse_x <= 1170 + iconeZoomArriere.get_width() and 700 <= mouse_y <= 700 + iconeZoomArriere.get_height(): #si la souris est sur l'icône zoom arrière
                if rows * 2 <= initialRows or cols * 2 <= initialCols:
                        rows, cols = int(rows * 2), int(cols * 2)
                    
            elif 1270 <= mouse_x <= 1270 + iconeZoomAvant.get_width() and 700 <= mouse_y <= 700 + iconeZoomAvant.get_height(): #si la souris est sur l'icône zoom avant
                if rows != 1 or cols != 1:
                        rows, cols = int(rows * 0.5), int(cols * 0.5)
                            
            elif 1150 <= mouse_x <= 1150 + iconePause1.get_width() and 20 <= mouse_y <= 20 + iconePause1.get_height(): #si la souris est sur l'icône pause 1
                if not pause:    
                    screen.blit(iconePause2, (1150, 20))
                    pause = True
                elif pause:    
                    screen.blit(iconePause1, (1150, 20))
                    pause = False
        
            #click.cliqueCase(plate, mouse_x, mouse_y, cell_width, cell_height)

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
