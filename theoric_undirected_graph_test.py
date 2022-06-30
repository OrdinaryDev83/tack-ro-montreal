from theoric.eulerize_directed import eulerize_directed
from theoric.utils import *
from theoric.utils_euler import find_eulerian_cycle_directed

nodes_number = 8

edges_directed, edges_undirected = random_connected_graph(nodes_number)

graph_undirected = Graph(nodes_number, edges_undirected)

nxgraph_undirected = undirected_graph_to_nxgraph(graph_undirected)

show_nxgraph(nxgraph_undirected)

edges_undirected_eulerized = eulerize_undirected(nodes_number, graph_undirected.edges)

graph_undirected_eulerized = Graph(nodes_number, edges_undirected_eulerized)

nxgraph_undirected_eulerized = undirected_graph_to_nxgraph(graph_undirected_eulerized)

show_nxgraph(nxgraph_undirected_eulerized)

eulerian_cycle_undirected = find_eulerian_cycle_undirected(nodes_number, graph_undirected_eulerized.edges, 0)

print ("eulerian_cycle_undirected: ", eulerian_cycle_undirected)

show_cycle(nodes_number, eulerian_cycle_undirected)

