#---------------------------------- FORMES STABLES -----------------------------------------

# A : carré ,  Z : planner ,  E : Cannon à planner

#Function d'affochage de formes :
#   -On récupère en paramètre les coordonnées de la souris pour savoir ou placer la forme
#   -On applique le calcul pour rédupérer les indices du tableau de la cellule depuis les coordonnées de la souris
#   -On rend vivante les cellules selon la forme voulut

def square(plate, clickX , clickY, cell_width, cell_height, scale, offsetX, offsetY ) :

    row = int((clickX - offsetX) // (cell_width * scale))
    col = int((clickY - offsetY) // (cell_height * scale))
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col+1 < plate.shape[1]:
        plate[row, col+1] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+1, col] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col+1 < plate.shape[1]: 
        plate[row+1, col+1] = 1

def planner(plate, clickX , clickY, cell_width, cell_height, scale, offsetX, offsetY ) :

    row = int((clickX - offsetX) // (cell_width * scale))
    col = int((clickY - offsetY) // (cell_height * scale))
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col-1 < plate.shape[1]: 
        plate[row, col-1] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col-2 < plate.shape[1]:
        plate[row+1, col-2] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+1, col] = 1
    if 0 <= row+2 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+2, col] = 1
        
def canon(plate, clickX , clickY, cell_width, cell_height, scale, offsetX, offsetY ) :

    row = int((clickX - offsetX) // (cell_width * scale))
    col = int((clickY - offsetY) // (cell_height * scale))
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-1, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-3, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-7, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-16, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-17, col] = 1
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-1, col-1] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-7, col-1] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-16, col-1] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-17, col-1] = 1
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-2, col-2] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-6, col-2] = 1
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-4, col-3] = 1
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row-5, col-3] = 1
        
    if 0 <= row < plate.shape[0] and 0 <= col+1 < plate.shape[1]:
        plate[row-1, col+1] = 1
    if 0 <= row < plate.shape[0] and 0 <= col+1 < plate.shape[1]:
        plate[row-7, col+1] = 1
    
    if 0 <= row < plate.shape[0] and 0 <= col+2 < plate.shape[1]:
        plate[row-2, col+2] = 1
    if 0 <= row < plate.shape[0] and 0 <= col+2 < plate.shape[1]:
        plate[row-6, col+2] = 1
        
    if 0 <= row < plate.shape[0] and 0 <= col+3 < plate.shape[1]:
        plate[row-4, col+3] = 1
    if 0 <= row < plate.shape[0] and 0 <= col+3 < plate.shape[1]:
        plate[row-5, col+3] = 1
        
    if 0 <= row+3 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+3, col-1] = 1
    if 0 <= row+3 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+3, col-2] = 1
    if 0 <= row+3 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+3, col-3] = 1
    
    if 0 <= row+4 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+4, col-1] = 1
    if 0 <= row+4 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+4, col-2] = 1
    if 0 <= row+4 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+4, col-3] = 1
    
    if 0 <= row+5 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+5, col] = 1
    if 0 <= row+7 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+7, col] = 1
    
    if 0 <= row+7 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+7, col+1] = 1
    
    if 0 <= row+5 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+5, col-4] = 1
    if 0 <= row +7< plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+7, col-4] = 1
    
    if 0 <= row+7 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+7, col-5] = 1
    
    if 0 <= row+17 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+17, col-2] = 1
    if 0 <= row+18 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+18, col-2] = 1
    
    if 0 <= row+17 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+17, col-3] = 1
    if 0 <= row+18 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+18, col-3] = 1
    