from imports import *

edges_directed, edges_undirected = random_connected_graph(10, 15)
graph_u = Graph(edges_undirected)
graph_d = Graph(edges_directed)
g_u = directed_graph_to_nxgraph(graph_u)
g_d = directed_graph_to_nxgraph(graph_d)
show_graph(g_u)
show_graph(g_d)