import pygame, sys, time
from pygame.locals import *


def pageAccueil(screen):
    vert = (0, 122, 123)
    jeu = False

    # screen.fill(vert)#couleur fond

    imageMenuAccueil = pygame.image.load("main/images/menuAccueil.png").convert_alpha()
    screen.blit(imageMenuAccueil, (0, 0))

    def draw_text(text, font, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

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

        draw_text(
            "LE JEU DE LA VIE",
            pygame.font.SysFont("Futura", 150),
            (255, 255, 255),
            250,
            300,
        )
        draw_text(
            "Imad MRROUCH / Victor MIRIEU DE LABARRE / Paul NOUGAREDE / Vinciane GUYONNEAU",
            pygame.font.SysFont("Futura", 30),
            (255, 255, 255),
            250,
            750,
        )

        pygame.display.flip()  # affichage

        mouse = pygame.mouse.get_pos()  # positions de la souris dans un tuple
        # light shade of the button
        color_light = (170, 170, 170)

        bouton_rect = pygame.draw.rect(
            screen, (255, 255, 255), (525, 450, 300, 100)
        )  # affichage bouton
        draw_text("JOUER", pygame.font.SysFont("Futura", 80), vert, 580, 475)

        if bouton_rect.collidepoint(pygame.mouse.get_pos()):  # si souris sur le bouton
            if pygame.mouse.get_pressed()[0]:  # si clic
                bouton_rect = pygame.draw.rect(
                    screen, vert, (525, 450, 300, 100)
                )  # affichage bouton
                draw_text(
                    "JOUER",
                    pygame.font.SysFont("Futura", 80),
                    (255, 255, 255),
                    580,
                    475,
                )
                pygame.display.flip()
                jeu = True  # la prochaine page s'affichera
                running = False
                time.sleep(0.2)
    return jeu
