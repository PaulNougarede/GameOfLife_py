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

pygame.init() # initialisation pygame

screen = pygame.display.set_mode((width, height)) # création de la fenetre
pygame.display.set_caption("Jeu de la Vie - Imad Victor Paul Vinciane") # titre fenetre

start_game = PageAccueil.pageAccueil(screen) # affichage page d'accueil
if start_game: # si on a cliqué sur jouer
    info = Menu.menu(screen) #info[0] : rules_choice / info[1] = plate / info[2] = nbr_tour / info[3] = rows / info[4] = cols / info[5] = mode
    if(int(info[3]<250)): #jeu "normal"
        graphData = Game.game(width, height, speed, info)
    else: #jeu en simulation (pour grilles > 250*250)
        graphData = Game.simulation(width, height, speed, info)
    #grapheData[0] = alives / [1] = calculTime / [2] = dead
    Menu.menu_graphs(screen,graphData) #affichage des graphes
    pygame.quit() #fermeture de la fenetre