def cliqueCase(plate, clickX, clickY, cell_width, cell_height):
    turn = 0
    while clickX > cell_width:
        turn += 1
        clickX = clickX - cell_width

    placeX = turn * cell_width
    turn = 0

    while clickY > cell_height:
        turn += 1
        clickY = clickY - cell_height

    placeY = turn * cell_height

    plate[int(placeX / cell_width)][int(placeY / cell_height)] = 1
