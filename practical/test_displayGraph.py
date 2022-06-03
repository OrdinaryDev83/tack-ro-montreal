from utils import *
from displayGraph import *

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from theoric.find_cycle import *

n = 10
E = random_edges(n, 25)
print(E)
G = Graph(n, E, True)
print(G.adj_matrix())

show_graph(G)

G.eulerize()
assert G.is_eulerian()

R = directed_graph_from_cycle(n, find_eulerian_cycle_undirected(G))
show_path(R)
