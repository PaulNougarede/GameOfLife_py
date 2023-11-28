import numpy as np
import pygame
from pygame.locals import *
import function.click as click
import time
import save as Save
import forme as Forme
import menu as Menu
from scipy.signal import convolve2d


# Tableaux de Cellules vivantes et Itérations
alives = []
dead = []
calculTime = []

def game(width, height, speed, info):

    # Recuperation des donnes de configuration 
    rule_choice = info[0]
    plate = info[1]
    nbr_tour = info[2]
    rows = info[3]
    cols = info[4]
    mode = info[5]
    offsetX = 0
    offsetY = 0
    scale = 1

    # Dimensions du plateau
    game_width, game_height = 800, 800
    initialRows, initialCols = rows, cols

    # random plate
    if len(plate)==0:
        if mode == 1:
            plate = np.random.choice([0,1], size=(rows, cols))
        else :
            plate = np.zeros((rows, cols), dtype=int)

    # init display
    #pygame.init()
    screen = pygame.display.set_mode((width, height))
    white = (255, 255, 255)
    black = (0, 0, 0)
    eceColor = (0,122,123)

    # Tailles de cellule
    cell_width = game_width // cols
    cell_height = game_height // rows

    # Tableaux de Cellules vivantes et Itérations
    alives = []
    dead = []
    calculTime = []

    # init image
    iconePause1 = pygame.image.load("main/images/icone_pause_1.png").convert_alpha()
    iconePause1 = pygame.transform.scale(iconePause1, (53, 53))
    iconePause2 = pygame.image.load("main/images/icone_pause_1.png").convert_alpha()
    iconePause2 = pygame.transform.scale(iconePause2, (53, 53))
    iconeStop = pygame.image.load("main/images/icone_stop.png").convert_alpha()
    iconeStop = pygame.transform.scale(iconeStop, (45, 45))
    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha()
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50))
    iconeZoomArriere = pygame.image.load("main/images/icone_zoom_-.png").convert_alpha()
    iconeZoomArriere = pygame.transform.scale(iconeZoomArriere, (50, 50))
    iconeZoomAvant = pygame.image.load("main/images/icone_zoom_+.png").convert_alpha()
    iconeZoomAvant = pygame.transform.scale(iconeZoomAvant, (50, 50))
    iconeCellulesEnVie = pygame.image.load("main/images/icone_cellules_en_vie.png").convert_alpha()
    iconeCellulesEnVie = pygame.transform.scale(iconeCellulesEnVie, (50, 50))
    iconeCellulesMortes = pygame.image.load("main/images/icone_cellules_mortes.png").convert_alpha()
    iconeCellulesMortes = pygame.transform.scale(iconeCellulesMortes, (50, 50))
    iconeTempsDeCalcul = pygame.image.load("main/images/icone_temps_de_calcul.png").convert_alpha()
    iconeTempsDeCalcul = pygame.transform.scale(iconeTempsDeCalcul, (50, 50))
    iconeNombreDeTours = pygame.image.load("main/images/icone_nombre_de_tours.png").convert_alpha()
    iconeNombreDeTours = pygame.transform.scale(iconeNombreDeTours, (50, 50))
    iconeVitessePlus = pygame.image.load("main/images/icone_vitesse_plus.png").convert_alpha()
    iconeVitessePlus = pygame.transform.scale(iconeVitessePlus, (50, 50))
    iconeVitesseMoins = pygame.image.load("main/images/icone_vitesse_moins.png").convert_alpha()
    iconeVitesseMoins = pygame.transform.scale(iconeVitesseMoins, (50, 50))

    # Fonction pour afficher uniquement les cellules modifiées
    def displayPlate(plate):
        screen.fill((40,40,40))
        mid = rows // 2
        for row in range(rows):
            for col in range(cols):
                if plate[row, col] == 1:
                    color = white
                elif row == mid and col == mid:
                    color = eceColor
                else:
                    color = black
                rect = ((row * cell_width * scale) + offsetX, (col * cell_height * scale) + offsetY, cell_width * scale, cell_height * scale)
                pygame.draw.rect(screen,color,rect)
                pygame.draw.rect(screen,(40,40,40),rect,1)



    # def display_grid(partie,screen):
    # screen.fill((255,255,255))
    # for i in range(partie.grid_size[0]):
    #     for j in range(partie.grid_size[1]):
    #         x = partie.offset[0]+i*int(partie.scale*partie.cell_size)
    #         y = partie.offset[1]+j*int(partie.scale*partie.cell_size)
    #         w = int(partie.scale*partie.cell_size)
    #         if partie.grid[i,j]==1:
    #             pygame.draw.rect(screen, (12,np.random.randint(0,255),12), (x, y, w, w))
    #         if partie.grid[i,j]==0:
    #             pygame.draw.rect(screen, (0,0,0), (x, y, w, w), 1)

    def drawPlate(screen, alives, dead, tour):
        pygame.draw.rect(screen,(0,0,0),(1100, 0, 300, 800))
        screen.blit(iconePause1, (1150, 20))
        screen.blit(iconeStop, (1230, 23))
        screen.blit(iconeQuitter, (1300, 20))
        Menu.draw_text("Zoom :", pygame.font.SysFont("Futura", 30), white, 1145, 620, screen) #zoom
        screen.blit(iconeZoomAvant, (1145, 660))
        screen.blit(iconeZoomArriere, (1145, 720))
        Menu.draw_text("Vitesse :", pygame.font.SysFont("Futura", 30), white, 1290, 620, screen) #vitesse
        screen.blit(iconeVitessePlus, (1300, 660))
        screen.blit(iconeVitesseMoins, (1300, 720))

        #infos de jeu
        font=pygame.font.SysFont("Futura", 30) #police d'écriture
        text_alive = font.render("Cellules en vie :", True, white)
        screen.blit(iconeCellulesEnVie, (1190, 190))
        screen.blit(text_alive, (1170,150))
        text_dead = font.render("Cellules mortes :", True, white)
        screen.blit(iconeCellulesMortes, (1190, 310))
        screen.blit(text_dead, (1170,270))
        text_dead = font.render("Temps de calcul :", True, white)
        screen.blit(iconeTempsDeCalcul, (1190, 420))
        screen.blit(text_dead, (1170,380))
        if alives :
            nbr_cellule = str(alives[-1])
            affichage_nbr_cellule = font.render(nbr_cellule, True, white)
            screen.blit(affichage_nbr_cellule, (1270,205))
        if dead :
            nbr_mort = str(dead[-1])
            affichage_nbr_mort = font.render(nbr_mort, True, white)
            screen.blit(affichage_nbr_mort, (1270, 325))
        if calculTime :
            time = str(calculTime[-1])
            affichage_time = font.render(time, True, white)
            screen.blit(affichage_time, (1270, 435))

        text_tour = font.render("Nombre de tours :", True, white)
        screen.blit(text_tour, (1170,510))
        nbr_tour = str(tour)
        affichage_nbr_tour = font.render(nbr_tour, True, white)
        screen.blit(iconeNombreDeTours, (1190, 540))
        screen.blit(affichage_nbr_tour, (1270,555))

    
    # Fonction pour obtenir l'état d'une cellule avec des bords toriques
    def get_cell(x, y):
        return plate[x % rows, y % cols]

    nbr_tour = int(nbr_tour)

    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    pause = False

    while running:
        count_alive = 0
        count_dead = 0
        testA = False
        testZ = False
        testE = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                isClicked = event.key
                if isClicked == pygame.K_LEFT:
                    offsetX -= 10
                if isClicked == pygame.K_RIGHT:
                    offsetX += 10 
                if isClicked == pygame.K_UP:
                    offsetY -= 10
                if isClicked == pygame.K_DOWN:
                    offsetY += 10
                if isClicked == pygame.K_a:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    Forme.square(plate, mouse_x , mouse_y, cell_width, cell_height, scale, offsetX, offsetY)
                if isClicked == pygame.K_z:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    Forme.planner(plate, mouse_x , mouse_y, cell_width, cell_height, scale, offsetX, offsetY)
                if isClicked == pygame.K_e:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    Forme.canon(plate, mouse_x , mouse_y, cell_width, cell_height, scale, offsetX, offsetY)
                if isClicked == pygame.K_c:
                    plate = np.zeros((rows, cols), dtype=int)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (1300 <= mouse_x <= 1300 + iconeQuitter.get_width()and 20 <= mouse_y <= 20 + iconeQuitter.get_height()):
                        running = False
                    elif (1230 <= mouse_x <= 1230 + iconeStop.get_width()and 23 <= mouse_y <= 23 + iconeStop.get_height()):
                        Save.save(info, nbr_tour)
                    elif (1150 <= mouse_x <= 1150 + iconePause1.get_width()and 20 <= mouse_y <= 20 + iconePause1.get_height()):
                        if not pause:
                            screen.blit(iconePause2, (1150, 20))
                            pause = True
                        elif pause:
                            screen.blit(iconePause1, (1150, 20))
                            pause = False
                    elif (1300 <= mouse_x <= 1300 + iconeVitesseMoins.get_width() and 720 <= mouse_y <= 720 + iconeVitesseMoins.get_height()):
                        if speed -1 > 0:
                            speed -= 1
                    elif (1300 <= mouse_x <= 1300 + iconeVitessePlus.get_width() and 660 <= mouse_y <= 660 + iconeVitessePlus.get_height()):
                        speed +=1
                    else:
                        click.cliqueCase(plate, mouse_x, mouse_y, cell_width, cell_height, scale, offsetX, offsetY)
                elif event.button == 4:  # Molette vers le haut (zoom in)
                    old_scale = scale
                    scale += 1
                    # Ajustez l'offset pour zoomer à l'endroit où se trouve la souris
                    offsetX -= (pygame.mouse.get_pos()[0] - offsetX) * (scale / old_scale - 1)
                    offsetY -= (pygame.mouse.get_pos()[1] - offsetY) * (scale / old_scale - 1)
                elif event.button == 5:  # Molette vers le bas (zoom out)
                    if scale - 1 > 0:
                        old_scale = scale
                        scale -= 1
                        # Ajustez l'offset pour zoomer à l'endroit où se trouve la souris
                        offsetX -= (pygame.mouse.get_pos()[0] - offsetX) * (scale / old_scale - 1)
                        offsetY -= (pygame.mouse.get_pos()[1] - offsetY) * (scale / old_scale - 1)


        displayPlate(plate)
        drawPlate(screen, alives, dead, nbr_tour)
        pygame.display.flip()

        if not pause:
            nbr_tour += 1
            new_plate = plate.copy()
            start = time.process_time()
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
                            count_dead +=1
                            new_plate[row, col] = 0
                    else:
                        if rule_choice == 1 :
                            if count == 3:
                                new_plate[row, col] = 1
                        else :
                            if count == 1:
                                new_plate[row, col] = 1
            end = time.process_time()

            calculTime.append(end-start)
            alives.append(count_alive)
            dead.append(count_dead)
            plate = new_plate

        clock.tick(speed)  # Ajustez la vitesse d'itération

    # Quittez Pygame
    return (alives, calculTime, dead)


def simulation(width, height, speed, info):

    # Recuperation des donnes de configuration 
    plate = info[1]
    rows = info[3]
    cols = info[4]
    mode = info[5]

    screen = pygame.display.set_mode((width, height))

    font=pygame.font.SysFont("Futura", 30) #police d'écriture
    text_chargement = font.render("Simulation en cours..." , True, (255,255,255))

    screen.blit(text_chargement, (600,500))
    pygame.display.flip()

    total = rows * cols

    def update_board(plate):
        kernel = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]])

        neighbors_count = convolve2d(plate, kernel, mode='same', boundary='wrap')

        new_plate = np.zeros_like(plate)
        new_plate[(plate == 1) & ((neighbors_count == 2) | (neighbors_count == 3))] = 1
        new_plate[(plate == 0) & (neighbors_count==3)]=1

        return new_plate

    # random plate
    if len(plate)==0:
        if mode == 1:
            plate = np.random.choice([0,1], size=(rows, cols))
        else :
            plate = np.zeros((rows, cols), dtype=int)
    
    
    for i in range(500):
        start = time.process_time()
        plate = update_board(plate)
        end = time.process_time()
        calculTime.append(end-start)
        count_alive = np.sum(plate)
        count_dead = total - count_alive
        dead.append(count_dead)
        alives.append(count_alive)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # Quittez Pygame
    return (alives, calculTime, dead) 
    