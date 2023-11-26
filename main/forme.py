#---------------------------------- FORMES STABLES -----------------------------------------

# A Z E

def square(plate, clickX , clickY, cell_width, cell_height ) :

    row = clickX // cell_width
    col = clickY // cell_height
    
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row, col] = 1
    if 0 <= row < plate.shape[0] and 0 <= col+1 < plate.shape[1]:
        plate[row, col+1] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row+1, col] = 1
    if 0 <= row+1 < plate.shape[0] and 0 <= col+1 < plate.shape[1]: 
        plate[row+1, col+1] = 1

def planner(plate, clickX , clickY, cell_width, cell_height ) :

    row = clickX // cell_width
    col = clickY // cell_height
    
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
        
def canon(plate, clickX , clickY, cell_width, cell_height ) :

    row = clickX // cell_width
    col = clickY // cell_height
    
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
    