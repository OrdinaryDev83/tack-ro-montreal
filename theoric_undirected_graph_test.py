from theoric.eulerize_directed import eulerize_directed
from theoric.utils import *
from theoric.utils_euler import find_eulerian_cycle_directed

nodes_number = 8


edges_directed, edges_undirected = random_connected_graph(nodes_number)

graph_undirected = Graph(nodes_number, edges_undirected)
graph_directed = Graph(nodes_number, edges_directed)

nxgraph_undirected = undirected_graph_to_nxgraph(graph_undirected)
nxgraph_directed = directed_graph_to_nxgraph(graph_directed)

show_graph(nxgraph_undirected)
show_graph(nxgraph_directed)

edges_undirected_eulerized = eulerize_undirected(nodes_number, graph_undirected.edges)
edges_directed_eulerized = eulerize_directed(nodes_number, graph_directed.edges)

graph_undirected_eulerized = Graph(len(edges_undirected_eulerized), edges_undirected_eulerized)
graph_directed_eulerized = Graph(len(edges_directed_eulerized), edges_directed_eulerized)

nxgraph_undirected_eulerized = undirected_graph_to_nxgraph(graph_undirected_eulerized)
nxgraph_directed_eulerized = directed_graph_to_nxgraph(graph_directed_eulerized)

show_graph(nxgraph_undirected_eulerized)
show_graph(nxgraph_directed_eulerized)

eulerian_cycle_undirected = find_eulerian_cycle_undirected(nodes_number, graph_undirected_eulerized.edges, 0)
eulerian_cycle_directed = find_eulerian_cycle_directed(nodes_number, graph_directed_eulerized.edges, 0)

print ("eulerian_cycle_undirected: ", eulerian_cycle_undirected)
print ("eulerian_cycle_directed: ", eulerian_cycle_directed)

show_graph(nxgraph_undirected_eulerized)
show_graph(nxgraph_directed_eulerized)

