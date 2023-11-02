import pygame
from pygame.locals import *
import game as Game
import graphs.graphAlive as Graph
import menu as Menu
import pageAccueil as PageAccueil

width, height = 800, 800
rows, cols = 100, 100
speed = 5
start_game = False
rule_choice = 0

pygame.init()

screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane")

start_game = PageAccueil.pageAccueil(screen)
if start_game:
    rule_choice = Menu.menu(screen)
    alive = Game.game(width, height, rows, cols, speed, rule_choice)
    Graph.graph_alive(alive)
