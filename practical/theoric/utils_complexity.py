from imports import *

edges_directed, edges_undirected = random_connected_graph(10, 15)
graph_u = Graph(10, edges_undirected, False)
graph_d = Graph(10, edges_directed, True)
g_u = undirected_graph_to_nxgraph(graph_u)
g_d = directed_graph_to_nxgraph(graph_d)
show_graph(g_u)
show_graph(g_d)