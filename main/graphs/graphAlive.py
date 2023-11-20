import matplotlib.pyplot as plt

# Afficher le graphe de cellules vivantes en fonction du temps
# alives = tableau du total de cellules en vie à chaque tours
def graph_alive(array):
    plt.plot(array)
    plt.xlabel("Iteration")
    plt.ylabel("Cells")
    plt.title("Cells alive")
    plt.show()

def graph_death(array):
    plt.plot(array)
    plt.xlabel("Iteration")
    plt.ylabel("Cells")
    plt.title("Cells dead")
    plt.show()

def graph_calcul(array):
    plt.plot(array)
    plt.xlabel("Iteration")
    plt.ylabel("temps")
    plt.title("Temps de calcul")
    plt.show()