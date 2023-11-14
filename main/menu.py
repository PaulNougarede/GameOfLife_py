import pygame, sys, time
from pygame.locals import *
import save as Save

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
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 300,screen)
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 350,screen)
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 400,screen)

        bouton_regles2 = pygame.draw.rect(screen, (255, 255, 255), (50, 500, 1300, 200))  # affichage règles 2
        draw_text("Règles 2:", pygame.font.SysFont("Futura", 40), vert, 50, 500,screen)
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 550,screen)
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 600,screen)
        draw_text("- ", pygame.font.SysFont("Futura", 40), vert, 50, 650,screen)

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
                if rules != 0:
                    return (rules, plate, 0)
                
        if bouton_ChargerPartie.collidepoint(
            pygame.mouse.get_pos()
        ): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clc
                bouton_ChargerPartie = pygame.draw.rect(screen, vert, (430,550,550,100))
                draw_text("Charger une partie",pygame.font.SysFont("Futura", 80),(255, 255, 255),450,575,screen)
                pygame.display.flip()
                time.sleep(0.2)
                tuple_info = Save.charge_plate()

                plate = tuple_info[0]
                nbr_tour = tuple_info[1]
                rules = tuple_info[2]

                return (rules, plate, nbr_tour)