import numpy as np
import pygame
from pygame.locals import *
import function.click as click
import sys
import menu as Menu

def save(plate, nbr_tour, rules_choice):
    with open("Sauvegarde/matrice.npy","wb") as f:
        np.save(f, plate)
    with open("Sauvegarde/nombre_tour.txt", "w") as file1 :
        file1.write(str(nbr_tour))
        file1.close()
    with open("Sauvegarde/rules.txt", "w") as file2 :
        file2.write(str(rules_choice))
        file2.close()


def charge_plate():
    with open("Sauvegarde/matrice.npy", "rb") as f:
        plate = np.load(f)
    with open("Sauvegarde/nombre_tour.txt", "r") as file1 :
        nbr_tour = file1.read()

        file1.close()
    with open("Sauvegarde/rules.txt", "r") as file2 :
        rules_choice = file2.read()
        file2.close()

    return (plate, nbr_tour, rules_choice)