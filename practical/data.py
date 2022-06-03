from displayGraph import *
from utils import *
import matplotlib.pyplot as plt
import osmnx.distance as distance
from theoric.find_cycle import *

data = ox.graph_from_place("LaSalle, Quebec, Canada", network_type="drive")
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

nx.draw(undirectedNxGraph, **options)
plt.plot()

G = undirected_nxgraph_to_graph(undirectedNxGraph)
G.eulerize()
assert G.is_eulerian()
cycle, weight = find_eulerian_cycle_undirected(G.n, G.edges)
print(cycle, weight)
R = directed_graph_from_cycle(G.n, cycle)
show_path(R)