from imports import *

nodes_numbers_list = [10, 20, 50, 100, 200, 500, 1000]

for i in nodes_numbers_list:
    edges_directed, edges_undirected = random_connected_graph(i)
    graph_u = Graph(10, edges_undirected, False)
    graph_d = Graph(10, edges_directed, True)
    g_u = undirected_graph_to_nxgraph(graph_u)
    g_d = directed_graph_to_nxgraph(graph_d)
    show_graph(g_u)
    show_graph(g_d)