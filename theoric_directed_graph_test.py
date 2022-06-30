from theoric.eulerize_directed import eulerize_directed
from theoric.utils import *
from theoric.utils_euler import find_eulerian_cycle_directed

nodes_number = 8

edges_directed, edges_undirected = random_connected_graph(nodes_number)

graph_directed = Graph(nodes_number, edges_directed)

nxgraph_directed = directed_graph_to_nxgraph(graph_directed)

show_nxgraph(nxgraph_directed)

edges_directed_eulerized = eulerize_directed(nodes_number, graph_directed.edges)

graph_directed_eulerized = Graph(nodes_number, edges_directed_eulerized)

print ("Successfully ?", graph_directed_eulerized.is_eulerian())

print("graph_directed_eulerized: ", graph_directed_eulerized.edges)

nxgraph_directed_eulerized = directed_graph_to_nxgraph(graph_directed_eulerized)

show_nxgraph(nxgraph_directed_eulerized)

eulerian_cycle_directed = find_eulerian_cycle_directed(nodes_number, graph_directed_eulerized.edges, 0)

print ("eulerian_cycle_directed: ", eulerian_cycle_directed)

show_cycle(nodes_number, eulerian_cycle_directed)

