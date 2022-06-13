from displayGraph import *
from utils import *
import matplotlib.pyplot as plt
import osmnx.distance as distance
from theoric import *

"""data = ox.graph_from_place("LaSalle, Quebec, Canada", network_type="drive")
data = distance.add_edge_lengths(data)

fig, ax = ox.plot_graph(data)

undirectedNxGraph = ox.utils_graph.get_undirected(data)

positionsx = nx.get_node_attributes(undirectedNxGraph, "x")
positionsy = nx.get_node_attributes(undirectedNxGraph, "y")
position = {}
for pos in positionsx:
    position[pos] = (positionsx[pos], positionsy[pos])

options = {
    "node_size": 2,
    "arrowsize": 3,
    "min_source_margin": 1,
    "pos": position
}

G = undirected_nxgraph_to_graph(undirectedNxGraph)
show_graph(G, False)
G.eulerize()
assert G.is_eulerian()
show_graph(G, False)
cycle, weight = find_eulerian_cycle_undirected(G.n, G.edges)
R = directed_graph_from_cycle(G.n, cycle)
show_graph(R, True)"""

E = edges_from_matrix(10, random_adj_matrix(10, 10))
G = Graph(10, E, True)
show_graph("test", G)