import pygame, sys, time
from pygame.locals import *
import menu as Menu


def pageAccueil(screen):
    vert = (0, 122, 123)
    blanc = (255, 255, 255)
    jeu = False

    imageMenuAccueil = pygame.image.load("main/images/menuAccueil.png").convert_alpha()
    screen.blit(imageMenuAccueil, (0, 0))

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

        Menu.draw_text("LE JEU DE LA VIE",pygame.font.SysFont("Futura", 150),(255, 255, 255),250,300,screen)
        Menu.draw_text("Imad MRROUCH / Victor MIRIEU DE LABARRE / Paul NOUGAREDE / Vinciane GUYONNEAU",pygame.font.SysFont("Futura", 30),(255, 255, 255),250,750,screen)

        pygame.display.flip()  # affichage

        mouse = pygame.mouse.get_pos()  # positions de la souris dans un tuple
        
        bouton_rect = pygame.draw.rect(screen, blanc, (525, 450, 300, 100), 0, 5)  # affichage bouton
        bord_rect = pygame.draw.rect(screen, vert, (535, 460, 280, 80), 7, 5)
        Menu.draw_text("JOUER", pygame.font.SysFont("Futura", 80), vert, 580, 475,screen)

        if bouton_rect.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_rect = pygame.draw.rect(screen, vert, (525, 450, 300, 100))  # affichage bouton
                bord_rect = pygame.draw.rect(screen, blanc, (535, 460, 280, 80), 7, 5)
                Menu.draw_text("JOUER", pygame.font.SysFont("Futura", 80), blanc, 580, 475, screen)
                pygame.display.flip()
                jeu = True  # la prochaine page s'affichera
                running = False
                time.sleep(0.07)
    return jeu
