import game as Game
import graphs.graphAlive as Graph
import menu as Menu
import pageAccueil as PageAccueil

width, height = 800, 800
rows, cols = 100, 100
speed = 10
start_game = False
rule_choice = 0

start_game = PageAccueil.pageAccueil()
if start_game:
    rule_choice = Menu.menu()
    alive = Game.game(width, height, rows, cols, speed, rule_choice)
    Graph.graph_alive(alive)
