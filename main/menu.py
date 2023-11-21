import pygame, sys, time
from pygame.locals import *
import save as Save
import graphs.graphAlive as Graph

def draw_text(text, font, color, x, y, screen):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

def principeDuJeu(screen):
    
    vert = (0, 122, 123) #définition couleur verte du jeu

    screen.fill(vert)  #couleur fond
    iconeRetour = pygame.image.load("main/images/icone_fleche_arriere.png").convert_alpha()  # icone fleche retour
    iconeRetour = pygame.transform.scale(iconeRetour, (150, 150))  # mise à l'échelle
    screen.blit(iconeRetour, (50, 50))

    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha() #icone quitter le jeu
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50)) #mise à l'échelle
    screen.blit(iconeQuitter, (1330, 20))
    
    pygame.display.flip()

    running = True

    while running:  # boucle infinie
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        draw_text("Principe du jeu:", pygame.font.SysFont("Futura", 80), (255, 255, 255), 500, 150,screen)
        draw_text("Le Jeu de la Vie est un automate cellulaire inventé par le mathématicien John Conway en 1970.", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 300,screen)
        draw_text("Il se déroule sur une grille bidimensionnelle infinie, où chaque cellule peut être vivante ou morte.", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 350,screen)
        draw_text("L'évolution des cellules est régie par des règles simples basées sur le nombre de voisins vivants", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 400,screen)
        draw_text("de chaque cellule.", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 450,screen)
        draw_text("Au fil des générations, des motifs complexes émergent,", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 500,screen)
        draw_text("sans aucune intervention directe du joueur.", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 550,screen)
        pygame.display.flip()
        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris
        if (
            50 <= mouse_x <= 50 + iconeRetour.get_width()
            and 50 <= mouse_y <= 50 + iconeRetour.get_height()
        ):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                return 0
            
        if (
            1330 <= mouse_x <= 1330 + iconeQuitter.get_width()
            and 20 <= mouse_y <= 20 + iconeQuitter.get_height()
        ):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                sys.exit()


def choixDesRegles(screen):
    vert = (0, 122, 123)

    screen.fill(vert)  # couleur fond
    iconeRetour = pygame.image.load("main/images/icone_fleche_arriere.png").convert_alpha()  # icone fleche retour
    iconeRetour = pygame.transform.scale(iconeRetour, (150, 150))  # mise à l'échelle
    screen.blit(iconeRetour, (50, 50))

    pygame.display.flip()
    
    running = True

    while running:  # boucle infinie
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        draw_text("Choix des règles:",pygame.font.SysFont("Futura", 80),(255, 255, 255),500,150,screen)

        bouton_regles1 = pygame.draw.rect(
            screen, (255, 255, 255), (50, 250, 1300, 200)
        )  # affichage règles 1
        draw_text("Règles 1:", pygame.font.SysFont("Futura", 40), vert, 50, 250,screen)
        draw_text("- Uniquement 2 cellules autour : meurt par isolement", pygame.font.SysFont("Futura", 40), vert, 50, 300,screen)
        draw_text("- Plus de 3 cellules autour : meurt de surpopulation ", pygame.font.SysFont("Futura", 40), vert, 50, 350,screen)
        draw_text("- 3 cellules autour de toi : naissance par invocation ", pygame.font.SysFont("Futura", 40), vert, 50, 400,screen)

        bouton_regles2 = pygame.draw.rect(screen, (255, 255, 255), (50, 500, 1300, 200))  # affichage règles 2
        draw_text("Règles 2:", pygame.font.SysFont("Futura", 40), vert, 50, 500,screen)
        draw_text("- Uniquement 2 cellules autour : meurt par isolement", pygame.font.SysFont("Futura", 40), vert, 50, 550,screen)
        draw_text("- Plus de 3 cellules autour : meurt de surpopulation", pygame.font.SysFont("Futura", 40), vert, 50, 600,screen)
        draw_text("- 1 cellules autour de toi : naissance par invocation", pygame.font.SysFont("Futura", 40), vert, 50, 650,screen)

        pygame.display.flip()

        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris
        if (50 <= mouse_x <= 50 + iconeRetour.get_width() and 50 <= mouse_y <= 50 + iconeRetour.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                return 0
                
        pygame.display.flip()

        if bouton_regles1.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_regles1 = pygame.draw.rect(
                    screen, vert, (50, 250, 1300, 200)
                )  # affichage bouton
                draw_text("Règles 1:",pygame.font.SysFont("Futura", 40),(255, 255, 255),50,250,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 300,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 350,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 400,screen)
                pygame.display.flip()
                time.sleep(0.05)
                return 1

        if bouton_regles2.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_regles2 = pygame.draw.rect(
                    screen, vert, (50, 500, 1300, 200)
                )  # affichage règles 2
                draw_text("Règles 2:",pygame.font.SysFont("Futura", 40),(255, 255, 255),50,500,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 550,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 600,screen)
                draw_text("- ", pygame.font.SysFont("Futura", 40), (255, 255, 255), 50, 650,screen)
                pygame.display.flip()
                time.sleep(0.05)
                return 2


def menu(screen):

    plate = []
    running = True

    while running:  # boucle infinie
        vert = (0, 122, 123)
        screen.fill(vert)  # couleur fond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        bouton_principeDuJeu = pygame.draw.rect(screen, (255, 255, 255), (430, 150, 550, 100))  # affichage bouton
        draw_text("Principe du jeu", pygame.font.SysFont("Futura", 80), vert, 500, 175, screen)

        bouton_nvlPartie = pygame.draw.rect(screen, (255, 255, 255), (430, 350, 550, 100))  # affichage bouton
        draw_text("Nouvelle partie", pygame.font.SysFont("Futura", 80), vert, 495, 375, screen)

        bouton_ChargerPartie = pygame.draw.rect(screen, (255, 255, 255), (430, 550, 550, 100))  # affichage bouton
        draw_text("Charger une partie", pygame.font.SysFont("Futura", 80), vert, 450, 575, screen)

        pygame.display.flip()

        if bouton_principeDuJeu.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_principeDuJeu = pygame.draw.rect(
                    screen, vert, (430, 150, 550, 100)
                )  # affichage bouton
                draw_text("Principe du jeu",pygame.font.SysFont("Futura", 80),(255, 255, 255),500,175,screen)
                pygame.display.flip()
                time.sleep(0.05)
                principeDuJeu(screen)

        if bouton_nvlPartie.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_nvlPartie = pygame.draw.rect(
                    screen, vert, (430, 350, 550, 100)
                )  # affichage bouton
                draw_text("Nouvelle partie",pygame.font.SysFont("Futura", 80),(255, 255, 255),495,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                rules = choixDesRegles(screen)
                time.sleep(0.2)
                taille = choix_taille(screen)
                time.sleep(0.2)
                mode = choix_mode(screen)
                if rules != 0:
                    return (rules, plate, 0, taille[0], taille[1], mode) #taille[0] = rows / taille[1] = cols
                
                

        if bouton_ChargerPartie.collidepoint(
            pygame.mouse.get_pos()
        ): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clc
                bouton_ChargerPartie = pygame.draw.rect(screen, vert, (430,550,550,100))
                draw_text("Charger une partie",pygame.font.SysFont("Futura", 80),(255, 255, 255),450,575,screen)
                pygame.display.flip()
                time.sleep(0.2)
                tuple_info = Save.charge_plate()

                rules_choice = tuple_info[0]
                plate = tuple_info[1]
                nbr_tour = tuple_info[2]
                rows = tuple_info[3]
                cols = tuple_info[4]
                mode = tuple_info[5]

                return (rules_choice, plate, nbr_tour,rows,cols,mode)
            

def choix_taille(screen):
    running = True

    while running:  # boucle infinie
        vert = (0, 122, 123)
        screen.fill(vert)  # couleur fond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        bouton_petit = pygame.draw.rect(screen, (255, 255, 255), (50, 350, 350, 100))  # affichage bouton
        draw_text("Petit", pygame.font.SysFont("Futura", 80), vert, 150, 375, screen)

        bouton_moyen = pygame.draw.rect(screen, (255, 255, 255), (500, 350, 350, 100))  # affichage bouton
        draw_text("Moyen", pygame.font.SysFont("Futura", 80), vert, 585, 375, screen)

        bouton_grand = pygame.draw.rect(screen, (255, 255, 255), (950, 350, 350, 100))  # affichage bouton
        draw_text("Grand", pygame.font.SysFont("Futura", 80), vert, 1035, 375, screen)

        pygame.display.flip()

        if bouton_petit.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_petit = pygame.draw.rect(
                    screen, vert, (50, 350, 350, 100)
                )  # affichage bouton
                draw_text("Petit",pygame.font.SysFont("Futura", 80),(255, 255, 255),150,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                rows = 50
                cols = 50
                return (rows, cols)

        if bouton_moyen.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_moyen = pygame.draw.rect(
                    screen, vert, (500, 350, 350, 100)
                )  # affichage bouton
                draw_text("Moyen",pygame.font.SysFont("Futura", 80),(255, 255, 255),585,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                rows = 100
                cols = 100
                return(rows, cols)
                
        if bouton_grand.collidepoint(
            pygame.mouse.get_pos()
        ): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clc
                bouton_grand = pygame.draw.rect(screen, vert, (950,350,350,100))
                draw_text("Grand",pygame.font.SysFont("Futura", 80),(255, 255, 255),1035,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                rows = 150
                cols = 150
                return(rows, cols)
            
            
def choix_mode(screen):
    running = True

    while running:  # boucle infinie
        vert = (0, 122, 123)
        screen.fill(vert)  # couleur fond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        bouton_alea = pygame.draw.rect(screen, (255, 255, 255), (100, 350, 500, 100))  # affichage bouton
        draw_text("Aléatoire", pygame.font.SysFont("Futura", 80), vert, 220, 375, screen)

        bouton_manu = pygame.draw.rect(screen, (255, 255, 255), (800, 350, 500, 100))  # affichage bouton
        draw_text("Manuel", pygame.font.SysFont("Futura", 80), vert, 940, 375, screen)

        pygame.display.flip()

        if bouton_alea.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_alea = pygame.draw.rect(
                    screen, vert, (100, 350, 500, 100)
                )  # affichage bouton
                draw_text("Aléatoire",pygame.font.SysFont("Futura", 80),(255, 255, 255),220,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                return (1)

        if bouton_manu.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_manu = pygame.draw.rect(
                    screen, vert, (800, 350, 500, 100)
                )  # affichage bouton
                draw_text("Manuel",pygame.font.SysFont("Futura", 80),(255, 255, 255),940,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                return(2)
            
def menu_graphs(screen, graphData):

    running = True

    while running:  # boucle infinie
        vert = (0, 122, 123)
        blanc = (255,255,255)
        screen.fill(vert)  # couleur fond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()

        bouton_vivante = pygame.draw.rect(screen, blanc, (50, 350, 350, 100))  # affichage bouton
        draw_text("Vivante", pygame.font.SysFont("Futura", 80), vert, 150, 375, screen)

        bouton_morte = pygame.draw.rect(screen, blanc, (500, 350, 350, 100))  # affichage bouton
        draw_text("Morte", pygame.font.SysFont("Futura", 80), vert, 585, 375, screen)

        bouton_calcul = pygame.draw.rect(screen, blanc, (950, 350, 350, 100))  # affichage bouton
        draw_text("Calcul", pygame.font.SysFont("Futura", 80), vert, 1035, 375, screen)

        pygame.display.flip()

        #grapheData[0] = alives / [1] = calculTime / [2] = dead

        if bouton_vivante.collidepoint(
            pygame.mouse.get_pos()
        ):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                pygame.display.flip()
                time.sleep(0.05)
                Graph.graph_alive(graphData[0])
                

        if bouton_morte.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                pygame.display.flip()
                time.sleep(0.2)
                Graph.graph_death(graphData[2])
                
        if bouton_calcul.collidepoint(pygame.mouse.get_pos()): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clc
                pygame.display.flip()
                time.sleep(0.2)
                Graph.graph_calcul(graphData[1])