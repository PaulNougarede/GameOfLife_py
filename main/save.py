import numpy as np
from pygame.locals import *


def save(info, nbr_tour):
    with open("Sauvegarde/matrice.npy","wb") as f:
        np.save(f, info[1]) #plate[]
    with open("Sauvegarde/configuration.txt", "w") as file1 :
        file1.write(str(info[0])+"\n") # rules_choice
        file1.write(str(nbr_tour)+"\n") # nbr_tour
        file1.write(str(info[3])+"\n") # rows
        file1.write(str(info[4])+"\n") # cols
        file1.write(str(info[5])+"\n") # mode
        file1.close()
        
def charge_plate():
    with open("Sauvegarde/matrice.npy", "rb") as f:
        plate = np.load(f)
    with open("Sauvegarde/configuration.txt", "r") as file1 :
        conf = file1.readlines()
        rules_choice = int(conf[0])
        nbr_tour = int(conf[1])
        rows = int(conf[2])
        cols = int(conf[3])
        mode = int(conf[4])
        file1.close()

    return (rules_choice,plate, nbr_tour,rows,cols,mode)