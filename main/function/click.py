def cliqueCase(plate, clickX, clickY, cell_width, cell_height, scale, offsetX, offsetY):
    # ajustement des coordonnées en fonction de l'offset et de l'échelle
    adjustedX = (clickX - offsetX) // (cell_width * scale)
    adjustedY = (clickY - offsetY) // (cell_height * scale)

    #les coordonnées ajustées sont dans les limites du tableau
    if 0 <= adjustedX < plate.shape[0] and 0 <= adjustedY < plate.shape[1]:
        # modification de l'état de la cellule dans le tableau
        plate[int(adjustedX), int(adjustedY)] = 1 if plate[int(adjustedX), int(adjustedY)] == 0 else 0

    # turn = 0
    # while clickX > cell_width:
    #     turn += 1
    #     clickX = clickX - cell_width
    # placeX = turn * cell_width
    # turn = 0
    # while clickY > cell_height:
    #     turn += 1
    #     clickY = clickY - cell_height
    # placeY = turn * cell_height
    # if plate[int(placeX / cell_width)][int(placeY / cell_height)] == 1:
    #     plate[int(placeX / cell_width)][int(placeY / cell_height)] = 0
    # else:
    #     plate[int(placeX / cell_width)][int(placeY / cell_height)] = 1