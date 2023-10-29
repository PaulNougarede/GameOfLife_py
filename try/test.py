import pygame, random 
import numpy as np

#--------------------------------------------------------SOUS PROG----------------------------------------------------------------------------------

def affichageFirstCellule( tableau , plateau ,  couleur) :
    
    aleaX = random.randint(0,49) #28 possibilités
    aleaY = random.randint(0,49) #16 possibilités
    pygame.draw.rect(plateau, couleur, (aleaX*28, aleaY*16, 28, 16))
    tableau[aleaX][aleaY] = 1

def affichagePlateau( plateau , couleur ) : 
    
    for  i in range(0,1400,28) :
            for  j in range(0,800,16) :
                # Dessine le plateau
                pygame.draw.rect(plateau, couleur, (i, j, 28, 16), 1)

def vie( tableau , tableau2, affichage, couleur1, couleur2 ) :
    
    unX , deuxX, troisX, quatreX, cinqX, sixX, septX, huitX = -28,0,28,-28,+28,-28,0,28
    unY , deuxY, troisY, quatreY, cinqY, sixY, septY, huitY = -16,-16,-16,0,0,16,16,16
    
    for i in range(50) :
        for j in range(50) :

            if tableau[i][j] == 0 :
                posX, posY, compte= i*28, j*16, 0
                
                if(posX+unX >= 0 and posY+unY >= 0 ) :
                    if  affichage.get_at((posX+unX+14,posY+unY+8)) == couleur2 :
                        compte += 1
                
                if(posY+deuxY >= 0) :
                    if  affichage.get_at((posX+deuxX+14,posY+deuxY+8)) == couleur2 :
                        compte += 1
                
                if(posX+troisX <= 1372 and posY+troisY >= 0) : 
                    if  affichage.get_at((posX+troisX+14,posY+troisY+8)) == couleur2 :
                        compte += 1
                
                if(posX+quatreX >= 0) :  
                    if  affichage.get_at((posX+quatreX+14,posY+quatreY+8)) == couleur2 :
                        compte += 1
                    
                if(posX+cinqX <= 1372) : 
                    if  affichage.get_at((posX+cinqX+14,posY+cinqY+8)) == couleur2 :
                        compte += 1
                
                if(posX+sixX >= 0 and posY+sixY <= 784) : 
                    if  affichage.get_at((posX+sixX+14,posY+sixY+8)) == couleur2 :
                        compte += 1
                
                if(posY+septY <= 784) :
                    if  affichage.get_at((posX+septX+14,posY+septY+8)) == couleur2 :
                        compte += 1
                
                if(posX+huitX <= 1372 and posY+huitY <= 784) :
                    if  affichage.get_at((posX+huitX+14,posY+huitY+8)) == couleur2 :
                        compte += 1
                
                if( compte == 3 ) :
                    compte = 0
                    #pygame.draw.rect(affichage, couleur2, (posX, posY, 50, 50))
                    tableau2[i][j] = 1

def mort( tableau, tableau2, affichage, couleur1, couleur2 ) :
    
    unX , deuxX, troisX, quatreX, cinqX, sixX, septX, huitX = -28,0,28,-28,+28,-28,0,28
    unY , deuxY, troisY, quatreY, cinqY, sixY, septY, huitY = -16,-16,-16,0,0,16,16,16
    
    for i in range(50) :
        for j in range(50) :
            
            tableau2[i][j] = tableau[i][j]
            
            if tableau[i][j] == 1 :
                posX, posY, compte= i*28, j*16, 0
                
                print("Vie détécté X :",posX,"et Y :",posY )
                
                if(posX+unX >= 0 and posY+unY >= 0 ) :
                    if  affichage.get_at((posX+unX+14,posY+unY+8)) == couleur2 :
                        compte += 1
                
                if(posY+deuxY >= 0) :
                    if  affichage.get_at((posX+deuxX+14,posY+deuxY+8)) == couleur2 :
                        compte += 1
                
                if(posX+troisX <= 1372 and posY+troisY >= 0) : 
                    if  affichage.get_at((posX+troisX+14,posY+troisY+8)) == couleur2 :
                        compte += 1
                
                if(posX+quatreX >= 0) :  
                    if  affichage.get_at((posX+quatreX+14,posY+quatreY+8)) == couleur2 :
                        compte += 1
                    
                if(posX+cinqX <= 1372) : 
                    if  affichage.get_at((posX+cinqX+14,posY+cinqY+8)) == couleur2 :
                        compte += 1
                
                if(posX+sixX >= 0 and posY+sixY <= 784) : 
                    if  affichage.get_at((posX+sixX+14,posY+sixY+8)) == couleur2 :
                        compte += 1
                
                if(posY+septY <= 784) :
                    if  affichage.get_at((posX+septX+14,posY+septY+8)) == couleur2 :
                        compte += 1
                
                if(posX+huitX <= 1372 and posY+huitY <= 784) :
                    if  affichage.get_at((posX+huitX+14,posY+huitY+8)) == couleur2 :
                        compte += 1
                        
                if( compte != 3 and compte != 2 ) :
                    print("Compte BON !! X :", i,"-",posX ,"Y:", j,"-", posY)
                    compte = 0                    
                    #pygame.draw.rect(affichage, couleur1, (posX, posY, 50, 50))
                    #pygame.draw.rect(affichage, couleur2, (posX, posY, 50, 50), 1)
                    tableau2[i][j] = 0

def majTableau( tableau, tableau1, tableau2, affichage, couleur1, couleur2 ) :
   
    for  i in range(50) :
        for  j in range(50) :
            tableau1[i][j] = tableau1[i][j] + tableau2[i][j]
            tableau[i][j] = tableau1[i][j]
            
            if tableau[i][j] == 0:
                pygame.draw.rect(affichage, couleur1, (i*28, j*16, 28, 16))
                pygame.draw.rect(affichage, couleur2, (i*28, j*16, 28, 16), 1)
            else :
                pygame.draw.rect(affichage, couleur2, (i*28, j*16, 28, 16))
                
            tableau1[i][j] = 0
            tableau2[i][j] = 0

def cliqueCase( tableau ,plateau , couleur, cliqueX, cliqueY ) : 
    
    tour = 0
    while cliqueX > 28 :
        tour += 1
        cliqueX = cliqueX - 28
    
    placeX = tour * 28
    tour = 0
    
    while cliqueY > 16 :
        tour += 1
        cliqueY = cliqueY - 16
    
    placeY = tour * 16
    pygame.draw.rect(plateau, couleur, (placeX, placeY, 28, 16)) 
    tableau[int(placeX/28)][int(placeY/16)] = 1

#---------------------------------------------------------------------------------------------------------------------------------------

pygame.init() #initialisation module Pygames
pygame.display.set_caption("JEU DE LA VIE - IMAD")
fond = pygame.display.set_mode((1400,800)) #init fenetre
clock = pygame.time.Clock() #init temps

#init variables
black, white,execution, run = (0,0,0) , (255, 255, 255), 0, True
plateau = np.zeros((50,50))
tmpVie = np.zeros((50,50))
tmpMort = np.zeros((50,50))
for  i in range(50) :
        for  j in range(50) :
            plateau[i][j] = 0 ;tmpVie[i][j] = 0 ;tmpMort[i][j] = 0

fond.fill(white) #fenetre avec un fond blanc 
#Affichages du plateau
affichagePlateau( fond , black ) 
#affichages premiere cellule
affichageFirstCellule( plateau, fond ,  black)

#Boucle de jeu
while run :
    
    #Quitter le jeu lors du clique sur la croix
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            run = False
            
    #Vérifie si les évenements contiennent un clique
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Clic gauche
            cliqueX, cliqueY = event.pos
            print("CLIQUE !!!!")
            cliqueCase( plateau ,fond , black, cliqueX, cliqueY )

    #Recupère le temps actuel en millisecondes
    myTime = pygame.time.get_ticks()
    #Vérifie si 5 sec se sont écoulées
    if myTime - execution >= 5000:
        print("EXECUTION !")
        vie( plateau, tmpVie, fond, white, black ) #Traitement de la naissance de cellules
        mort( plateau, tmpMort, fond, white, black ) #Traitement de la mort de cellules
        majTableau( plateau, tmpVie, tmpMort, fond, white, black )#Actualisation de l'affichage
        
        execution = myTime

    #Met à jour l'écran 
    pygame.display.flip()

    #gestion du nombre de FPS
    clock.tick(60)

pygame.quit()

