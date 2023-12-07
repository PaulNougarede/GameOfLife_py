import numpy as np
from pygame.locals import *


def save(rule_choice,plate,rows,cols,mode, nbr_tour):
    with open("Sauvegarde/matrice.npy","wb") as f:
        np.save(f, plate) #plate[]
    with open("Sauvegarde/configuration.txt", "w") as file1 :
        file1.write(str(rule_choice)+"\n") # rules_choice
        file1.write(str(nbr_tour)+"\n") # nbr_tour
        file1.write(str(rows)+"\n") # rows
        file1.write(str(cols)+"\n") # cols
        file1.write(str(mode)+"\n") # mode
        file1.close()
        
def charge_plate():
    with open("Sauvegarde/matrice.npy", "rb") as f:
        plate = np.load(f)
    with open("Sauvegarde/configuration.txt", "r") as file1 :
        conf = file1.readlines() #lis les lignes du fichier te les retourne en liste
        rules_choice = int(conf[0]) #récupère la première ligne -> choix des règles
        nbr_tour = int(conf[1]) #récupère la 2e ligne -> nombre de tours
        rows = int(conf[2]) #récupère la 3e ligne -> nombre de lignes
        cols = int(conf[3]) #récupère la 4e ligne -> nombre de colonnes
        mode = int(conf[4]) #récupère la 5e ligne -> mode
        file1.close() #ferme le fichier

    return (rules_choice,plate, nbr_tour,rows,cols,mode)