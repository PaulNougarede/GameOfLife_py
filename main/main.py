import game as Game
import graphs.graphAlive as Graph

width, height = 800, 800
rows, cols = 100, 100
speed = 10

alive = Game.game(width, height, rows, cols, speed)
Graph.graph_alive(alive)
