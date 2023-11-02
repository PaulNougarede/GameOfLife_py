import pygame, sys
from pygame.locals import *

pygame.init()  # initialisation de la bibli pygame

horloge = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 800))  # creer la fenetre
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane")

vert = (0, 122, 123)

screen.fill(vert)  # couleur fond


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

    pygame.display.flip()  # AFFICHAGE

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
                "JOUER", pygame.font.SysFont("Futura", 80), (255, 255, 255), 580, 475
            )

            # LE JEU COMMENCE LA

    pygame.display.flip()


pygame.quit()
