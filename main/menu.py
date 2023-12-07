import pygame, sys, time
from pygame.locals import *
import save as Save
import graphs.graphAlive as Graph

def draw_text(text, font, color, x, y, screen): # fonction pour écrire du texte
        img = font.render(text, True, color)
        screen.blit(img, (x, y)) # affichage

def principeDuJeu(screen):
    
    vert = (0, 122, 123) #définition couleurs du jeu
    blanc = (255, 255, 255)

    screen.fill(vert)  #couleur fond
    iconeRetour = pygame.image.load("main/images/icone_fleche_arriere.png").convert_alpha()  # icone fleche retour
    iconeRetour = pygame.transform.scale(iconeRetour, (150, 150))  # mise à l'échelle
    screen.blit(iconeRetour, (50, 50)) #affichage à 50,50

    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha() #icone quitter le jeu
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50)) #mise à l'échelle
    screen.blit(iconeQuitter, (1330, 20)) #affichage à 1330,20
    
    pygame.display.flip() #affichage

    running = True

    while running:  # boucle infinie
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit() # fermeture de la fenetre
                sys.exit()
            if event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()
                    
        draw_text("Principe du jeu:", pygame.font.SysFont("Futura", 80), blanc, 500, 150,screen) #ecriture des textes
        draw_text("Le Jeu de la Vie est un automate cellulaire inventé par le mathématicien John Conway en 1970.", pygame.font.SysFont("Futura", 40), blanc, 50, 300,screen)
        draw_text("Il se déroule sur une grille bidimensionnelle infinie, où chaque cellule peut être vivante ou morte.", pygame.font.SysFont("Futura", 40), blanc, 50, 350,screen)
        draw_text("L'évolution des cellules est régie par des règles simples basées sur le nombre de voisins vivants", pygame.font.SysFont("Futura", 40), blanc, 50, 400,screen)
        draw_text("de chaque cellule.", pygame.font.SysFont("Futura", 40), blanc, 50, 450,screen)
        draw_text("Au fil des générations, des motifs complexes émergent,", pygame.font.SysFont("Futura", 40), blanc, 50, 500,screen)
        draw_text("sans aucune intervention directe du joueur.", pygame.font.SysFont("Futura", 40), blanc, 50, 550,screen)
        pygame.display.flip()
        
        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris
        if (50 <= mouse_x <= 50 + iconeRetour.get_width() and 50 <= mouse_y <= 50 + iconeRetour.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                return 0
            
        if (1330 <= mouse_x <= 1330 + iconeQuitter.get_width() and 20 <= mouse_y <= 20 + iconeQuitter.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                sys.exit()


def choixDesRegles(screen):
    vert = (0, 122, 123)
    blanc = (255, 255, 255)
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

        draw_text("Choix des règles:",pygame.font.SysFont("Futura", 80),blanc,500,150,screen)

        bouton_regles1 = pygame.draw.rect(screen, blanc, (50, 250, 1300, 200), 0, 5)  # affichage règles 1
        bord_regles1 = pygame.draw.rect(screen, vert, (60, 260, 1280, 180), 7, 5)
        draw_text("Règles 1:", pygame.font.SysFont("Futura", 35), vert, 70, 270,screen)
        pygame.draw.line(screen, vert, (70, 300), (180, 300), 3)
        draw_text("- Uniquement 2 cellules autour : mort par isolement", pygame.font.SysFont("Futura", 30), vert, 70, 320,screen)
        draw_text("- Plus de 3 cellules autour : mort de surpopulation ", pygame.font.SysFont("Futura", 30), vert, 70, 350,screen)
        draw_text("- 3 cellules autour de toi : naissance par invocation ", pygame.font.SysFont("Futura", 30), vert, 70, 380,screen)

        bouton_regles2 = pygame.draw.rect(screen, blanc, (50, 500, 1300, 200), 0, 5)  # affichage règles 2
        bord_regles2 = pygame.draw.rect(screen, vert, (60, 510, 1280, 180), 7, 5)
        draw_text("Règles 2:", pygame.font.SysFont("Futura", 35), vert, 70, 520,screen)
        pygame.draw.line(screen, vert, (70, 550), (180, 550), 3)
        draw_text("- Uniquement 2 cellules autour : mort par isolement", pygame.font.SysFont("Futura", 30), vert, 70, 570,screen)
        draw_text("- Plus de 3 cellules autour : mort de surpopulation", pygame.font.SysFont("Futura", 30), vert, 70, 600,screen)
        draw_text("- 1 cellules autour de toi : naissance par invocation", pygame.font.SysFont("Futura", 30), vert, 70, 630,screen)

        pygame.display.flip()

        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris
        if (50 <= mouse_x <= 50 + iconeRetour.get_width() and 50 <= mouse_y <= 50 + iconeRetour.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                menu(screen)
                
        pygame.display.flip()

        if bouton_regles1.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_regles1 = pygame.draw.rect(screen, vert, (50, 250, 1300, 200), 0, 5)  # affichage règles 1
                bord_regles1 = pygame.draw.rect(screen, blanc, (60, 260, 1280, 180), 7, 5)
                draw_text("Règles 1:", pygame.font.SysFont("Futura", 35), blanc, 70, 270,screen)
                pygame.draw.line(screen, blanc, (70, 300), (180, 300), 3)
                draw_text("- Uniquement 2 cellules autour : mort par isolement", pygame.font.SysFont("Futura", 30), blanc, 70, 320,screen)
                draw_text("- Plus de 3 cellules autour : mort de surpopulation ", pygame.font.SysFont("Futura", 30), blanc, 70, 350,screen)
                draw_text("- 3 cellules autour de toi : naissance par invocation ", pygame.font.SysFont("Futura", 30), blanc, 70, 380,screen)
                pygame.display.flip()
                time.sleep(0.05) # pour ne pas que le bouton soit cliqué plusieurs fois
                return 1

        if bouton_regles2.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_regles2 = pygame.draw.rect(screen, vert, (50, 500, 1300, 200), 0, 5)  # affichage règles 2
                bord_regles2 = pygame.draw.rect(screen, blanc, (60, 510, 1280, 180), 7, 5)
                draw_text("Règles 2:", pygame.font.SysFont("Futura", 35), blanc, 70, 520,screen)
                pygame.draw.line(screen, blanc, (70, 550), (180, 550), 3)
                draw_text("- Uniquement 2 cellules autour : mort par isolement", pygame.font.SysFont("Futura", 30), blanc, 70, 570,screen)
                draw_text("- Plus de 3 cellules autour : mort de surpopulation", pygame.font.SysFont("Futura", 30), blanc, 70, 600,screen)
                draw_text("- 1 cellules autour de toi : naissance par invocation", pygame.font.SysFont("Futura", 30), blanc, 70, 630,screen)
                pygame.display.flip()
                time.sleep(0.05) # pour ne pas que le bouton soit cliqué plusieurs fois
                return 2


def menu(screen):

    plate = []
    running = True
    
    vert = (0, 122, 123)
    blanc = (255, 255, 255)
    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha() #icone quitter le jeu
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50)) #mise à l'échelle
    
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
                    
        screen.fill(vert)
        screen.blit(iconeQuitter, (1330, 20))
        
        bouton_principeDuJeu = pygame.draw.rect(screen, blanc, (430, 150, 550, 100), 0, 5)  # affichage bouton
        bord_principeDuJeu = pygame.draw.rect(screen, vert, (440, 160, 530, 80), 7, 5)
        draw_text("Principe du jeu", pygame.font.SysFont("Futura", 75), vert, 505, 175, screen)

        bouton_nvlPartie = pygame.draw.rect(screen, blanc, (430, 350, 550, 100), 0, 5)  # affichage bouton
        bord_nvlPartie = pygame.draw.rect(screen, vert, (440, 360, 530, 80), 7, 5)
        draw_text("Nouvelle partie", pygame.font.SysFont("Futura", 75), vert, 500, 375, screen)

        bouton_ChargerPartie = pygame.draw.rect(screen, blanc, (430, 550, 550, 100), 0, 5)  # affichage bouton
        bord_ChargerPartie = pygame.draw.rect(screen, vert, (440, 560, 530, 80), 7, 5)
        draw_text("Charger une partie", pygame.font.SysFont("Futura", 75), vert, 465, 575, screen)

        pygame.display.flip()

        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris
        if (1330 <= mouse_x <= 1330 + iconeQuitter.get_width() and 20 <= mouse_y <= 20 + iconeQuitter.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                sys.exit(0)

        if bouton_principeDuJeu.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_principeDuJeu = pygame.draw.rect(screen, vert, (430, 150, 550, 100), 0, 5)  # affichage bouton
                bord_principeDuJeu = pygame.draw.rect(screen, blanc, (440, 160, 530, 80), 7, 5)
                draw_text("Principe du jeu", pygame.font.SysFont("Futura", 75), blanc, 505, 175, screen)
                pygame.display.flip()
                time.sleep(0.1) # pour ne pas que le bouton soit cliqué plusieurs fois
                principeDuJeu(screen)

        if bouton_nvlPartie.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_nvlPartie = pygame.draw.rect(screen, vert, (430, 350, 550, 100), 0, 5)  # affichage bouton
                bord_nvlPartie = pygame.draw.rect(screen, blanc, (440, 360, 530, 80), 7, 5)
                draw_text("Nouvelle partie", pygame.font.SysFont("Futura", 75), blanc, 500, 375, screen)
                pygame.display.flip()
                time.sleep(0.2) # pour ne pas que le bouton soit cliqué plusieurs fois
                rules = choixDesRegles(screen) #récupère le choix des règles
                time.sleep(0.1)
                taille = choix_taille(screen) #récupère la taille du plateau
                time.sleep(0.1)
                if(taille[0] < 250):
                    mode = choix_mode(screen) #récupère le mode de jeu
                else:
                    mode = 1 #mode simulation
                if rules != 0:
                    return (rules, plate, 0, taille[0], taille[1], mode) #taille[0] = rows / taille[1] = cols
                
        if bouton_ChargerPartie.collidepoint(pygame.mouse.get_pos()): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clic
                bouton_ChargerPartie = pygame.draw.rect(screen, vert, (430,550,550,100), 0, 5)
                bord_ChargerPartie = pygame.draw.rect(screen, blanc, (440, 560, 530, 80), 7, 5)
                draw_text("Charger une partie", pygame.font.SysFont("Futura", 75), blanc, 465, 575, screen)
                pygame.display.flip()
                time.sleep(0.2) # pour ne pas que le bouton soit cliqué plusieurs fois
                tuple_info = Save.charge_plate() #récupère les infos de la partie sauvegardée

                rules_choice = tuple_info[0]
                plate = tuple_info[1]
                print(plate)
                nbr_tour = tuple_info[2]
                rows = tuple_info[3]
                cols = tuple_info[4]
                mode = tuple_info[5]

                return (rules_choice, plate, nbr_tour,rows,cols,mode)
            

def choix_taille(screen):

    width, height = 1400, 800

    #couleurs
    BLANC = (255, 255, 255)
    ROUGE = (255, 0, 0)

    #variables
    valeur_variable = 50
    valeur_min = 50
    valeur_max = 1000
    running = True

    #chargement de la police
    pygame.font.init()
    police = pygame.font.SysFont("Futura", 24)

    while running:  # boucle infinie
        vert = (0, 122, 123)
        screen.fill(vert)  # couleur fond
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si la croix est cliquée
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:  # si on appuie sur une touche
                if event.key == K_ESCAPE:  # si c'est la touch echap
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width // 2 - 140 <= event.pos[0] <= width // 2 + 100 and height // 2 - 20 <= event.pos[1] <= height // 2 + 20:
                    #si clic dans zone du curseur
                    curseur_enfonce = True
            elif event.type == pygame.MOUSEBUTTONUP:
                curseur_enfonce = False
        
        if curseur_enfonce: #MAJ valeur variable en fonction de la position du curseur
            x_souris, _ = pygame.mouse.get_pos()
            valeur_variable = int((x_souris - (width // 2 - 100)) / 200 * (valeur_max - valeur_min))
            valeur_variable = max(valeur_min, min(valeur_max, valeur_variable))

        screen.fill(vert)

        pygame.draw.rect(screen, BLANC, (width // 2 - 130, height // 2 - 20, 240, 40)) #affichage curseur
        pygame.draw.rect(screen, ROUGE, (width // 2 - 140 + int(valeur_variable / (valeur_max - valeur_min) * 200), height // 2 - 20, 40, 40))

        texte = police.render(str(valeur_variable)+"x"+str(valeur_variable), True, BLANC)
        texte_rect = texte.get_rect(center=(width // 2-20, height // 2 + 40)) #affichage valeur de la variable

        draw_text("Choisissez la taille du plateau", pygame.font.SysFont("Futura", 60), BLANC, 400, 200, screen) #affichage choix taille plateau

        bouton_entree = pygame.draw.rect(screen, BLANC, (586, 525, 190, 70), 0, 5) #affichage bouton
        bord_entree = pygame.draw.rect(screen, vert, (591, 530, 180, 60), 5, 5)
        draw_text("Valider", pygame.font.SysFont("Futura", 60), vert, 606, 545, screen)

        screen.blit(texte, texte_rect)
        pygame.display.flip()

        if bouton_entree.collidepoint(pygame.mouse.get_pos()): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clic
                bouton_entree = pygame.draw.rect(screen, vert, (586,525,190,70), 0, 5)
                bord_entree = pygame.draw.rect(screen, BLANC, (591, 530, 180, 60), 7, 5)
                draw_text("Valider", pygame.font.SysFont("Futura", 60), BLANC, 606, 545, screen)
                pygame.display.flip()
                time.sleep(0.2) # pour ne pas que le bouton soit cliqué plusieurs fois
                return (valeur_variable, valeur_variable) 
            
            
def choix_mode(screen): #choix du mode de jeu
    running = True
    
    vert = (0, 122, 123)
    blanc = (255, 255, 255)
    
    while running:  # boucle infinie
        
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

        bouton_alea = pygame.draw.rect(screen, blanc, (100, 350, 500, 100), 0, 5)  # affichage bouton
        bord_alea = pygame.draw.rect(screen, vert, (110, 360, 480, 80), 7, 5)
        draw_text("Aléatoire", pygame.font.SysFont("Futura", 80), vert, 220, 375, screen)

        bouton_manu = pygame.draw.rect(screen, blanc, (800, 350, 500, 100), 0, 5)  # affichage bouton
        bord_manu = pygame.draw.rect(screen, vert, (810, 360, 480, 80), 7, 5)
        draw_text("Manuel", pygame.font.SysFont("Futura", 80), vert, 940, 375, screen)

        pygame.display.flip()

        if bouton_alea.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_alea = pygame.draw.rect(screen, vert, (100, 350, 500, 100), 0, 5)  # affichage bouton
                bord_alea = pygame.draw.rect(screen, blanc, (110, 360, 480, 80), 7, 5)
                draw_text("Aléatoire",pygame.font.SysFont("Futura", 80),blanc,220,375,screen)
                pygame.display.flip()
                time.sleep(0.2) # pour ne pas que le bouton soit cliqué plusieurs fois
                return (1) #mode aléatoire

        if bouton_manu.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_manu = pygame.draw.rect(screen, vert, (800, 350, 500, 100), 0, 5)  # affichage bouton
                bord_manu = pygame.draw.rect(screen, blanc, (810, 360, 480, 80), 7, 5)
                draw_text("Manuel",pygame.font.SysFont("Futura", 80),blanc,940,375,screen)
                pygame.display.flip()
                time.sleep(0.2)
                return(2) #mode manuel
            
def menu_graphs(screen, graphData):

    running = True
    vert = (0, 122, 123)
    blanc = (255,255,255)
    iconeQuitter = pygame.image.load("main/images/icone_quitter.png").convert_alpha() #icone quitter le jeu
    iconeQuitter = pygame.transform.scale(iconeQuitter, (50, 50)) #mise à l'échelle

    while running:  # boucle infinie
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
                    
        screen.blit(iconeQuitter, (1330, 20))

        bouton_vivante = pygame.draw.rect(screen, blanc, (50, 350, 350, 160))  # affichage bouton
        bord_vivante= pygame.draw.rect(screen, vert, (60, 360, 330, 140), 7, 5)
        draw_text("Cellules", pygame.font.SysFont("Futura", 80), vert, 120, 375, screen)
        draw_text("vivantes", pygame.font.SysFont("Futura", 80), vert, 110, 425, screen)

        bouton_morte = pygame.draw.rect(screen, blanc, (500, 350, 350, 160))  # affichage bouton
        bord_morte= pygame.draw.rect(screen, vert, (510, 360, 330, 140), 7, 5)
        draw_text("Cellules", pygame.font.SysFont("Futura", 80), vert, 555, 375, screen)
        draw_text("mortes", pygame.font.SysFont("Futura", 80), vert, 585, 425, screen)
        
        bouton_calcul = pygame.draw.rect(screen, blanc, (950, 350, 350, 160))  # affichage bouton
        bord_calcul= pygame.draw.rect(screen, vert, (960, 360, 330, 140), 7, 5)
        draw_text("Temps", pygame.font.SysFont("Futura", 80), vert, 1035, 375, screen)
        draw_text("de calcul", pygame.font.SysFont("Futura", 80), vert, 1005, 425, screen)
        
        draw_text("Graphiques:", pygame.font.SysFont("Futura", 80), blanc, 500, 150, screen)

        pygame.display.flip()

        #grapheData[0] = alives / [1] = calculTime / [2] = dead
        
        mouse_x, mouse_y = pygame.mouse.get_pos()  # coordonnées de la souris      
        if (1330 <= mouse_x <= 1330 + iconeQuitter.get_width() and 20 <= mouse_y <= 20 + iconeQuitter.get_height()):  # si la souris est sur l'icône
            if pygame.mouse.get_pressed()[0]:  # si clic
                return 0

        if bouton_vivante.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_vivante = pygame.draw.rect(screen, vert, (50, 350, 350, 160))  # affichage bouton
                bord_vivante= pygame.draw.rect(screen, blanc, (60, 360, 330, 140), 7, 5)
                draw_text("Cellules", pygame.font.SysFont("Futura", 80), blanc, 120, 375, screen)
                draw_text("vivantes", pygame.font.SysFont("Futura", 80), blanc, 110, 425, screen)
                pygame.display.flip()
                time.sleep(0.1)
                Graph.graph_alive(graphData[0]) #affichage du graphe cellules vivantes
                

        if bouton_morte.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_morte = pygame.draw.rect(screen, vert, (500, 350, 350, 160))  # affichage bouton
                bord_morte= pygame.draw.rect(screen, blanc, (510, 360, 330, 140), 7, 5)
                draw_text("Cellules", pygame.font.SysFont("Futura", 80), blanc, 555, 375, screen)
                draw_text("mortes", pygame.font.SysFont("Futura", 80), blanc, 585, 425, screen)
                pygame.display.flip()
                time.sleep(0.1)
                Graph.graph_death(graphData[2]) #affichage du graphe cellules mortes
                
        if bouton_calcul.collidepoint(pygame.mouse.get_pos()): # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]: #si clic
                bouton_calcul = pygame.draw.rect(screen, vert, (950, 350, 350, 160))  # affichage bouton
                bord_calcul= pygame.draw.rect(screen, blanc, (960, 360, 330, 140), 7, 5)
                draw_text("Temps", pygame.font.SysFont("Futura", 80), blanc, 1035, 375, screen)
                draw_text("de calcul", pygame.font.SysFont("Futura", 80), blanc, 1005, 425, screen)
                pygame.display.flip()
                time.sleep(0.1)
                Graph.graph_calcul(graphData[1]) #affichage du graphe temps de calcul