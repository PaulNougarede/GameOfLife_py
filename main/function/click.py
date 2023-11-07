def cliqueCase(plate, clickX, clickY, cell_width, cell_height):
    row = clickX // cell_width
    col = clickY // cell_height
    if 0 <= row < plate.shape[0] and 0 <= col < plate.shape[1]:
        plate[row, col] = 1 if plate[row, col] == 0 else 0
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