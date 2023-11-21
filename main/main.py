import pygame
from pygame.locals import *
import game as Game
import menu as Menu
import pageAccueil as PageAccueil

width, height = 1400, 800
#rows, cols = 100, 100
speed = 5
start_game = False
rule_choice = 0

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane")

start_game = PageAccueil.pageAccueil(screen)
if start_game:
    info = Menu.menu(screen) #info[0] : rules_choice / info[1] = plate / info[2] = nbr_tour / info[3] = rows / info[4] = cols / info[5] = mode
    graphData = Game.game(width, height, info[3], info[4], speed, info[0], info[1], info[2], info[5])
    #grapheData[0] = alives / [1] = calculTime / [2] = dead
    Menu.menu_graphs(screen,graphData)
    pygame.quit()