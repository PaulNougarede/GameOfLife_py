import matplotlib.pyplot as plt


# Afficher le graphe de cellules vivantes en focntion du temps
# alives = tableau du total de cellules en vie à chaque tours
def graph_alive(alives):
    plt.plot(alives)
    plt.xlabel("Iteration")
    plt.ylabel("Cells")
    plt.title("Cells alive")
    plt.show()
